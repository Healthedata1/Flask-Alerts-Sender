
'''
simple flask app to fetch data build a bundle and send as $process-message operation
use ps aux | grep Flask to find app and kill
'''

from flask import Flask, render_template, redirect, url_for, session, send_from_directory, request, Response
from werkzeug.contrib.cache import SimpleCache
import sys, datetime, uuid
from commonmark import commonmark
from json import dumps, load, loads
from requests import get, post, put
from pathlib import Path
import fhirtemplates # local templates
from importlib import import_module
from copy import deepcopy
import fhirclient.r4models.meta as M
import fhirclient.r4models.fhirdate as FD
import fhirclient.r4models.bundle as B
from utils import write_out, clear_dir, read_in
from time import sleep
import logging

logging.basicConfig(
        level=logging.DEBUG,
        #filename='/Users/ehaas/Documents/Python/Flask-PL/demo.log',
        format='[%(asctime)s] %(levelname)s in %(module)s %(lineno)d}: %(message)s',
        )

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'my secret key'

####### Globals #############
validate_me = False # to save for validation in IG

profile_list = dict(
Bundle = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/notifications-bundle",
MessageHeader = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/notifications-messageheader",
MessageHeader_admit = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/admit-notification-messageheader",
MessageHeader_transfer = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/transfer-notification-messageheader",
MessageHeader_discharge ="http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/dsicharge-notification-messageheader",
Condition = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/adt-notification-condition",
Coverage = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/adt-notification-coverage",
Encounter = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/adt-notification-encounter",
Patient = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient",
Practitioner = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner",
Location = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-location",
Organization = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization",
Provenance = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-provenance",
)


#enc_list = [i for i in range(905,911)] +['foo']# test R4 Server encounters
#enc_list = [588258,588265,588267,588274,588276,588283]+['foo']# test HAPI R4 Server encounters
enc_list = [ #for 64 = admit, 65 = transfer =, 66 = discharge
 '5fe62cd5-bfcf-4d3b-a1e9-80d6f75d6f82/_history/64',
 '5fe62cd5-bfcf-4d3b-a1e9-80d6f75d6f82/_history/66',
 '5fe62cd5-bfcf-4d3b-a1e9-80d6f75d6f82/_history/67',
 '542f9e32-4309-4277-81ce-12419f0d1294/_history/65',
 '542f9e32-4309-4277-81ce-12419f0d1294/_history/67',
 '542f9e32-4309-4277-81ce-12419f0d1294/_history/68',
 '02ba9ec6-0712-4715-8ba4-5485fc571403/_history/64',
 '02ba9ec6-0712-4715-8ba4-5485fc571403/_history/66',
 '02ba9ec6-0712-4715-8ba4-5485fc571403/_history/67',
 'foo/_history/1',
 'foo/_history/2',
 'foo/_history/3']


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
    'WildFHIR': 'http://wildfhir4.aegis.net/fhir4-0-1',
    }
#ref_server_name = "FHIR R4"
ref_server_name = "HAPI UHN R4"
alerts_servers = { # base_url for alerts server
    "Intermediary-Simulator": '/DaVinci-Notifications-Intermediary',
    "Alerts-RI": 'https://davinci-alerts-receiver.logicahealth.org/fhir',
    #'Cigna': 'https://ttbfdsk0pc.execute-api.us-east-1.amazonaws.com/dev',
    'WildFHIR': "http://wildfhir4.aegis.net/fhir4-0-1",
    #'One Medical': "https://dev.fhir.onemedical.io/r4",
    #'Guidewell-Edifecs': 'https://davinci.collablynk.com/payor/alerts',
    #'IBC': 'https://tbd'
    #"EMR Direct": 'https://stage.healthtogo.me:8181/fhir/r4/stage',
    'Tell Health': 'http://dev0.tell.health:8888/fhir',
    }

# some timestamp formats
now = f'{str(datetime.datetime.utcnow().isoformat())}Z' # get url freindly time stamp
id_safe_now = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S.%f')
RFC1123_date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
############################

