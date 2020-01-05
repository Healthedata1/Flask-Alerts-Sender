
'''
simple flask app to fetch data build a bundle and send as $process-message operation
use ps aux | grep Flask to find app and kill
'''

from flask import Flask, render_template, redirect, url_for, session, send_from_directory
from werkzeug.contrib.cache import SimpleCache
import sys, datetime, uuid
from json import load, dumps, loads
from requests import get, post, put
from commonmark import commonmark
import fhirtemplates # local templates
from importlib import import_module
from pathlib import Path
from copy import deepcopy
import fhirclient.r4models.meta as M
import fhirclient.r4models.fhirdate as FD
import fhirclient.r4models.bundle as B
from utils import write_out, clear_dir


app = Flask(__name__, static_url_path='/static')
UPLOAD_FOLDER = '/test_output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'my secret key'
cache = SimpleCache()

####### Globals #############
validate_me = False # to save for validation in IG

profile_list = dict(
Bundle = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/notifications-bundle",
MessageHeader = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/notifications-messageheader",
MessageHeader_admit = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/admit-notification-messageheader",
MessageHeader_discharge ="http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/dsicharge-notification-messageheader",
Condition = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/admit-discharge-notification-condition",
Coverage = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/admit-discharge-notification-coverage",
Encounter = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/admit-discharge-notification-encounter",
Patient = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient",
Practitioner = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner",
Location = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-location",
Organization = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization",
)

# admit if encounter in progess and type if class =
admit_types = dict(
            EMER = 'notification-admit-er',
            IMP = 'notification-admit-inpatient',
            OBSENC = 'notification-admit-forobservation',
            AMB = 'notification-admit-ambulatory',
        )
# discharge if encounter completed

enc_list = [i for i in range(905,911)] +['foo']# test R4 Server encounters

get_ids = [# [{name:name, Type:Type, args=(args), is_req=bool}]
    dict(
    name = 'patient',
    Type = 'Patient',
    args = ('subject','reference'),
    is_req=True,
    ),
    dict(
    name = 'location',
    Type = 'Location',
    args = ('location','location','reference'),
    is_req=True,
    ),
    dict(
    name = 'practitioner',
    Type = 'Practitioner',
    args = ('participant','individual','reference'),
    is_req=False,
    ),
    dict(
    name = 'service_provider',
    Type = 'Organization',
    args = ('serviceProvider','reference'),
    is_req=False,
    ),
]

ref_server =  {  # base_url for reference server - no trailing forward slash
    'FHIR R4': 'http://test.fhir.org/r4',
    'HAPI UHN R4': 'http://hapi.fhir.org/baseR4',
    'WildFHIR': 'http://wildfhir4.aegis.net/fhir4-0-0',
    }
ref_server_name = "FHIR R4"
alerts_servers = { # base_url for alerts server
    "Alerts-RI": 'https://davinci-alerts-receiver.logicahealth.org/fhir',
    'Cigna': 'https://ttbfdsk0pc.execute-api.us-east-1.amazonaws.com/dev',
    'WildFHIR': "http://wildfhir4.aegis.net/fhir4-0-0",
    }

# some timestamp formats
now = f'{str(datetime.datetime.utcnow().isoformat())}Z' # get url freindly time stamp
id_safe_now = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S.%f')

############################

#  ************************** add profiles ************************
def add_profile(r):
    try:
        r.meta.profile.append(profile_list[r.resource_type])# add profile if meta.profile already there
        r.meta.profile = list(set(r.meta.profile))# remove duplicate
    except AttributeError: # no profile
        #r.meta = M.Meta()
        try:
            r.meta.profile = [(profile_list[r.resource_type])]
        except AttributeError: # no meta
            r.meta = M.Meta()
            r.meta.profile = [(profile_list[r.resource_type])]

# *************************** check and append **************

def append_resource(resource, resources, Type, id="?", is_req=False):
    app.logger.info(f'******append_resources parameters: Type={Type}, id= {id}, is_req={is_req}***')
    if resource:
        r_pyfhir = pyfhir(r_dict=resource)
        add_profile(r_pyfhir)
        resources.append(r_pyfhir)
        app.logger.info(f'******resources={resources}***')
    elif is_req:
        return redirect(url_for('resource_not_found', type=Type, id=id))
    else:
        app.logger.info(f'no {Type}/{id} resource found')

