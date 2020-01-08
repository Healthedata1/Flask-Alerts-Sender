from importlib import import_module
from pprint import pprint
from functools import reduce
from json import dumps
from pathlib import Path

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

t_bundle = {
    "entry": [
        {
            "fullUrl": "urn:uuid:b7d15e6b-07e1-4517-9f78-e3d4ab8a9c82",
            "request": {
                "method": "POST",
                "url": "Encounter"
            },
            "resource": {
                "id": "b7d15e6b-07e1-4517-9f78-e3d4ab8a9c82",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"
                    ]
                },
                "class": {
                    "code": "EMER",
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode"
                },
                "hospitalization": {
                    "dischargeDisposition": {
                        "coding": [
                            {
                                "code": "1",
                                "display": "Discharge to Home or Self Care (Routine Discharge)",
                                "system": "http://www.nubc.org/patient-discharge"
                            }
                        ],
                        "text": "Discharge to Home or Self Care (Routine Discharge)"
                    }
                },
                "identifier": [
                    {
                        "system": "https://github.com/synthetichealth/synthea",
                        "use": "official",
                        "value": "b7d15e6b-07e1-4517-9f78-e3d4ab8a9c82"
                    }
                ],
                "location": [
                    {
                        "location": {
                            "display": "HOLY FAMILY HOSPITAL",
                            "reference": "urn:uuid:09188b81-0d1d-453c-b0fa-203ef88c794c"
                        }
                    }
                ],
                "participant": [
                    {
                        "individual": {
                            "display": "Dr. Janeth814 Jakubowski832",
                            "reference": "urn:uuid:0000016f-57cb-cdac-0000-00000000014a"
                        }
                    }
                ],
                "period": {
                    "end": "2018-10-23T22:22:15-07:00",
                    "start": "2018-10-21T21:22:15-07:00"
                },
                "serviceProvider": {
                    "display": "HOLY FAMILY HOSPITAL",
                    "reference": "urn:uuid:a9f20dc1-5147-3789-bcef-bbecb41c5983"
                },
                "status": "in-progress",
                "subject": {
                    "display": "Mr. Elden718 Halvorson124",
                    "reference": "urn:uuid:06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b"
                },
                "type": [
                    {
                        "coding": [
                            {
                                "code": "261665006",
                                "display": "Unknown (qualifier value)",
                                "system": "http://snomed.info/sct"
                            }
                        ],
                        "text": "Unknown (qualifier value)"
                    }
                ],
                "resourceType": "Encounter"
            }
        },
        {
            "fullUrl": "urn:uuid:06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b",
            "request": {
                "method": "POST",
                "url": "Patient"
            },
            "resource": {
                "id": "06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
                    ]
                },
                "extension": [
                    {
                        "extension": [
                            {
                                "url": "ombCategory",
                                "valueCoding": {
                                    "code": "2106-3",
                                    "display": "White",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "text",
                                "valueString": "White"
                            }
                        ],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"
                    },
                    {
                        "extension": [
                            {
                                "url": "ombCategory",
                                "valueCoding": {
                                    "code": "2186-5",
                                    "display": "Not Hispanic or Latino",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "text",
                                "valueString": "Not Hispanic or Latino"
                            }
                        ],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity"
                    },
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName",
                        "valueString": "Marge692 Yost751"
                    },
                    {
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
                        "valueCode": "M"
                    },
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/patient-birthPlace",
                        "valueAddress": {
                            "city": "Rockland",
                            "country": "US",
                            "state": "Massachusetts"
                        }
                    },
                    {
                        "url": "http://synthetichealth.github.io/synthea/disability-adjusted-life-years",
                        "valueDecimal": 0.0
                    },
                    {
                        "url": "http://synthetichealth.github.io/synthea/quality-adjusted-life-years",
                        "valueDecimal": 18.0
                    }
                ],
                "text": {
                    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Generated by <a href=\"https://github.com/synthetichealth/synthea\">Synthea</a>.Version identifier: v2.5.0-164-gcf5ad87d\n .   Person seed: -7752864393210988204  Population seed: 1577725971884</div>",
                    "status": "generated"
                },
                "address": [
                    {
                        "extension": [
                            {
                                "extension": [
                                    {
                                        "url": "latitude",
                                        "valueDecimal": 42.757779285956644
                                    },
                                    {
                                        "url": "longitude",
                                        "valueDecimal": -71.14760946593316
                                    }
                                ],
                                "url": "http://hl7.org/fhir/StructureDefinition/geolocation"
                            }
                        ],
                        "city": "Methuen",
                        "country": "US",
                        "line": [
                            "715 Crona Corner"
                        ],
                        "postalCode": "01844",
                        "state": "MA"
                    }
                ],
                "birthDate": "2000-10-15",
                "communication": [
                    {
                        "language": {
                            "coding": [
                                {
                                    "code": "en-US",
                                    "display": "English",
                                    "system": "urn:ietf:bcp:47"
                                }
                            ],
                            "text": "English"
                        }
                    }
                ],
                "gender": "male",
                "identifier": [
                    {
                        "system": "https://github.com/synthetichealth/synthea",
                        "value": "06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b"
                    },
                    {
                        "system": "http://hospital.smarthealthit.org",
                        "type": {
                            "coding": [
                                {
                                    "code": "MR",
                                    "display": "Medical Record Number",
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                                }
                            ],
                            "text": "Medical Record Number"
                        },
                        "value": "06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b"
                    },
                    {
                        "system": "http://hl7.org/fhir/sid/us-ssn",
                        "type": {
                            "coding": [
                                {
                                    "code": "SS",
                                    "display": "Social Security Number",
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                                }
                            ],
                            "text": "Social Security Number"
                        },
                        "value": "999-87-1037"
                    },
                    {
                        "system": "urn:oid:2.16.840.1.113883.4.3.25",
                        "type": {
                            "coding": [
                                {
                                    "code": "DL",
                                    "display": "Driver's License",
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                                }
                            ],
                            "text": "Driver's License"
                        },
                        "value": "S99952689"
                    }
                ],
                "maritalStatus": {
                    "coding": [
                        {
                            "code": "S",
                            "display": "Never Married",
                            "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"
                        }
                    ],
                    "text": "Never Married"
                },
                "multipleBirthBoolean": False,
                "name": [
                    {
                        "family": "Halvorson124",
                        "given": [
                            "Elden718"
                        ],
                        "prefix": [
                            "Mr."
                        ],
                        "use": "official"
                    }
                ],
                "telecom": [
                    {
                        "system": "phone",
                        "use": "home",
                        "value": "555-903-1143"
                    }
                ],
                "resourceType": "Patient"
            }
        },
        {
            "fullUrl": "urn:uuid:eec76c92-2b4c-11ea-9734-a4d18ccf5172",
            "request": {
                "method": "POST",
                "url": "Coverage"
            },
            "resource": {
                "id": "eec76c92-2b4c-11ea-9734-a4d18ccf5172",
                "beneficiary": {
                    "reference": "urn:uuid:06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b"
                },
                "payor": [
                    {
                        "display": "Blue Cross Blue Shield",
                        "reference": "urn:uuid:eec77066-2b4c-11ea-9734-a4d18ccf5172"
                    }
                ],
                "status": "active",
                "subscriberId": "12345",
                "type": {
                    "text": "Blue Cross Blue Shield"
                },
                "resourceType": "Coverage"
            }
        },
        {
            "fullUrl": "urn:uuid:eec77066-2b4c-11ea-9734-a4d18ccf5172",
            "request": {
                "method": "POST",
                "url": "Organization"
            },
            "resource": {
                "id": "eec77066-2b4c-11ea-9734-a4d18ccf5172",
                "active": True,
                "address": [
                    {
                        "city": "Chicago",
                        "line": [
                            "Michigan Plaza"
                        ],
                        "postalCode": "60007",
                        "state": "IL"
                    }
                ],
                "identifier": [
                    {
                        "system": "http://hl7.org/fhir/sid/us-npi",
                        "value": "0000010005"
                    }
                ],
                "name": "Blue Cross Blue Shield",
                "telecom": [
                    {
                        "system": "phone",
                        "use": "work",
                        "value": "1-800-262-2583"
                    }
                ],
                "resourceType": "Organization"
            }
        },
        {
            "fullUrl": "urn:uuid:09188b81-0d1d-453c-b0fa-203ef88c794c",
            "request": {
                "method": "POST",
                "url": "Location"
            },
            "resource": {
                "id": "09188b81-0d1d-453c-b0fa-203ef88c794c",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-location"
                    ]
                },
                "address": {
                    "city": "METHUEN",
                    "country": "US",
                    "line": [
                        "70 EAST STREET"
                    ],
                    "postalCode": "01844",
                    "state": "MA"
                },
                "managingOrganization": {
                    "display": "HOLY FAMILY HOSPITAL",
                    "reference": "urn:uuid:a9f20dc1-5147-3789-bcef-bbecb41c5983"
                },
                "name": "HOLY FAMILY HOSPITAL",
                "position": {
                    "latitude": 42.742751,
                    "longitude": -71.178588
                },
                "status": "active",
                "telecom": [
                    {
                        "system": "phone",
                        "value": "9786870156"
                    }
                ],
                "resourceType": "Location"
            }
        },
        {
            "fullUrl": "urn:uuid:a9f20dc1-5147-3789-bcef-bbecb41c5983",
            "request": {
                "method": "POST",
                "url": "Organization"
            },
            "resource": {
                "id": "a9f20dc1-5147-3789-bcef-bbecb41c5983",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization"
                    ]
                },
                "active": True,
                "address": [
                    {
                        "city": "METHUEN",
                        "country": "US",
                        "line": [
                            "70 EAST STREET"
                        ],
                        "postalCode": "01844",
                        "state": "MA"
                    }
                ],
                "identifier": [
                    {
                        "system": "https://github.com/synthetichealth/synthea",
                        "value": "a9f20dc1-5147-3789-bcef-bbecb41c5983"
                    }
                ],
                "name": "HOLY FAMILY HOSPITAL",
                "telecom": [
                    {
                        "system": "phone",
                        "value": "9786870156"
                    }
                ],
                "type": [
                    {
                        "coding": [
                            {
                                "code": "prov",
                                "display": "Healthcare Provider",
                                "system": "http://terminology.hl7.org/CodeSystem/organization-type"
                            }
                        ],
                        "text": "Healthcare Provider"
                    }
                ],
                "resourceType": "Organization"
            }
        },
        {
            "fullUrl": "urn:uuid:0000016f-57cb-cdac-0000-00000000014a",
            "request": {
                "method": "POST",
                "url": "Practitioner"
            },
            "resource": {
                "id": "0000016f-57cb-cdac-0000-00000000014a",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner"
                    ]
                },
                "active": True,
                "address": [
                    {
                        "city": "METHUEN",
                        "country": "US",
                        "line": [
                            "70 EAST STREET"
                        ],
                        "postalCode": "01844",
                        "state": "MA"
                    }
                ],
                "gender": "female",
                "identifier": [
                    {
                        "system": "http://hl7.org/fhir/sid/us-npi",
                        "value": "330"
                    }
                ],
                "name": [
                    {
                        "family": "Jakubowski832",
                        "given": [
                            "Janeth814"
                        ],
                        "prefix": [
                            "Dr."
                        ]
                    }
                ],
                "telecom": [
                    {
                        "extension": [
                            {
                                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-direct",
                                "valueBoolean": True
                            }
                        ],
                        "system": "email",
                        "use": "work",
                        "value": "Janeth814.Jakubowski832@example.com"
                    }
                ],
                "resourceType": "Practitioner"
            }
        },
        {
            "fullUrl": "urn:uuid:5fe62cd5-bfcf-4d3b-a1e9-80d6f75d6f82",
            "request": {
                "method": "POST",
                "url": "Encounter"
            },
            "resource": {
                "id": "5fe62cd5-bfcf-4d3b-a1e9-80d6f75d6f82",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"
                    ]
                },
                "class": {
                    "code": "EMER",
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode"
                },
                "identifier": [
                    {
                        "system": "https://github.com/synthetichealth/synthea",
                        "use": "official",
                        "value": "5fe62cd5-bfcf-4d3b-a1e9-80d6f75d6f82"
                    }
                ],
                "location": [
                    {
                        "location": {
                            "display": "HOLY FAMILY HOSPITAL",
                            "reference": "urn:uuid:09188b81-0d1d-453c-b0fa-203ef88c794c"
                        }
                    }
                ],
                "participant": [
                    {
                        "individual": {
                            "display": "Dr. Janeth814 Jakubowski832",
                            "reference": "urn:uuid:0000016f-57cb-cdac-0000-00000000014a"
                        }
                    }
                ],
                "period": {
                    "end": "2018-10-21T22:22:15-07:00",
                    "start": "2018-10-21T21:22:15-07:00"
                },
                "serviceProvider": {
                    "display": "HOLY FAMILY HOSPITAL",
                    "reference": "urn:uuid:a9f20dc1-5147-3789-bcef-bbecb41c5983"
                },
                "status": "finished",
                "subject": {
                    "display": "Mr. Elden718 Halvorson124",
                    "reference": "urn:uuid:06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b"
                },
                "type": [
                    {
                        "coding": [
                            {
                                "code": "1234",
                                "display": "Examplotomy Encounter",
                                "system": "http://snomed.info/sct"
                            }
                        ],
                        "text": "Examplotomy Encounter"
                    }
                ],
                "resourceType": "Encounter"
            }
        },
        {
            "fullUrl": "urn:uuid:4ac41715-fcbd-421c-8796-9b2c9706dd3f",
            "request": {
                "method": "POST",
                "url": "Condition"
            },
            "resource": {
                "id": "4ac41715-fcbd-421c-8796-9b2c9706dd3f",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition"
                    ]
                },
                "category": [
                    {
                        "coding": [
                            {
                                "code": "encounter-diagnosis",
                                "display": "Encounter Diagnosis",
                                "system": "http://terminology.hl7.org/CodeSystem/condition-category"
                            }
                        ]
                    }
                ],
                "clinicalStatus": {
                    "coding": [
                        {
                            "code": "active",
                            "system": "http://terminology.hl7.org/CodeSystem/condition-clinical"
                        }
                    ]
                },
                "code": {
                    "coding": [
                        {
                            "code": "1234",
                            "display": "Examplitis",
                            "system": "http://snomed.info/sct"
                        }
                    ],
                    "text": "Examplitis"
                },
                "encounter": {
                    "reference": "urn:uuid:b7d15e6b-07e1-4517-9f78-e3d4ab8a9c82"
                },
                "onsetDateTime": "2018-10-21T21:22:15-07:00",
                "recordedDate": "2018-10-21T21:22:15-07:00",
                "subject": {
                    "reference": "urn:uuid:06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b"
                },
                "verificationStatus": {
                    "coding": [
                        {
                            "code": "confirmed",
                            "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status"
                        }
                    ]
                },
                "resourceType": "Condition"
            }
        },
        {
            "fullUrl": "urn:uuid:69c19eda-496b-42b2-ae3c-9629ec70b007",
            "request": {
                "method": "POST",
                "url": "Encounter"
            },
            "resource": {
                "id": "69c19eda-496b-42b2-ae3c-9629ec70b007",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"
                    ]
                },
                "class": {
                    "code": "EMER",
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode"
                },
                "hospitalization": {
                    "dischargeDisposition": {
                        "coding": [
                            {
                                "code": "1",
                                "display": "Discharge to Home or Self Care (Routine Discharge)",
                                "system": "http://www.nubc.org/patient-discharge"
                            }
                        ],
                        "text": "Discharge to Home or Self Care (Routine Discharge)"
                    }
                },
                "identifier": [
                    {
                        "system": "https://github.com/synthetichealth/synthea",
                        "use": "official",
                        "value": "69c19eda-496b-42b2-ae3c-9629ec70b007"
                    }
                ],
                "location": [
                    {
                        "location": {
                            "display": "BETH ISRAEL DEACONESS HOSPITAL - PLYMOUTH",
                            "reference": "urn:uuid:09178b24-9340-47ec-90b2-1aac03248cd5"
                        }
                    }
                ],
                "participant": [
                    {
                        "individual": {
                            "display": "Dr. Tommy814 Schmeler639",
                            "reference": "urn:uuid:0000016f-57cb-cdac-0000-0000000000dc"
                        }
                    }
                ],
                "period": {
                    "end": "2018-02-19T16:07:39-08:00",
                    "start": "2018-02-17T15:07:39-08:00"
                },
                "serviceProvider": {
                    "display": "BETH ISRAEL DEACONESS HOSPITAL - PLYMOUTH",
                    "reference": "urn:uuid:b1ddf812-1fdd-3adf-b1d5-32cc8bd07ebb"
                },
                "status": "in-progress",
                "subject": {
                    "display": "Mr. Garland107 Conn188",
                    "reference": "urn:uuid:b1cf5f57-b061-4b7f-aa9d-6283a121694b"
                },
                "type": [
                    {
                        "coding": [
                            {
                                "code": "261665006",
                                "display": "Unknown (qualifier value)",
                                "system": "http://snomed.info/sct"
                            }
                        ],
                        "text": "Unknown (qualifier value)"
                    }
                ],
                "resourceType": "Encounter"
            }
        },
        {
            "fullUrl": "urn:uuid:b1cf5f57-b061-4b7f-aa9d-6283a121694b",
            "request": {
                "method": "POST",
                "url": "Patient"
            },
            "resource": {
                "id": "b1cf5f57-b061-4b7f-aa9d-6283a121694b",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
                    ]
                },
                "extension": [
                    {
                        "extension": [
                            {
                                "url": "ombCategory",
                                "valueCoding": {
                                    "code": "2106-3",
                                    "display": "White",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "text",
                                "valueString": "White"
                            }
                        ],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"
                    },
                    {
                        "extension": [
                            {
                                "url": "ombCategory",
                                "valueCoding": {
                                    "code": "2186-5",
                                    "display": "Not Hispanic or Latino",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "text",
                                "valueString": "Not Hispanic or Latino"
                            }
                        ],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity"
                    },
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName",
                        "valueString": "Gina573 Terry864"
                    },
                    {
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
                        "valueCode": "M"
                    },
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/patient-birthPlace",
                        "valueAddress": {
                            "city": "Brookline",
                            "country": "US",
                            "state": "Massachusetts"
                        }
                    },
                    {
                        "url": "http://synthetichealth.github.io/synthea/disability-adjusted-life-years",
                        "valueDecimal": 0.0
                    },
                    {
                        "url": "http://synthetichealth.github.io/synthea/quality-adjusted-life-years",
                        "valueDecimal": 18.0
                    }
                ],
                "text": {
                    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Generated by <a href=\"https://github.com/synthetichealth/synthea\">Synthea</a>.Version identifier: v2.5.0-164-gcf5ad87d\n .   Person seed: 9133911975177377557  Population seed: 1577725971884</div>",
                    "status": "generated"
                },
                "address": [
                    {
                        "extension": [
                            {
                                "extension": [
                                    {
                                        "url": "latitude",
                                        "valueDecimal": 41.97243792772779
                                    },
                                    {
                                        "url": "longitude",
                                        "valueDecimal": -70.05957503171508
                                    }
                                ],
                                "url": "http://hl7.org/fhir/StructureDefinition/geolocation"
                            }
                        ],
                        "city": "Truro",
                        "country": "US",
                        "line": [
                            "660 Bernier Bridge Suite 5"
                        ],
                        "state": "MA"
                    }
                ],
                "birthDate": "2000-02-12",
                "communication": [
                    {
                        "language": {
                            "coding": [
                                {
                                    "code": "en-US",
                                    "display": "English",
                                    "system": "urn:ietf:bcp:47"
                                }
                            ],
                            "text": "English"
                        }
                    }
                ],
                "gender": "male",
                "identifier": [
                    {
                        "system": "https://github.com/synthetichealth/synthea",
                        "value": "b1cf5f57-b061-4b7f-aa9d-6283a121694b"
                    },
                    {
                        "system": "http://hospital.smarthealthit.org",
                        "type": {
                            "coding": [
                                {
                                    "code": "MR",
                                    "display": "Medical Record Number",
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                                }
                            ],
                            "text": "Medical Record Number"
                        },
                        "value": "b1cf5f57-b061-4b7f-aa9d-6283a121694b"
                    },
                    {
                        "system": "http://hl7.org/fhir/sid/us-ssn",
                        "type": {
                            "coding": [
                                {
                                    "code": "SS",
                                    "display": "Social Security Number",
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                                }
                            ],
                            "text": "Social Security Number"
                        },
                        "value": "999-45-9851"
                    },
                    {
                        "system": "urn:oid:2.16.840.1.113883.4.3.25",
                        "type": {
                            "coding": [
                                {
                                    "code": "DL",
                                    "display": "Driver's License",
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                                }
                            ],
                            "text": "Driver's License"
                        },
                        "value": "S99917866"
                    }
                ],
                "maritalStatus": {
                    "coding": [
                        {
                            "code": "S",
                            "display": "Never Married",
                            "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"
                        }
                    ],
                    "text": "Never Married"
                },
                "multipleBirthBoolean": False,
                "name": [
                    {
                        "family": "Conn188",
                        "given": [
                            "Garland107"
                        ],
                        "prefix": [
                            "Mr."
                        ],
                        "use": "official"
                    }
                ],
                "telecom": [
                    {
                        "system": "phone",
                        "use": "home",
                        "value": "555-572-6599"
                    }
                ],
                "resourceType": "Patient"
            }
        },
        {
            "fullUrl": "urn:uuid:eef77a68-2b4c-11ea-9734-a4d18ccf5172",
            "request": {
                "method": "POST",
                "url": "Coverage"
            },
            "resource": {
                "id": "eef77a68-2b4c-11ea-9734-a4d18ccf5172",
                "beneficiary": {
                    "reference": "urn:uuid:b1cf5f57-b061-4b7f-aa9d-6283a121694b"
                },
                "payor": [
                    {
                        "display": "UnitedHealthcare",
                        "reference": "urn:uuid:eef77c34-2b4c-11ea-9734-a4d18ccf5172"
                    }
                ],
                "status": "active",
                "subscriberId": "12345",
                "type": {
                    "text": "UnitedHealthcare"
                },
                "resourceType": "Coverage"
            }
        },
        {
            "fullUrl": "urn:uuid:eef77c34-2b4c-11ea-9734-a4d18ccf5172",
            "request": {
                "method": "POST",
                "url": "Organization"
            },
            "resource": {
                "id": "eef77c34-2b4c-11ea-9734-a4d18ccf5172",
                "active": True,
                "address": [
                    {
                        "city": "Minnetonka",
                        "line": [
                            "9800 Healthcare Lane"
                        ],
                        "postalCode": "55436",
                        "state": "MN"
                    }
                ],
                "identifier": [
                    {
                        "system": "http://hl7.org/fhir/sid/us-npi",
                        "value": "0000010006"
                    }
                ],
                "name": "UnitedHealthcare",
                "telecom": [
                    {
                        "system": "phone",
                        "use": "work",
                        "value": "1-888-545-5205"
                    }
                ],
                "resourceType": "Organization"
            }
        },
        {
            "fullUrl": "urn:uuid:09178b24-9340-47ec-90b2-1aac03248cd5",
            "request": {
                "method": "POST",
                "url": "Location"
            },
            "resource": {
                "id": "09178b24-9340-47ec-90b2-1aac03248cd5",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-location"
                    ]
                },
                "address": {
                    "city": "PLYMOUTH",
                    "country": "US",
                    "line": [
                        "275 SANDWICH STREET"
                    ],
                    "postalCode": "02360",
                    "state": "MA"
                },
                "managingOrganization": {
                    "display": "BETH ISRAEL DEACONESS HOSPITAL - PLYMOUTH",
                    "reference": "urn:uuid:b1ddf812-1fdd-3adf-b1d5-32cc8bd07ebb"
                },
                "name": "BETH ISRAEL DEACONESS HOSPITAL - PLYMOUTH",
                "position": {
                    "latitude": 41.897892,
                    "longitude": -70.62403
                },
                "status": "active",
                "telecom": [
                    {
                        "system": "phone",
                        "value": "5087462000"
                    }
                ],
                "resourceType": "Location"
            }
        },
        {
            "fullUrl": "urn:uuid:b1ddf812-1fdd-3adf-b1d5-32cc8bd07ebb",
            "request": {
                "method": "POST",
                "url": "Organization"
            },
            "resource": {
                "id": "b1ddf812-1fdd-3adf-b1d5-32cc8bd07ebb",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization"
                    ]
                },
                "active": True,
                "address": [
                    {
                        "city": "PLYMOUTH",
                        "country": "US",
                        "line": [
                            "275 SANDWICH STREET"
                        ],
                        "postalCode": "02360",
                        "state": "MA"
                    }
                ],
                "identifier": [
                    {
                        "system": "https://github.com/synthetichealth/synthea",
                        "value": "b1ddf812-1fdd-3adf-b1d5-32cc8bd07ebb"
                    }
                ],
                "name": "BETH ISRAEL DEACONESS HOSPITAL - PLYMOUTH",
                "telecom": [
                    {
                        "system": "phone",
                        "value": "5087462000"
                    }
                ],
                "type": [
                    {
                        "coding": [
                            {
                                "code": "prov",
                                "display": "Healthcare Provider",
                                "system": "http://terminology.hl7.org/CodeSystem/organization-type"
                            }
                        ],
                        "text": "Healthcare Provider"
                    }
                ],
                "resourceType": "Organization"
            }
        },
        {
            "fullUrl": "urn:uuid:0000016f-57cb-cdac-0000-0000000000dc",
            "request": {
                "method": "POST",
                "url": "Practitioner"
            },
            "resource": {
                "id": "0000016f-57cb-cdac-0000-0000000000dc",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner"
                    ]
                },
                "active": True,
                "address": [
                    {
                        "city": "PLYMOUTH",
                        "country": "US",
                        "line": [
                            "275 SANDWICH STREET"
                        ],
                        "postalCode": "02360",
                        "state": "MA"
                    }
                ],
                "gender": "male",
                "identifier": [
                    {
                        "system": "http://hl7.org/fhir/sid/us-npi",
                        "value": "220"
                    }
                ],
                "name": [
                    {
                        "family": "Schmeler639",
                        "given": [
                            "Tommy814"
                        ],
                        "prefix": [
                            "Dr."
                        ]
                    }
                ],
                "telecom": [
                    {
                        "extension": [
                            {
                                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-direct",
                                "valueBoolean": True
                            }
                        ],
                        "system": "email",
                        "use": "work",
                        "value": "Tommy814.Schmeler639@example.com"
                    }
                ],
                "resourceType": "Practitioner"
            }
        },
        {
            "fullUrl": "urn:uuid:542f9e32-4309-4277-81ce-12419f0d1294",
            "request": {
                "method": "POST",
                "url": "Encounter"
            },
            "resource": {
                "id": "542f9e32-4309-4277-81ce-12419f0d1294",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"
                    ]
                },
                "class": {
                    "code": "EMER",
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode"
                },
                "identifier": [
                    {
                        "system": "https://github.com/synthetichealth/synthea",
                        "use": "official",
                        "value": "542f9e32-4309-4277-81ce-12419f0d1294"
                    }
                ],
                "location": [
                    {
                        "location": {
                            "display": "BETH ISRAEL DEACONESS HOSPITAL - PLYMOUTH",
                            "reference": "urn:uuid:09178b24-9340-47ec-90b2-1aac03248cd5"
                        }
                    }
                ],
                "participant": [
                    {
                        "individual": {
                            "display": "Dr. Tommy814 Schmeler639",
                            "reference": "urn:uuid:0000016f-57cb-cdac-0000-0000000000dc"
                        }
                    }
                ],
                "period": {
                    "end": "2018-02-17T16:07:39-08:00",
                    "start": "2018-02-17T15:07:39-08:00"
                },
                "serviceProvider": {
                    "display": "BETH ISRAEL DEACONESS HOSPITAL - PLYMOUTH",
                    "reference": "urn:uuid:b1ddf812-1fdd-3adf-b1d5-32cc8bd07ebb"
                },
                "status": "finished",
                "subject": {
                    "display": "Mr. Garland107 Conn188",
                    "reference": "urn:uuid:b1cf5f57-b061-4b7f-aa9d-6283a121694b"
                },
                "type": [
                    {
                        "coding": [
                            {
                                "code": "1234",
                                "display": "Examplotomy Encounter",
                                "system": "http://snomed.info/sct"
                            }
                        ],
                        "text": "Examplotomy Encounter"
                    }
                ],
                "resourceType": "Encounter"
            }
        },
        {
            "fullUrl": "urn:uuid:64620614-f540-46d2-9bdb-af52c8528fdc",
            "request": {
                "method": "POST",
                "url": "Condition"
            },
            "resource": {
                "id": "64620614-f540-46d2-9bdb-af52c8528fdc",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition"
                    ]
                },
                "category": [
                    {
                        "coding": [
                            {
                                "code": "encounter-diagnosis",
                                "display": "Encounter Diagnosis",
                                "system": "http://terminology.hl7.org/CodeSystem/condition-category"
                            }
                        ]
                    }
                ],
                "clinicalStatus": {
                    "coding": [
                        {
                            "code": "active",
                            "system": "http://terminology.hl7.org/CodeSystem/condition-clinical"
                        }
                    ]
                },
                "code": {
                    "coding": [
                        {
                            "code": "1234",
                            "display": "Examplitis",
                            "system": "http://snomed.info/sct"
                        }
                    ],
                    "text": "Examplitis"
                },
                "encounter": {
                    "reference": "urn:uuid:69c19eda-496b-42b2-ae3c-9629ec70b007"
                },
                "onsetDateTime": "2018-02-17T15:07:39-08:00",
                "recordedDate": "2018-02-17T15:07:39-08:00",
                "subject": {
                    "reference": "urn:uuid:b1cf5f57-b061-4b7f-aa9d-6283a121694b"
                },
                "verificationStatus": {
                    "coding": [
                        {
                            "code": "confirmed",
                            "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status"
                        }
                    ]
                },
                "resourceType": "Condition"
            }
        },
        {
            "fullUrl": "urn:uuid:89dcdcc1-9db3-428b-b79b-2897e18641fd",
            "request": {
                "method": "POST",
                "url": "Encounter"
            },
            "resource": {
                "id": "89dcdcc1-9db3-428b-b79b-2897e18641fd",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"
                    ]
                },
                "class": {
                    "code": "EMER",
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode"
                },
                "hospitalization": {
                    "dischargeDisposition": {
                        "coding": [
                            {
                                "code": "1",
                                "display": "Discharge to Home or Self Care (Routine Discharge)",
                                "system": "http://www.nubc.org/patient-discharge"
                            }
                        ],
                        "text": "Discharge to Home or Self Care (Routine Discharge)"
                    }
                },
                "identifier": [
                    {
                        "system": "https://github.com/synthetichealth/synthea",
                        "use": "official",
                        "value": "89dcdcc1-9db3-428b-b79b-2897e18641fd"
                    }
                ],
                "location": [
                    {
                        "location": {
                            "display": "SOUTH SHORE HOSPITAL",
                            "reference": "urn:uuid:76ebe279-211e-493a-8318-4bc784129ac5"
                        }
                    }
                ],
                "participant": [
                    {
                        "individual": {
                            "display": "Dr. Raina861 Willms744",
                            "reference": "urn:uuid:0000016f-57cb-cdac-0000-00000000019a"
                        }
                    }
                ],
                "period": {
                    "end": "2019-07-08T19:47:44-07:00",
                    "start": "2019-07-06T18:47:44-07:00"
                },
                "serviceProvider": {
                    "display": "SOUTH SHORE HOSPITAL",
                    "reference": "urn:uuid:db0acede-4abe-3c01-8d03-5c68a190d8c7"
                },
                "status": "in-progress",
                "subject": {
                    "display": "Ms. Jama227 Corwin846",
                    "reference": "urn:uuid:aad0894e-47f4-4ffc-8fab-8fe5487110d2"
                },
                "type": [
                    {
                        "coding": [
                            {
                                "code": "261665006",
                                "display": "Unknown (qualifier value)",
                                "system": "http://snomed.info/sct"
                            }
                        ],
                        "text": "Unknown (qualifier value)"
                    }
                ],
                "resourceType": "Encounter"
            }
        },
        {
            "fullUrl": "urn:uuid:aad0894e-47f4-4ffc-8fab-8fe5487110d2",
            "request": {
                "method": "POST",
                "url": "Patient"
            },
            "resource": {
                "id": "aad0894e-47f4-4ffc-8fab-8fe5487110d2",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
                    ]
                },
                "extension": [
                    {
                        "extension": [
                            {
                                "url": "ombCategory",
                                "valueCoding": {
                                    "code": "2106-3",
                                    "display": "White",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "text",
                                "valueString": "White"
                            }
                        ],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"
                    },
                    {
                        "extension": [
                            {
                                "url": "ombCategory",
                                "valueCoding": {
                                    "code": "2186-5",
                                    "display": "Not Hispanic or Latino",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "text",
                                "valueString": "Not Hispanic or Latino"
                            }
                        ],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity"
                    },
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName",
                        "valueString": "Becky854 Crist667"
                    },
                    {
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
                        "valueCode": "F"
                    },
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/patient-birthPlace",
                        "valueAddress": {
                            "city": "Boston",
                            "country": "US",
                            "state": "Massachusetts"
                        }
                    },
                    {
                        "url": "http://synthetichealth.github.io/synthea/disability-adjusted-life-years",
                        "valueDecimal": 0.0
                    },
                    {
                        "url": "http://synthetichealth.github.io/synthea/quality-adjusted-life-years",
                        "valueDecimal": 17.0
                    }
                ],
                "text": {
                    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Generated by <a href=\"https://github.com/synthetichealth/synthea\">Synthea</a>.Version identifier: v2.5.0-164-gcf5ad87d\n .   Person seed: -5662576097641999161  Population seed: 1577725971884</div>",
                    "status": "generated"
                },
                "address": [
                    {
                        "extension": [
                            {
                                "extension": [
                                    {
                                        "url": "latitude",
                                        "valueDecimal": 42.23059709875085
                                    },
                                    {
                                        "url": "longitude",
                                        "valueDecimal": -71.04894935227846
                                    }
                                ],
                                "url": "http://hl7.org/fhir/StructureDefinition/geolocation"
                            }
                        ],
                        "city": "Braintree",
                        "country": "US",
                        "line": [
                            "801 Wolf Quay Suite 61"
                        ],
                        "state": "MA"
                    }
                ],
                "birthDate": "2001-06-30",
                "communication": [
                    {
                        "language": {
                            "coding": [
                                {
                                    "code": "en-US",
                                    "display": "English",
                                    "system": "urn:ietf:bcp:47"
                                }
                            ],
                            "text": "English"
                        }
                    }
                ],
                "gender": "female",
                "identifier": [
                    {
                        "system": "https://github.com/synthetichealth/synthea",
                        "value": "aad0894e-47f4-4ffc-8fab-8fe5487110d2"
                    },
                    {
                        "system": "http://hospital.smarthealthit.org",
                        "type": {
                            "coding": [
                                {
                                    "code": "MR",
                                    "display": "Medical Record Number",
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                                }
                            ],
                            "text": "Medical Record Number"
                        },
                        "value": "aad0894e-47f4-4ffc-8fab-8fe5487110d2"
                    },
                    {
                        "system": "http://hl7.org/fhir/sid/us-ssn",
                        "type": {
                            "coding": [
                                {
                                    "code": "SS",
                                    "display": "Social Security Number",
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                                }
                            ],
                            "text": "Social Security Number"
                        },
                        "value": "999-21-5963"
                    },
                    {
                        "system": "urn:oid:2.16.840.1.113883.4.3.25",
                        "type": {
                            "coding": [
                                {
                                    "code": "DL",
                                    "display": "Driver's License",
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                                }
                            ],
                            "text": "Driver's License"
                        },
                        "value": "S99984181"
                    }
                ],
                "maritalStatus": {
                    "coding": [
                        {
                            "code": "S",
                            "display": "Never Married",
                            "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"
                        }
                    ],
                    "text": "Never Married"
                },
                "multipleBirthBoolean": False,
                "name": [
                    {
                        "family": "Corwin846",
                        "given": [
                            "Jama227"
                        ],
                        "prefix": [
                            "Ms."
                        ],
                        "use": "official"
                    }
                ],
                "telecom": [
                    {
                        "system": "phone",
                        "use": "home",
                        "value": "555-442-3071"
                    }
                ],
                "resourceType": "Patient"
            }
        },
        {
            "fullUrl": "urn:uuid:ef0d471c-2b4c-11ea-9734-a4d18ccf5172",
            "request": {
                "method": "POST",
                "url": "Coverage"
            },
            "resource": {
                "id": "ef0d471c-2b4c-11ea-9734-a4d18ccf5172",
                "beneficiary": {
                    "reference": "urn:uuid:aad0894e-47f4-4ffc-8fab-8fe5487110d2"
                },
                "payor": [
                    {
                        "display": "Anthem",
                        "reference": "urn:uuid:ef0d4898-2b4c-11ea-9734-a4d18ccf5172"
                    }
                ],
                "status": "active",
                "subscriberId": "12345",
                "type": {
                    "text": "Anthem"
                },
                "resourceType": "Coverage"
            }
        },
        {
            "fullUrl": "urn:uuid:ef0d4898-2b4c-11ea-9734-a4d18ccf5172",
            "request": {
                "method": "POST",
                "url": "Organization"
            },
            "resource": {
                "id": "ef0d4898-2b4c-11ea-9734-a4d18ccf5172",
                "active": True,
                "address": [
                    {
                        "city": "Indianapolis",
                        "line": [
                            "220 Virginia Ave"
                        ],
                        "postalCode": "46204",
                        "state": "IN"
                    }
                ],
                "identifier": [
                    {
                        "system": "http://hl7.org/fhir/sid/us-npi",
                        "value": "0000010009"
                    }
                ],
                "name": "Anthem",
                "telecom": [
                    {
                        "system": "phone",
                        "use": "work",
                        "value": "1-800-331-1476"
                    }
                ],
                "resourceType": "Organization"
            }
        },
        {
            "fullUrl": "urn:uuid:76ebe279-211e-493a-8318-4bc784129ac5",
            "request": {
                "method": "POST",
                "url": "Location"
            },
            "resource": {
                "id": "76ebe279-211e-493a-8318-4bc784129ac5",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-location"
                    ]
                },
                "address": {
                    "city": "SOUTH WEYMOUTH",
                    "country": "US",
                    "line": [
                        "55 FOGG ROAD"
                    ],
                    "postalCode": "02190",
                    "state": "MA"
                },
                "managingOrganization": {
                    "display": "SOUTH SHORE HOSPITAL",
                    "reference": "urn:uuid:db0acede-4abe-3c01-8d03-5c68a190d8c7"
                },
                "name": "SOUTH SHORE HOSPITAL",
                "position": {
                    "latitude": 42.24158900000001,
                    "longitude": -71.082651
                },
                "status": "active",
                "telecom": [
                    {
                        "system": "phone",
                        "value": "7813408000"
                    }
                ],
                "resourceType": "Location"
            }
        },
        {
            "fullUrl": "urn:uuid:db0acede-4abe-3c01-8d03-5c68a190d8c7",
            "request": {
                "method": "POST",
                "url": "Organization"
            },
            "resource": {
                "id": "db0acede-4abe-3c01-8d03-5c68a190d8c7",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization"
                    ]
                },
                "active": True,
                "address": [
                    {
                        "city": "SOUTH WEYMOUTH",
                        "country": "US",
                        "line": [
                            "55 FOGG ROAD"
                        ],
                        "postalCode": "02190",
                        "state": "MA"
                    }
                ],
                "identifier": [
                    {
                        "system": "https://github.com/synthetichealth/synthea",
                        "value": "db0acede-4abe-3c01-8d03-5c68a190d8c7"
                    }
                ],
                "name": "SOUTH SHORE HOSPITAL",
                "telecom": [
                    {
                        "system": "phone",
                        "value": "7813408000"
                    }
                ],
                "type": [
                    {
                        "coding": [
                            {
                                "code": "prov",
                                "display": "Healthcare Provider",
                                "system": "http://terminology.hl7.org/CodeSystem/organization-type"
                            }
                        ],
                        "text": "Healthcare Provider"
                    }
                ],
                "resourceType": "Organization"
            }
        },
        {
            "fullUrl": "urn:uuid:0000016f-57cb-cdac-0000-00000000019a",
            "request": {
                "method": "POST",
                "url": "Practitioner"
            },
            "resource": {
                "id": "0000016f-57cb-cdac-0000-00000000019a",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner"
                    ]
                },
                "active": True,
                "address": [
                    {
                        "city": "SOUTH WEYMOUTH",
                        "country": "US",
                        "line": [
                            "55 FOGG ROAD"
                        ],
                        "postalCode": "02190",
                        "state": "MA"
                    }
                ],
                "gender": "female",
                "identifier": [
                    {
                        "system": "http://hl7.org/fhir/sid/us-npi",
                        "value": "410"
                    }
                ],
                "name": [
                    {
                        "family": "Willms744",
                        "given": [
                            "Raina861"
                        ],
                        "prefix": [
                            "Dr."
                        ]
                    }
                ],
                "telecom": [
                    {
                        "extension": [
                            {
                                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-direct",
                                "valueBoolean": True
                            }
                        ],
                        "system": "email",
                        "use": "work",
                        "value": "Raina861.Willms744@example.com"
                    }
                ],
                "resourceType": "Practitioner"
            }
        },
        {
            "fullUrl": "urn:uuid:02ba9ec6-0712-4715-8ba4-5485fc571403",
            "request": {
                "method": "POST",
                "url": "Encounter"
            },
            "resource": {
                "id": "02ba9ec6-0712-4715-8ba4-5485fc571403",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"
                    ]
                },
                "class": {
                    "code": "EMER",
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode"
                },
                "identifier": [
                    {
                        "system": "https://github.com/synthetichealth/synthea",
                        "use": "official",
                        "value": "02ba9ec6-0712-4715-8ba4-5485fc571403"
                    }
                ],
                "location": [
                    {
                        "location": {
                            "display": "SOUTH SHORE HOSPITAL",
                            "reference": "urn:uuid:76ebe279-211e-493a-8318-4bc784129ac5"
                        }
                    }
                ],
                "participant": [
                    {
                        "individual": {
                            "display": "Dr. Raina861 Willms744",
                            "reference": "urn:uuid:0000016f-57cb-cdac-0000-00000000019a"
                        }
                    }
                ],
                "period": {
                    "end": "2019-07-06T19:47:44-07:00",
                    "start": "2019-07-06T18:47:44-07:00"
                },
                "serviceProvider": {
                    "display": "SOUTH SHORE HOSPITAL",
                    "reference": "urn:uuid:db0acede-4abe-3c01-8d03-5c68a190d8c7"
                },
                "status": "finished",
                "subject": {
                    "display": "Ms. Jama227 Corwin846",
                    "reference": "urn:uuid:aad0894e-47f4-4ffc-8fab-8fe5487110d2"
                },
                "type": [
                    {
                        "coding": [
                            {
                                "code": "1234",
                                "display": "Examplotomy Encounter",
                                "system": "http://snomed.info/sct"
                            }
                        ],
                        "text": "Examplotomy Encounter"
                    }
                ],
                "resourceType": "Encounter"
            }
        },
        {
            "fullUrl": "urn:uuid:5e83a7b0-6ce9-48c0-aede-81ef3a12b69e",
            "request": {
                "method": "POST",
                "url": "Condition"
            },
            "resource": {
                "id": "5e83a7b0-6ce9-48c0-aede-81ef3a12b69e",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition"
                    ]
                },
                "category": [
                    {
                        "coding": [
                            {
                                "code": "encounter-diagnosis",
                                "display": "Encounter Diagnosis",
                                "system": "http://terminology.hl7.org/CodeSystem/condition-category"
                            }
                        ]
                    }
                ],
                "clinicalStatus": {
                    "coding": [
                        {
                            "code": "active",
                            "system": "http://terminology.hl7.org/CodeSystem/condition-clinical"
                        }
                    ]
                },
                "code": {
                    "coding": [
                        {
                            "code": "1234",
                            "display": "Examplitis",
                            "system": "http://snomed.info/sct"
                        }
                    ],
                    "text": "Examplitis"
                },
                "encounter": {
                    "reference": "urn:uuid:89dcdcc1-9db3-428b-b79b-2897e18641fd"
                },
                "onsetDateTime": "2019-07-06T18:47:44-07:00",
                "recordedDate": "2019-07-06T18:47:44-07:00",
                "subject": {
                    "reference": "urn:uuid:aad0894e-47f4-4ffc-8fab-8fe5487110d2"
                },
                "verificationStatus": {
                    "coding": [
                        {
                            "code": "confirmed",
                            "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status"
                        }
                    ]
                },
                "resourceType": "Condition"
            }
        }
    ],
    "type": "transaction",
    "resourceType": "Bundle"
}

new_bundle = pyfhir(t_bundle)
items = []
for i,entry in enumerate(new_bundle.entry):
    if entry.resource.resource_type is not "Patient":
        #print(i,entry.resource.resource_type)
        items.append(i)
    else:
        entry.resource.extension.pop()
        entry.resource.extension.pop()

for i in reversed(items):
    new_bundle.entry.pop(i)
b_dict = new_bundle.as_json()
#pprint([x['resource']['resourceType'] for x in b_dict['entry']])
print(dumps(b_dict,indent=4))

downloads = Path('/Users/ehaas/Downloads')
p = downloads / 'patients-transaction-bundle.json' 
p.write_text(dumps(b_dict,indent=4))