# ************** fetch last bundle from local filesystem **************
def get_sessionfile(alerts_server='Alerts-RI'):
    f_name=session['f_names'][-1]
    app.logger.info(f'last file =  {session["f_names"][-1]}')
    data = read_in(in_path=app.root_path,f_name=f_name) # most recent saved bundle
    pydata = pyfhir(loads(data)) # convert to fhirclient model
    try:
        pydata.entry[0].resource.destination[0].name = alerts_server
        pydata.entry[0].resource.destination[0].endpoint = alerts_servers[alerts_server]
    except AttributeError:
        for e in pydata.entry:
            # sub_e = e[0].resource
            e.resource.entry[0].resource.destination[0].name = alerts_server
            e.resource.entry[0].resource.destination[0].endpoint = alerts_servers[alerts_server]
    return pydata.as_json()  #convert to dict

#  ************************** add profiles - Does not differentiate between deqm and US-Core for example ************************
def add_profile(r):
    try:
        r.meta.profile.append(profile_list[r.resource_type])# add profile if meta.profile already there
        r.meta.profile = list(set(r.meta.profile))# remove duplicate
        app.logger.info(f'******meta = {r.meta.profile}***')

    except AttributeError: # no profile
        #r.meta = M.Meta()
        try:
            r.meta.profile = [(profile_list[r.resource_type])]
            app.logger.info(f'******meta = {r.meta.profile}***')
        except AttributeError: # no meta
            r.meta = M.Meta()
            r.meta.profile = [(profile_list[r.resource_type])]
            app.logger.info(f'******meta = {r.meta.profile}***')

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

# *********************** Search Resource ********************
def search(Type,**kwargs):
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
    #app.logger.info(f'****** params = {kwargs}*****')
    with get(r_url, headers=headers, params=kwargs) as r:
        # return r.status_code
        # view  output
        # return (r.json()["text"]["div"])
        if r.status_code <300 and r.json()["total"] > 0: # >0
            return r.json()["entry"][0]["resource"] # just the first for now
        else:
            return None

# *********************** Fetch Resource ********************
def fetch(Type,_id,ver=None):
    '''
    fetch resource by READ or VREAD method e.g. [base]/[Type]/[id]/{[_history]}/{[version]}
    return resource as fhirclient model
    '''
    headers = {
    'Accept':'application/fhir+json',
    'Content-Type':'application/fhir+json'
    }

    r_url = (f'{ref_server[ref_server_name]}/{Type.capitalize()}/{_id}/_history/{ver}'
            if ver else f'{ref_server[ref_server_name]}/{Type.capitalize()}/{_id}')
    app.logger.info(f'****** r_url = {r_url}***')
    for attempt in range(5): #retry request up to ten times
        sleep(1)  # wait a bit between retries
        with get(r_url, headers=headers) as r:
            # return r.status_code
            # view  output
            # return (r.json()["text"]["div"])
            if r.status_code <300:
                return r.json() # just the first for now
    else:
        return None


# ******************* update ref ****************************
# is uuid first then update assuming Type/id
def update_ref(ref):
    #app.logger.info(f'ref = {ref} ref type = {type(ref)}')
    try:
        return uuid.UUID(ref).urn
    except ValueError:   # not a valid UUID
        return ref

# ******************* Get Provenance ****************************
def get_prov(target, org, author, sender, activity, now):
    prov = getattr(fhirtemplates,f'prov_{activity}') # hardcoded template for now
    resource = pyfhir(prov) #convert to fhirclient model
    resource.id = str(uuid.uuid1())
    resource.recorded = FD.FHIRDate(f'{str(now.isoformat())}Z')
    resource.target[0].reference = update_ref(target)
    resource.agent[0].who.reference = update_ref(author)
    resource.agent[0].onBehalfOf.reference = update_ref(org)
    resource.agent[1].who.reference = update_ref(sender)
    return resource