#  ************************** get id ************************
def get_r_id(Type,*args):
    app.logger.info(f'****** args = {args}***')
    my_id = atterror_filter(Type, *args)
    app.logger.info(f'****** my_id = {my_id}***')
    if my_id.startswith("urn:uuid:"):
        app.logger.info(f'****** my_id = {my_id[9:]}***')
        return my_id[9:]
    if my_id.endswith(":-("):
        app.logger.info('****** my_id = "[no id]"***')
        return '[no id]'
    else:  # assume is Regular FHIR endpoint # ID
        app.logger.info(f'****** my_id = {my_id.split("/")[-1]}***')
        return my_id.split('/')[-1]

# *********************** Fetch Resource ********************
def fetch(Type,**kwargs):
    '''
    fetch resource by search parameters e.g. _id
    return resource as fhirclient model
    '''
    headers = {
    'Accept':'application/fhir+json',
    'Content-Type':'application/fhir+json'
    }

    r_url = f'{ref_server[ref_server_name]}/{Type.capitalize()}'
    app.logger.info(f'****** r_url = {ref_server[ref_server_name]}/{Type.capitalize()}***')
    app.logger.info(f'****** params = {kwargs}*****')
    with get(r_url, headers=headers, params=kwargs) as r:
        # return r.status_code
        # view  output
        # return (r.json()["text"]["div"])
        if r.status_code <300 and r.json()["total"] > 0: # >0
            return r.json()["entry"][0]["resource"] # just the first for now
        else:
            return None

def pyfhir(r_dict, Type=None):
    '''
    input is resource instance as r_dict
    output is fhirclient class instance
    '''
    type = Type if Type else r_dict['resourceType']
    MyClass = getattr(import_module(f"fhirclient.r4models.{type.lower()}"),type)
    # Instantiate the class (pass arguments to the constructor, if needed)
    instance = MyClass(r_dict, strict=False)
    return(instance)

def bundler(resources, type, validate_me=False):
    # input list of fhirclient objects return a json copy of Bundle type = type
    now = datetime.datetime.utcnow()
    resources_copy = deepcopy(resources)
    app.logger.info(f"creating bundle of type = {type}...")
    bundle = pyfhir({'resourceType': 'Bundle'})
    bundle.id = f'davinci-notifications-bundle-{now.strftime("%Y%m%d%H%M%S.%f")}'
    if validate_me and type == 'message': #add meta profiles
        bundle.meta = M.Meta()
        bundle.meta.profile = [profile_list["Bundle"]]
    bundle.type = type
    bundle.timestamp = FD.FHIRDate(f'{str(now.isoformat())}Z')
    bundle.entry = []
    ref_map = {}
    for r in resources_copy:  #  append list of resources create replace id with uuids.
        app.logger.info(f'res = {r}')
        entry = B.BundleEntry()
        new_urn = uuid.uuid1().urn # TODO get new uuid
        old_ref = f'{r.resource_type}/{r.id}'
        ref_map[old_ref] = new_urn
        entry.fullUrl = new_urn
        if not validate_me: #remove meta profiles
             if r.meta: #remove meta
                r.meta = None
        r.id = None #remove old_ids
        r.text = None #remove textB
        entry.resource = r
        if type in ['transaction', 'batch']:
            entry.request = B.BundleEntryRequest(dict
                        (
                        method = 'POST',
                        url = '$process-message'
                        )
                        )

        bundle.entry.append(entry)
    app.logger.info(f'ref_map = {dumps(ref_map, indent = 4)}')
    b_json = dumps(bundle.as_json(), indent=4)
    for old_ref, new_urn in ref_map.items():
        b_json = b_json.replace(old_ref, new_urn)
    return(b_json)


@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

@app.template_filter()
def markdown(text, *args, **kwargs):
    return commonmark(text, *args, **kwargs)

"""
@app.template_filter()  # to handle KeyError exception in Jinja for dicts
def keyerror_filter(value, *args):
    app.logger.info(f'****** args ={args}***')
    try:
        app.logger.info(f'****** value type value={type(value)}***')
        for arg in args:
            app.logger.info(f'****** arg = {arg}***')
            app.logger.info(f'****** value[{arg}] = ***')
            value = value[arg][0] if isinstance(value[arg], list) else value[arg]
        return (value)
    except KeyError:
        return (f"Resource has no <code>{'.'.join(args)}</code> element :-(")
"""


