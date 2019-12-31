#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-dce2165f on 2019-06-14.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import catalogentry
from .fhirdate import FHIRDate


class CatalogEntryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CatalogEntry", js["resourceType"])
        return catalogentry.CatalogEntry(js)
    
    def testCatalogEntry1(self):
        inst = self.instantiate_from("catalogentry-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CatalogEntry instance")
        self.implCatalogEntry1(inst)
        
        js = inst.as_json()
        self.assertEqual("CatalogEntry", js["resourceType"])
        inst2 = catalogentry.CatalogEntry(js)
        self.implCatalogEntry1(inst2)
    
    def implCatalogEntry1(self, inst):
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2018-12-16").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2018-12-16")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://example.com/identifier")
        self.assertEqual(inst.identifier[0].value, "456")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Serum electrolyte panel")
        self.assertEqual(inst.note[0].authorString, "Adam Man")
        self.assertEqual(inst.note[0].text, "created as an example")
        self.assertTrue(inst.orderable)
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"> </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "ActivityDefinition")