# *********************** POST Resource ********************
def post_bundle(alerts_server,headers,data):
    for attempt in range(5): #retry request up to ten times
        sleep(1)  # wait a bit between retries
        app.logger.info(f'endpoint = {alerts_server}')
        with post(f'{alerts_server}', headers=headers, data=data) as r:
            if r.status_code < 300:
              return(r)
    return(r)


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
    fhir_now = FD.FHIRDate(f'{str(now.isoformat())}Z')
    resources_copy = deepcopy(resources)
    app.logger.info(f"creating bundle of type = {type}...")
    bundle = pyfhir({'resourceType': 'Bundle'})
    #bundle.id = f'davinci-notifications-bundle-{now.strftime("%Y%m%d%H%M%S.%f")}'
    bundle.id = str(uuid.uuid1())
    if validate_me and type == 'message': #add meta profiles
        bundle.meta = M.Meta()
        bundle.meta.profile = [profile_list["Bundle"]]
        bundle.meta.lastUpdated = fhir_now
    bundle.type = type
    bundle.timestamp = fhir_now
    bundle.entry = []
    ref_map = {}
    for r in resources_copy:  #  append list of resources create replace id with uuids.
        app.logger.info(f'res = {r}')
        entry = B.BundleEntry()
        old_ref = f'{r.resource_type}/{r.id}'
        try:
           entry.fullUrl = uuid.UUID(r.id).urn # TODO get new uuid
        except ValueError:
           app.logger.info(f'resource = {r.resource_type} id = {r.id} is not uuid')
           r.id = str(uuid.uuid1())
           entry.fullUrl = uuid.UUID(r.id).urn
        ref_map[old_ref] = entry.fullUrl
        if not validate_me: #remove meta profiles
             if r.meta: #remove meta
                r.meta = None
        #if r.resource_type is not "MessageHeader":
            #r.id = None #remove old_ids
        r.text = None #remove text
        entry.resource = r
        if type in ['transaction', 'batch']:
            entry.request = B.BundleEntryRequest(dict
                        (
                        method = 'POST',
                        url = '$process-message'
                        )
                        )

        bundle.entry.append(entry)
    #app.logger.info(f'ref_map = {dumps(ref_map, indent = 2)}')
    #app.logger.info(f'meta elements = {[i.resource.meta.profile for i in bundle.entry]}')
    b_json = dumps(bundle.as_json(), indent=2)
    # replace old references with new urns
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
    #app.logger.info(f'****** args={args}***')
    try:
        app.logger.info(f'****** value type value={type(value)}***')
        for arg in args:
            #app.logger.info(f'****** arg = {arg}***')
            #app.logger.info(f'****** getattr({value},{arg}) = {getattr(value,arg)}***')
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
    try:
        for f_name in session['f_names']:
            app.logger.info(f'******* clear out {app.root_path}/testoutput{f_name} from  = {session}')
            clear_dir(out_path=app.root_path,f_name=f_name)
    except:
        pass
    session['my_encounters']=[]
    session['f_names']=[]
    session['resource_list']=[]

    app.logger.info(f'******* sessions = {session}')
    #cache.get('f_name') #clear upload files if present in cache.
    #cache.clear()  # clear all the cache *TODO  switch over to db*


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

@app.route("/not_found/<type>/", defaults={'r_id': None,'hx': None,'ver': None })
@app.route("/not_valid/<type>/<r_id>", defaults={'hx': None,'ver': None })
@app.route("/not_valid/<type>/<r_id>/<hx>/<ver>")
def resource_not_found(type, hx, ver, r_id):
    my_string='''
>Woops, that resource `{type}/{r_id}/{hx}/{ver}` doesn't exist! (0 search results)

-  Click on the home button in the nav bar and try a different id
'''.format(type= type,r_id=r_id, hx=hx,ver=ver)
    return render_template('sub_template1.html',
                           my_string=my_string,
                           title="Resource not found error",
                           current_time=datetime.datetime.now(),
                           )

@app.route("/not_valid/<type>/<r_id>", defaults={'ver': None })
@app.route("/not_valid/<type>/<r_id>/_history/<ver>")
def resource_not_valid(type, ver, r_id=None):
    my_string='''
>Woops, that resource `{type}/{r_id.split("#")[0]}` is invalid. The element {r_id.split("#")[1]} doesn't exist!

-  Click on the home button in the nav bar and try a different id
'''.format(type= type,r_id=r_id)
    return render_template('sub_template1.html',
                           my_string=my_string,
                           title="Resource not valid error",
                           current_time=datetime.datetime.now(),
                           )