@app.template_filter()  # to handle AttributeError exception in Jinja for classes
def atterror_filter(value, *args):
    app.logger.info(f'****** args={args}***')
    try:
        app.logger.info(f'****** value type value={type(value)}***')
        for arg in args:
            app.logger.info(f'****** arg = {arg}***')
            app.logger.info(f'****** getattr({value},{arg}) = {getattr(value,arg)}***')
            value = getattr(value, arg)[0] if isinstance(getattr(value,arg), list) else getattr(value,arg)
            app.logger.info(f'****** value = {value} , type = {type(value)}***')
        return (value)
    except AttributeError:
        return (f"Resource has no <code>{'.'.join(args)}</code> element :-(")

app.jinja_env.filters['datetimefilter'] = datetimefilter
app.jinja_env.filters['markdown'] = markdown
# app.jinja_env.filters['keyerror_filter'] = keyerror_filter
app.jinja_env.filters['atterror_filter'] = atterror_filter

@app.route("/")
def template_test():
    clear_dir(out_path=app.root_path, f_name = cache.get('f_name')) #clear upload files if present in cache.
    cache.clear()  # clear all the cache
    my_string='''This is a simple Flask App FHIR Facade which:

For single "real-time" Notifications:

  1. Fetches *Admit* and *Discharge* Encoounters from the {ref_server} Reference Server
  1. Builds the Da Vinci Notifications Message Bundle
  1. Submits the Message to the nominated endpoint using the `$process-message` operation
  1. Receives and displays the $process-message operation response from the server

For a Batch Transaction of multiple Notification:

  1. Fetches all the relevant *Admit* and *Discharge* Encoounters from the {ref_server} Reference Server
  1. Builds a transaction Bundle with:
     1. the Da Vinci Notifications Message Bundle as entries
     1. `POST` for the request method
     1. `/$process-message` for the request url
  1. Submits the transaction Bundle to the nominated endpoint using the `POST` operation
  1. Receives and displays the "transaction-response" response from the server.
'''.format(ref_server=ref_server_name)
    return render_template(
        'template.html',
         ref_server=ref_server_name,
         enc_list=enc_list,
         title="Index",
         )

@app.route("/home")  # reroute to "/"
def home():
    return redirect('/')

@app.route("/about")
def about():
    my_string='''This is a simple python Flask App FHIR Facade which:

 - Fetches *Admit* and *Discharge* Encounters from the {ref_server} Reference Servers
 - Build the Da Vinci Notifications Message
 - Submit the Message to the nominated endpoint using the $process-message operation

 The source code can be found on *github*: <https://github.com/Healthedata1/Flask-Alerts-Sender>

 This application is deployed on [![pythonanywhere](https://www.pythonanywhere.com/static/anywhere/images/PA-logo.svg)](https://www.pythonanywhere.com/)
 '''.format(ref_server=ref_server_name)
    return render_template('sub_template1.html',
                           my_string=my_string,
                           title="About",
                           current_time=datetime.datetime.now(),
                           )

@app.route("/contact")
def contact():
    return render_template('sub_template2.html'
                           , my_string="Contact Information",
                           title="Contact Us", current_time=datetime.datetime.now(),
                            )

@app.route("/not_found/<type>/")
@app.route("/not_found/<type>/<r_id>")
def resource_not_found(type, r_id=None):
    my_string='''
>Woops, that resource `{type}/{r_id}` doesn't exist! (0 search results)

-  Click on the home button in the nav bar and try a different id
'''.format(type= type,r_id=r_id)
    return render_template('sub_template1.html',
                           my_string=my_string,
                           title="Resource not found error",
                           current_time=datetime.datetime.now(),
                           )

@app.route("/not_valid/<type>/<r_id>")
def resource_not_valid(type, r_id=''):
    my_string='''
>Woops, that resource `{type}/{r_id.split("#")[0]}` is invalid. The element {r_id.split("#")[1]} doesn't exist!

-  Click on the home button in the nav bar and try a different id
'''.format(type= type,r_id=r_id)
    return render_template('sub_template1.html',
                           my_string=my_string,
                           title="Resource not valid error",
                           current_time=datetime.datetime.now(),
                           )


