messageheader={
  "resourceType" : "MessageHeader",
  "id" : "messageheader-01",
  "meta" : {
    "profile" : [
      "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/notifications-messageheader",
      "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/admit-notification-messageheader"
    ]
  },

  "eventCoding" : {
    "system" : "http://hl7.org/fhir/us/davinci-alerts/CodeSystem/notification-event",
    "code" : "notification-admit",
    "display" : "Notification Admit"
  },
  "destination" : [
    {
      "name" : "Acme Message Gateway",
      "endpoint" : "https://example.org/Endpoints/P123"
    }
  ],
  "sender" : {
    "reference" : "urn:uuid:4f7c997a-d6a4-11ea-814c-b5baa7182d44",
    "display" : "Acme Message Sender"
  },
  "author" : {
    "reference" : "urn:uuid:e4b71aed-1c54-4f85-bea0-48444aa31f59",
    "display" : "Ronald Bone"
  },
  "source" : {
    "name" : "Acme Central Patient Registry",
    "software" : "FooBar Patient Manager",
    "version" : "3.1.45.AABB",
    "contact" : {
      "system" : "phone",
      "value" : "+1 (555) 123 4567"
    },
    "endpoint" : "https://example.org/Endpoints/P456"
  },
  "responsible" : {
    "reference" : "urn:uuid:7221aa91-d9e1-44fa-8b90-c5a8c7caeade",
    "display" : "Saint Luke W Endpoint"
  },
  "focus" : [
    {
      "reference" : "urn:uuid:a33d1eed-c4ad-4def-8087-042b7ac0f2b7",
      "display" : "Inpatient Encounter"
    }
  ]
}

sender= {
    "resourceType": "Organization",
    "id": "4f7c997a-d6a4-11ea-814c-b5baa7182d44",
    "identifier": [
        {
            "system": "http://hl7.org/fhir/sid/us-npi",
            "value": "0000010005"
        }
    ],
    "active": True,
    "name": "Acme Message Sender",
    "telecom": [
        {
            "system": "phone",
            "value": "1-800-555-5555",
            "use": "work"
        }
    ],
    "address": [
        {
            "line": [
                "1 Main"
            ],
            "city": "Chicago",
            "state": "IL",
            "postalCode": "60007"
        }
    ]
}

prov_transmit = {
    "id": "provenance",
    "resourceType": "Provenance",
    "meta": {
        "profile": [
            "http://hl7.org/fhir/us/core/StructureDefinition/us-core-provenance"
        ]
    },
    "target": [
        {
            "reference": ""
        }
    ],
    "recorded": '',
    "activity": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/iso-21089-lifecycle",
                "code": "transmit",
                "display": "Transmit",
            }
        ],
        "text": "Forward the message bundle"
    },
    "agent": [
        {
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/provenance-participant-type",
                        "code": "author",
                        "display": "Author"
                    }
                ]
            },
            "who": {
                "reference": "Practitioner/author"
            },
            "onBehalfOf": {
                "reference": "Organization/author-organization"
            }
        },
        {
            "type": {
                "coding": [
                    {
                        "system": "http://hl7.org/fhir/us/core/CodeSystem/us-core-provenance-participant-type",
                        "code": "transmitter",
                        "display": "Transmitter"
                    }
                ]
            },
            "who": {
                "reference": "urn:uuid:4f7c997a-d6a4-11ea-814c-b5baa7182d44"
            }
        }
    ]
}

prov_amend = {
    "id": "provenance",
    "resourceType": "Provenance",
    "meta": {
        "profile": [
            "http://hl7.org/fhir/us/core/StructureDefinition/us-core-provenance"
        ]
    },
    "target": [
        {
            "reference": ""
        }
    ],
    "recorded": '',
    "activity": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/iso-21089-lifecycle",
                "code": "amend",
                "display": "Amend",
            }
        ],
        "text": "Remove Coverage and Forward the Bundle"
    },
    "agent": [
        {
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/provenance-participant-type",
                        "code": "author",
                        "display": "Author"
                    }
                ]
            },
            "who": {
                "reference": "Practitioner/author-"
            },
            "onBehalfOf": {
                "reference": "Organization/author-organization"
            }
        },
        {
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/provenance-participant-type",
                        "code": "assembler",
                        "display": "Assembler"
                    }
                ]
            },
            "who": {
                "reference": "urn:uuid:4f7c997a-d6a4-11ea-814c-b5baa7182d44"
            }
        }
    ]
}