@app.route("/Encounter/<string:r_id>", defaults={'hx': None,'ver': None })
@app.route("/Encounter/<string:r_id>/<string:hx>/<string:ver>")  # get the encounter and fetch the others and bundle em together!
def r_id(r_id, hx, ver):
    '''
      Fetch encounter
    '''
    batch = False
    encounters = []
    session['my_encounters']=[]
    app.logger.info(f'r_id = {r_id}')
    if r_id == 'batch':
        batch = True
        r_ids = enc_list[:-3]
    else:
        r_ids = [f'{r_id}/{hx}/{ver}']
    for my_id in r_ids:
        r_id, hx, ver = my_id.split('/')
        session['my_encounters'].append((r_id,ver))  # save encounter id and ver for this session
        app.logger.info(f'****** see what is in session = {session}')
        resource = fetch('Encounter', _id=r_id, ver=ver ) # fetch encounter resource by id as dict
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
            encounters.append(resource)

        else:
            return redirect(url_for('resource_not_found', type='Encounter', r_id=r_id))

        app.logger.info(f'******resource id={resource.id}***')
        app.logger.info(f'******estimated file size ={str(sys.getsizeof(resource.as_json())/1024)} "KB"***')

        #cache.set('encounters', encounters, timeout=60*15 )
        '''set cache to use during the session.
        assuming single user for now to keep it simple
        keep data for 15 minutes
        '''
    #app.logger.info(f'****** line 454 see what is in cache = {cache.get("encounters")}***')
    return render_template('sub_template4.html',
            r_id=','.join(r_ids),
           title= "Encounter",
           r_type='Encounter',
           r_pyfhir=encounters,
           batch = batch,
           )