@app.route("/<string:r_type>/<string:r_ids>")  # get the encounter and fetch the others and bundle em together!
def r_id(r_type, r_ids):
    '''
    General approach
    fetch encounter ids - 1 for single bundle, multiple for batching using a transaction bundle
    create messageheader, coverage, orgs 1 and 2
    fetch graph of resources as list
    create bundle
    '''
    app.logger.info(f'************r_ids={r_ids.split(",")}*************')
    if r_type == "Encounter":
        encounters = []
        for r_id in r_ids.split(','):
            resource = fetch(r_type, _id=r_id) # fetch encounter resource by id as dict
            if resource:
                resource = pyfhir(r_dict=resource) # convert encounter to pyfhir instance
                add_profile(resource) # add profile if not already there
                ##### check to see if status and class present #####
                try:
                    r_status = resource.status
                except:
                    return redirect(url_for('resource_not_valid', type='Encounter', r_id=f'{r_id}#status'))
                try:
                    r_class = resource.class_fhir
                except:
                    return redirect(url_for('resource_not_valid', type='Encounter', r_id=f'{r_id}#class'))

                #session['encounter'] = resource.as_json()  # save encounter class as dict for this session
                encounters.append(resource)

            else:
                return redirect(url_for('resource_not_found', type='Encounter', r_id=r_id))

            app.logger.info(f'******resource id={resource.id}***')
            app.logger.info(f'******estimated file size ={str(sys.getsizeof(resource.as_json())/1024)} "KB"***')

        cache.set('encounters', encounters, timeout=60*15 )
        '''set cache to use during the session.
        assuming single user for now to keep it simple
        keep data for 15 minutes
        '''

        return render_template('sub_template4.html',
               title=f"{r_type}: {r_ids}",
               r_type = r_type,
               r_id=r_ids,
               r_pyfhir=encounters,
               )
    else:
        ################### Assemble Bundle ################################
        app.logger.info(f'******see what is in cache = {cache.get("encounters")}***')

        encounters = cache.get("encounters") # get resources from cache
        resource_list=[]
        message_bundles =[]
        ################
        #for loop over encounters,  if encounter length > 1 then create transaction Bundles
        #################
        for encounter in encounters:
            resources = [encounter]
            #+++ create messageheader
            mh = getattr(fhirtemplates,'messageheader') # resources as dict
            mh = pyfhir(mh) #convert to fhirclient
            now = datetime.datetime.utcnow()
            mh.id = f'messageheader-{now.strftime("%Y%m%d%H%M%S.%f")}'
            mh.focus[0].reference = f"Encounter/{encounter.id}"
            if encounter.status == "in-progress":
                try:
                    mh.eventCoding.code =  admit_types[encounter.class_fhir.code]
                    mh.eventCoding.display = mh.eventCoding.code.replace('-', ' ').title()
                    mh.focus[0].display = f'{mh.eventCoding.display}({encounter.type[0].text})'
                except KeyError:
                    pass
            elif encounter.status == "completed":
                mh.eventCoding.code =  'notification-discharge'
                mh.eventCoding.display = 'Notification Discharge'
                mh.meta.profile = profile_list['MessageHeader_discharge']
            # TODO add discharge subtypes and handle other statuses

            mh.destination[0].name = list(alerts_servers.keys())[0]
            mh.destination[0].endpoint = list(alerts_servers.values())[0]
            # TODO make a selection for the destination

            mh.sender.reference = 'Organization/sending_organization'  # hardcoded for now
            mh.sender.display = "Acme Message Sender"  # hardcoded for now

            mh.author.reference = encounter.participant[0].individual.reference
            mh.author.display = encounter.participant[0].individual.display

            mh.responsible.reference = encounter.serviceProvider.reference
            mh.responsible.display = encounter.serviceProvider.display

            resources.insert(0, mh)

            for i in get_ids:  # [{Type:Type, args=(args)}]
                Type = i['Type']
                args = i['args']
                is_req = i['is_req']
                my_id = get_r_id(encounter,*args)
                resource = fetch(Type, _id=my_id)
                append_resource(resource, resources, Type=Type, id=my_id, is_req = is_req)



            resource = fetch('Condition',
                             patient=get_r_id(encounter,'subject','reference'), encounter=encounter.id,
                             ) # fetch condition
            append_resource(resource, resources, Type='Condition')

            resource = fetch('Coverage',
                             patient=get_r_id(encounter,'subject','reference'),
                              ) # fetch coverage
            coverage = pyfhir(r_dict=resource)
            append_resource(resource, resources, Type='Coverage')

            if coverage:
                my_id = get_r_id(coverage,'payor','reference')
                resource = fetch('Organization',
                                _id=my_id,
                             ) # fetch coverage
                append_resource(resource, resources, Type='Organization', id=my_id)

            sender = getattr(fhirtemplates,'sender') # hardcode org for now
            resource = pyfhir(sender) #convert to fhirclient model
            add_profile(resource)
            resources.append(resource)
            message_bundles.append(bundler(resources,'message', validate_me)) # returns as json string!
            resource_list = resource_list + [f'{r.resource_type}/{r.id}' for r in resources]
            ################### End Assemble Bundle ################################
            # endfor loop over encounters,  if encounter length > 1 then create transaction Bundles

        if len(message_bundles) < 2:
            my_string=f"Getting Resources ready for Da Vinci Notification Message Bundle...for `Encounter/{encounter.id}`"
            app.logger.info(f' type my_string = {type(my_string)}')
            notification_bundle = message_bundles[0]
            #app.logger.info(f'notification_bundle = {message_bundles[0]}')
            endpoint = '$process-message'
        else:
            '''
            if message_bundles length > 2 then bundle as transaction.
            loop through message bundles and convert back to pyfhir object and save to array
            then bundle again in a transaction and get a transaction as json string back. (modify the function to do this too)
            '''
            pyfhir_messages = [pyfhir(loads(b)) for b in message_bundles]
            notification_bundle = bundler(pyfhir_messages,'transaction', validate_me)
            my_string=f'Getting Resources ready for Tansaction Bundle of Da Vinci Notification Message Bundle...\n'\
            f'for {",".join([r for r in resource_list if r.startswith("Encounter")])}'
            endpoint = 'transaction'

        # writing to ig examples file and running the IG Build:
        f_name = f'davinci_notification_bundle_{now.strftime("%Y%m%d%H%M%S.%f")}.json'
        write_out(app.root_path, f_name, notification_bundle)
        app.logger.info(f'writing example notification bundle to {app.root_path}/test_output/{f_name}')
        cache.set('f_name', f_name, timeout=60*60) # to delete upload files when start over

        '''set cache to use during the session.
        assuming single user for now to keep it simple
        keep data for 15 minutes
        '''
        cache.set('notification_bundle', notification_bundle, timeout=60*15 )

        return render_template('sub_template5.html',
               my_string=my_string,
               title="Notification Bundle Prep",
               resource_list=resource_list,
               endpoint_urls = alerts_servers,
               endpoint = endpoint,
               notification_bundle = notification_bundle,
               f_name=f_name,
               )

