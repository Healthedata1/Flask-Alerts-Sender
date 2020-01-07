from importlib import import_module
from pprint import pprint
from functools import reduce

resources = []

def pyfhir(r_dict, fhir_resource=None, fhir_attribute=None):
    '''
    input is resource instance as r_dict
    output is fhirclient class instance
    '''
    fhir_resource = fhir_resource if fhir_resource else r_dict['resourceType']
    fhir_attribute = fhir_attribute if fhir_attribute else fhir_resource
    MyClass = getattr(import_module(
                f"fhirclient.r4models.{fhir_resource.lower()}"
                )
                ,fhir_attribute
                )
    # Instantiate the class (pass arguments to the constructor, if needed)
    instance = MyClass(r_dict, strict=False)
    return(instance)

r_dict = {
  "resourceType": "Encounter",
  "id": "11",
  "meta": {
    "versionId": "1",
    "lastUpdated": "2019-09-17T22:02:19.290+00:00",
    "source": "#1ac48e14302628ae"
  },
  "subject": {
    "reference": "Patient/6"
  },
  "period": {
    "start": "2019-09-17T21:52:19+00:00"
  },
  "location": [
    {
      "location": {
        "reference": "Location/8",
        "display": "ER, 8100bcac-c2af-4287-98cf-20c69b98f60b"
      },
      "status": "active",
      "period": {
        "start": "2019-09-17T21:52:19+00:00",
        "end": "2019-09-17T21:57:19+00:00"
      }
    },
    {
      "location": {
        "reference": "Location/9",
        "display": "Ward 1, Room d8302386-8ac1-451e-9c8a-63599aeb597b, Bed 1"
      },
      "status": "active",
      "period": {
        "start": "2019-09-17T21:57:19+00:00"
      }
    }
  ]
}

def safegetattr(obj):
    """Returns None no attribute"""
    try:
        print(eval(obj))
    except AttributeError:
        print("none")


instance = pyfhir(r_dict)
instance.status = "completed"
instance.class_fhir = pyfhir({"code":"amb"}, "Coding")
pprint(instance.as_json())




print(f'access attribute if exists using gettattr: getattr(instance,"status", None)= {getattr(instance,"status", None)}')
safegetattr("instance.location[0].location.reference")
resources.append(instance)

from json import dumps, loads

r_json = dumps(r_dict)
r_json_list = [r_json]
r_new_dict_list = [loads(r_json) for r_json in r_json_list]

print([pyfhir(r) for r in r_new_dict_list])

b = pyfhir({},'Bundle')



print(b)

pprint(dir(b))
pprint(b.elementProperties())
print(b.id)
print(b.timestamp)

MyClass = getattr(import_module(
                "fhirclient.r4models.bundle"
                )
                ,"BundleEntry"
                )

be = MyClass({})
be.fullUrl = 'foo'
print(be.as_json())

be = pyfhir({'fullUrl': 'foo'},'Bundle', 'BundleEntry')

print(be)
print(be.as_json())
pprint(be.elementProperties())