@app.route("/MessageBundle", methods=["POST", "GET"])
def mb():
    '''
    fetch encounter ids - 1 for single bundle, multiple for batching using a transaction bundle
    create messageheader, coverage, orgs 1 and 2
    fetch graph of resources as list
    create bundle
    '''

    ################### Assemble Bundle ################################
    app.logger.info(f'****** line 492 see what is in session = {session}***')
    #app.logger.info(f'****** line 465 see what is in cache = {cache.get("encounters")}***')

    #encounters = cache.get("encounters") # get resources from cache
    session['resource_list'] = []
    message_bundles =[]
    now = datetime.datetime.utcnow()

    ################
    #for loop over encounters,  if encounter length > 1 then create transaction Bundles
    #################
    for r_id, ver in session['my_encounters']:  #encounters:
        encounter =fetch('Encounter', _id=r_id, ver=ver) #as dict
        encounter = pyfhir(r_dict=encounter) # convert encounter to pyfhir instance
        add_profile(encounter) # add profile if not already there
        resources = [encounter]
        # create messageheader
        mh = getattr(fhirtemplates,'messageheader') # resources as dict
        mh = pyfhir(mh) #convert to fhirclient
        mh.id = str(uuid.uuid1())
        mh.focus[0].reference = f"Encounter/{encounter.id}"

        if encounter.status == "in-progress" and encounter.class_fhir.code == "EMER":
            mh.eventCoding.code = 'notification-admit'
            mh.eventCoding.display = 'Notification Admit'
        elif encounter.status == "in-progress" and encounter.class_fhir.code == "IMP":
            mh.eventCoding.code =  'notification-transfer'
            mh.eventCoding.display = 'Notification Transfer'
            mh.meta.profile[1] = profile_list['MessageHeader_transfer']
        elif encounter.status == "finished":
            mh.eventCoding.code =  'notification-discharge'
            mh.eventCoding.display = 'Notification Discharge'
            mh.meta.profile[1] = profile_list['MessageHeader_discharge']


        # TODO add discharge subtypes and handle other statuses
        mh.focus[0].display = f'{mh.eventCoding.display}({encounter.type[0].text})'

        # mh.destination[0].name = list(alerts_servers.keys())[0]
        # mh.destination[0].endpoint = list(alerts_servers.values())[0]
        # TODO make a selection for the destination

        mh.sender.reference = encounter.serviceProvider.reference
        mh.sender.display = encounter.serviceProvider.display

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
            app.logger.info(f'******my_id = {my_id}')
            resource = fetch(Type, _id=my_id, ver=None)
            append_resource(resource, resources, Type=Type, id=my_id, is_req = is_req)

        resource = search('Condition',
                         patient=get_r_id(encounter,'subject','reference'), encounter=encounter.id,
                         ) # fetch condition
        append_resource(resource, resources, Type='Condition')

        resource = search('Coverage',
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

        # assume sender = author i.e. no separate sender initially save for intermediary
        # sender = getattr(fhirtemplates,'sender') # hardcode org for now
        # resource = pyfhir(sender) #convert to fhirclient model
        # add_profile(resource)
        # resources.append(resource)

        message_bundles.append(bundler(resources,'message', validate_me)) # returns as json string!
        session['resource_list'] = session['resource_list']+[f'{r.resource_type}/{r.id}' for r in resources]

        ################### End Assemble Bundle ################################
        # endfor loop over encounters,  if encounter length > 1 then create transaction Bundles
    # writing to ig examples file and running the IG Build:
    #f_name = f'davinci_notification_bundle_{now.strftime("%Y%m%d%H%M%S.%f")}.json'
    is_message_bundle = len(message_bundles) < 2

    if is_message_bundle:
        my_string=f"Getting Resources ready for Da Vinci Notification Message Bundle...for `Encounter/{encounter.id}`"
        app.logger.info(f' type my_string = {type(my_string)}')
        notification_bundle = message_bundles[0]
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
        f'for {",".join([r for r in session["resource_list"] if r.startswith("Encounter")])}'
        endpoint = 'transaction'

    b_id = loads(notification_bundle)["id"]
    f_name = f'davinci-notification-bundle-{b_id}.json'
    write_out(app.root_path, f_name, notification_bundle)
    app.logger.info(f'writing example notification bundle to {app.root_path}/test_output/{f_name}')
    session['f_names'].append(f_name) # keep track of f_names for session to delete later
    session.modified = True
    app.logger.info(f'****** see what is in session = {session}***')
    #app.logger.info(f'notification_bundle = {message_bundles[0]}')
    #cache.set('notification_bundle', notification_bundle, timeout=60*15 )
    #app.logger.info(f'****** line 574 see what is in cache = {cache.get("notification_bundle")}***')
    return render_template('sub_template5.html',
           my_string=my_string,
           title="Notification Bundle Prep",
           endpoint_urls = alerts_servers,
           endpoint = endpoint,
           notification_bundle = notification_bundle,
           b_id = loads(notification_bundle)["id"],
           )

@app.route("/ForwardBundle", methods=["POST"])
def fwd():
    '''
    reassemble message bundle:
    new bundle id, timestamp
    new messageheader.id and sender and source and destination
    if "intermed-no-change" is checked then add provenance for MH
    elif "intermed-change" is checked then add provenance for MH and and sender Org and remove coverage
    use prov template as dicts with variable
    add static text for forwarding messages
    '''
    now = datetime.datetime.utcnow()
    fhir_now = FD.FHIRDate(f'{str(now.isoformat())}Z')

    #get existing bundle and modify
    app.logger.info(f'****** see what is in session = {session}')
    f_name=session['f_names'][-1]
    app.logger.info(f'line nnnn f_name list = {session["f_names"]} f_name item = {f_name}')
    data = read_in(in_path=app.root_path,f_name=f_name) # most recent saved bundle
    #data = cache.get('notification_bundle')
    #app.logger.info(f'data = {data}')

    #convert to r4models
    b = pyfhir(loads(data))
    b.id = str(uuid.uuid1())
    b.timestamp = fhir_now
    mh =  b.entry[0].resource
    mh.id = str(uuid.uuid1())
    b.entry[0].fullUrl = uuid.UUID(mh.id).urn
    mh.sender.reference = "urn:uuid:4f7c997a-d6a4-11ea-814c-b5baa7182d44"  # hardcoded for now
    mh.sender.display = "Da Vinci Intermediary"  # hardcoded for now
    mh.source.name = "Da Vinci Intermediary Source Application"
    mh.source.endpoint = "https://example.org/Endpoints/P999"
    mh.source.contact.system = 'phone'
    mh.source.contact.value = '+1-800-555-5555'
    session['resource_list'][0] = f'MessageHeader/{mh.id}'

    ################### ADD Provenance ################################SHOULD BE REMOVED NOT NEEDED ANYMORE
    app.logger.info(f'************intermed is {request.form["intermed"]}*************')

    provenance = get_prov(target=f'MessageHeader/{mh.id}',
                        author=mh.author.reference,
                        org=mh.responsible.reference,
                        sender=mh.sender.reference,
                        activity=request.form['intermed'],
                        now=now, )
    prov_entry = B.BundleEntry()
    prov_entry.fullUrl = uuid.UUID(provenance.id).urn
    prov_entry.resource = provenance
    b.entry.insert(1, prov_entry)
    session['resource_list'].insert(1,f'Provenance/{provenance.id}')

    ################### ADD new sender Org ################################
    sender = getattr(fhirtemplates,'sender') # hardcode org for now
    org = pyfhir(sender) #convert to fhirclient model
    add_profile(org)
    org_entry = B.BundleEntry()
    org_entry.fullUrl = uuid.UUID(org.id).urn
    org_entry.resource = org
    b.entry.append(org_entry)
    session['resource_list'].append(f'Organization/{org.id}')

    ################### Remove Coverage and Referenced Org ################################SHOULD BE REMOVED NOT NEEDED ANYMORE
    if request.form['intermed'] == 'amend': # example for intermediary as sender with change in content
        try:
            coverage_index = next((index for (index, r) in enumerate(b.entry)
                   if r.resource.resource_type == 'Coverage'))
        except StopIteration:
            pass
        else:
            coverage = b.entry.pop(coverage_index).resource
            session['resource_list'].pop(coverage_index)
            payor_url = coverage.payor[0].reference
            try:
                payor_index = next((index for (index, r) in enumerate(b.entry)
                   if r.fullUrl == payor_url))
            except StopIteration:
                pass
            else:
                b.entry.pop(payor_index)
                session['resource_list'].pop(payor_index)

    # writing to ig examples file and running the IG Build:
    notification_bundle = dumps(b.as_json(), indent=2)
    #app.logger.info(f'notification_bundle = {message_bundles[0]}')
    f_name = f'davinci-notification-bundle-{b.id}.json'
    write_out(app.root_path, f_name, notification_bundle)
    app.logger.info(f'writing example notification bundle to {app.root_path}/test_output/{f_name}')
    session['f_names'].append(f_name) # keep track of f_names for session to delete later
    session.modified = True
    app.logger.info(f'****** see what is in session = {session}***')

    return render_template('sub_template5.html',
           title="Forwarding Notification Bundle Prep",
           endpoint_urls = alerts_servers,
           endpoint = '$process-message',
           notification_bundle = notification_bundle,
           b_id=b.id,
           forwarding = True,
           )

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    directory= f'{app.root_path}/test_output'
    return send_from_directory(directory= directory, filename=filename, as_attachment=True, mimetype='application/json')

@app.route("/Intermediary-Simulator/$process-message")
def intermediary():
    '''
    intermediary simulator
    return 200 status_code
    buttons for forwarding message bundle with and without changes

    if "intermed-no-change" modify Bundle to add provenance for MH with actor = transmitte and add sender organization
    elif "intermed-change" remove Coverage and modify Bundle to add provenance for MH with actor = Assemblerand add sender organization
    '''

    response = Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["date"] = RFC1123_date
    oo = {
        "resourceType": "OperationOutcome",
        "id": "intermediary-response",
        "text": {
            "status": "generated",
            "div": "<div><p><b>Operation Outcome for :</b></p><p>All OK</p><table class=\"grid\"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>information</td><td/><td>The message was received and the message has been fully processed</td><td/><td>informational</td></tr></table></div>"
        },
        "issue": [
            {
                "severity": "information",
                "code": "informational",
                "details": {
                    "text": "The message was received and the message has been fully processed"
                }
            }
        ]
    }
    # default to return the full resource
    representation = get_sessionfile('Intermediary-Simulator')
    return render_template('sub_template6.html',
                       my_string1=f"#### Response from Intermediary Simulator Server: **200**",
                       my_string2="url = [base]/FHIR/R4/Intermediary-Simulator/$process-message",
                       title="$process-message Response From Intermediary-Simulator",
                        headers = dict(response.headers),
                        oo = representation,
                        intermed=True,
                        )

@app.route("/<string:alerts_server>/$process-message")
def process_message(alerts_server):
        '''
        upload message to process-message endpoint
        return operation outcome
        '''
        headers = {
        'Accept':'application/fhir+json',
        'Content-Type':'application/fhir+json',
        'Authorization':'Bearer heqfnVgiMGCJuef',  #if alerts_server == "One Medical" else None,
        }
        app.logger.info(f'*******alerts_server = {alerts_server}******')
        app.logger.info(f'****** see what is in session = {session}')
        data = get_sessionfile(alerts_server)
        #app.logger.info(f'data = {data}')
        #with post(f'{alerts_servers[alerts_server]}/$process-message', headers=headers, data=data) as r:
        r = post_bundle(alerts_server=f'{alerts_servers[alerts_server]}/$process-message', headers=headers, data=dumps(data))
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
        'Content-Type':'application/fhir+json',
        #'Authorization':'Bearer heqfnVgiMGCJuef',  #if alerts_server == "One Medical" else None,
        }

        #data = cache.get('notification_bundle')
        app.logger.info(f'*******alerts_server = {alerts_server}******')
        app.logger.info(f'*******alerts_server $process-message url = {alerts_servers[alerts_server]}******')
        data = get_sessionfile(alerts_server)
        #app.logger.info(f'data = {data}')
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