@app.route("/uploads")
def download():
    uploads = Path().joinpath(app.root_path, app.config['UPLOAD_FOLDER'])
    try:
        return send_from_directory(directory=uploads, filename='foo.json', as_attachment=True)
    except Exception as e:
        return str(e)

@app.route("/<string:alerts_server>/$process-message")
def process_message(alerts_server):
        '''
        upload message to process-message endpoint
        return operation outcome
        '''
        headers = {
        'Accept':'application/fhir+json',
        'Content-Type':'application/fhir+json'
        }

        data = cache.get('notification_bundle')
        app.logger.info(f'data = {data}')
        with post(f'{alerts_servers[alerts_server]}/$process-message', headers=headers, data=data) as r:
            try:
                oo = r.json()
            except:
                oo = {}
            app.logger.info(f'url= {alerts_servers[alerts_server]}\n\
                            r.status_code ={r.status_code}\n\
                            r.reason={r.reason}\n\
                            r.headers=\n\
                            {r.headers}\n')

        return render_template('sub_template6.html',
                           my_string1=f"#### Response from {alerts_server} Server: **{r.status_code}**",
                           my_string2=f"url = {alerts_servers[alerts_server]}/$process-message",
                           title="$process-message Response",
                            headers = dict(r.headers),
                            oo = oo
                            )
@app.route("/<string:alerts_server>/transaction")
def transaction(alerts_server):
        '''
        upload message to transaction endpoint
        return operation outcome
        '''
        headers = {
        'Accept':'application/fhir+json',
        'Content-Type':'application/fhir+json'
        }

        data = cache.get('notification_bundle')
        app.logger.info(f'data = {data}')
        with post(f'{alerts_servers[alerts_server]}/', headers=headers, data=data) as r:
            try:
                oo = r.json()
            except:
                oo = {}
            app.logger.info(f'url= {alerts_servers[alerts_server]}\n\
                            r.status_code ={r.status_code}\n\
                            r.reason={r.reason}\n\
                            r.headers=\n\
                            {r.headers}\n')

        return render_template('sub_template6.html',
                           my_string1=f"#### Response from {alerts_server} Server: **{r.status_code}**",
                           my_string2=f"url = {alerts_servers[alerts_server]}/",
                           title="Transaction Bundle Response",
                            headers = dict(r.headers),
                            oo = oo
                            )

if __name__ == '__main__':
    app.run(debug=True)
