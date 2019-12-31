#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-dce2165f on 2019-06-14.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import conditiondefinition
from .fhirdate import FHIRDate


class ConditionDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ConditionDefinition", js["resourceType"])
        return conditiondefinition.ConditionDefinition(js)
    
    def testConditionDefinition1(self):
        inst = self.instantiate_from("conditiondefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConditionDefinition instance")
        self.implConditionDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ConditionDefinition", js["resourceType"])
        inst2 = conditiondefinition.ConditionDefinition(js)
        self.implConditionDefinition1(inst2)
    
    def implConditionDefinition1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "55822004")
        self.assertEqual(inst.code.coding[0].display, "Hyperlipidemia (disorder)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.date.date, FHIRDate("2019-05-26T10:44:00+10:00").date)
        self.assertEqual(inst.date.as_json(), "2019-05-26T10:44:00+10:00")
        self.assertEqual(inst.definition[0], "https://med.stanford.edu/content/dam/sm/cerc/documents/Hyperlipidemia%20Management%20Protocol.pdf")
        self.assertFalse(inst.hasBodySite)
        self.assertFalse(inst.hasSeverity)
        self.assertFalse(inst.hasStage)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.medication[0].code.coding[0].code, "203151")
        self.assertEqual(inst.medication[0].code.coding[0].display, "Gemfibrozil")
        self.assertEqual(inst.medication[0].code.coding[0].system, "http://www.nlm.nih.gov/research/umls/rxnorm")
        self.assertEqual(inst.name, "Hyperlipidemia")
        self.assertEqual(inst.observation[0].code.coding[0].code, "24331-1")
        self.assertEqual(inst.observation[0].code.coding[0].display, "Lipid 1996 panel - Serum or Plasma")
        self.assertEqual(inst.observation[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.observation[0].code.text, "Lipid Panel")
        self.assertEqual(inst.observation[1].code.coding[0].code, "35200-5")
        self.assertEqual(inst.observation[1].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.observation[1].code.text, "Cholesterol")
        self.assertEqual(inst.observation[2].code.coding[0].code, "35217-9")
        self.assertEqual(inst.observation[2].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.observation[2].code.text, "Triglyceride")
        self.assertEqual(inst.observation[3].code.coding[0].code, "2085-9")
        self.assertEqual(inst.observation[3].code.coding[0].display, "HDL Cholesterol")
        self.assertEqual(inst.observation[3].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.observation[3].code.text, "Cholesterol in HDL")
        self.assertEqual(inst.observation[4].code.coding[0].code, "13457-7")
        self.assertEqual(inst.observation[4].code.coding[0].display, "Cholesterol in LDL [Mass/volume] in Serum or Plasma by calculation")
        self.assertEqual(inst.observation[4].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.observation[4].code.text, "LDL Chol. (Calc)")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Hyperlipidemia Status")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ConditionDefinition/example")

