#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-dce2165f (http://hl7.org/fhir/StructureDefinition/ConditionDefinition) on 2019-06-14.
#  2019, SMART Health IT.


from . import domainresource

class ConditionDefinition(domainresource.DomainResource):
    """ A definition of a condition.
    
    A definition of a condition and information relevant to managing it.
    """
    
    resource_type = "ConditionDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.bodySite = None
        """ Anatomical location, if relevant.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Identification of the condition, problem or diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.definition = None
        """ Formal Definition for the condition.
        List of `str` items. """
        
        self.description = None
        """ Natural language description of the condition definition.
        Type `str`. """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.hasBodySite = None
        """ Whether bodySite is appropriate.
        Type `bool`. """
        
        self.hasSeverity = None
        """ Whether Severity is appropriate.
        Type `bool`. """
        
        self.hasStage = None
        """ Whether stage is appropriate.
        Type `bool`. """
        
        self.identifier = None
        """ Additional identifier for the condition definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for condition definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.medication = None
        """ Medications particularly relevant for this condition.
        List of `ConditionDefinitionMedication` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name for this condition definition (computer friendly).
        Type `str`. """
        
        self.observation = None
        """ Observations particularly relevant to this condition.
        List of `ConditionDefinitionObservation` items (represented as `dict` in JSON). """
        
        self.plan = None
        """ Plan that is appropriate.
        List of `ConditionDefinitionPlan` items (represented as `dict` in JSON). """
        
        self.precondition = None
        """ Observation that suggets this condition.
        List of `ConditionDefinitionPrecondition` items (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.questionnaire = None
        """ Questionnaire for this condition.
        List of `ConditionDefinitionQuestionnaire` items (represented as `dict` in JSON). """
        
        self.severity = None
        """ Subjective severity of condition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.stage = None
        """ Stage/grade, usually assessed formally.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.subtitle = None
        """ Subordinate title of the event definition.
        Type `str`. """
        
        self.team = None
        """ Appropriate team for this condition.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Name for this condition definition (human friendly).
        Type `str`. """
        
        self.url = None
        """ Canonical identifier for this condition definition, represented as
        a URI (globally unique).
        Type `str`. """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the condition definition.
        Type `str`. """
        
        super(ConditionDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConditionDefinition, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("definition", "definition", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("hasBodySite", "hasBodySite", bool, False, None, False),
            ("hasSeverity", "hasSeverity", bool, False, None, False),
            ("hasStage", "hasStage", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("medication", "medication", ConditionDefinitionMedication, True, None, False),
            ("name", "name", str, False, None, False),
            ("observation", "observation", ConditionDefinitionObservation, True, None, False),
            ("plan", "plan", ConditionDefinitionPlan, True, None, False),
            ("precondition", "precondition", ConditionDefinitionPrecondition, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("questionnaire", "questionnaire", ConditionDefinitionQuestionnaire, True, None, False),
            ("severity", "severity", codeableconcept.CodeableConcept, False, None, False),
            ("stage", "stage", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("subtitle", "subtitle", str, False, None, False),
            ("team", "team", fhirreference.FHIRReference, True, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ConditionDefinitionMedication(backboneelement.BackboneElement):
    """ Medications particularly relevant for this condition.
    """
    
    resource_type = "ConditionDefinitionMedication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Category that is relevant.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Code for relevant Medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ConditionDefinitionMedication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConditionDefinitionMedication, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ConditionDefinitionObservation(backboneelement.BackboneElement):
    """ Observations particularly relevant to this condition.
    """
    
    resource_type = "ConditionDefinitionObservation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Category that is relevant.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Code for relevant Observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ConditionDefinitionObservation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConditionDefinitionObservation, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ConditionDefinitionPlan(backboneelement.BackboneElement):
    """ Plan that is appropriate.
    """
    
    resource_type = "ConditionDefinitionPlan"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ The actual plan.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.role = None
        """ Use for the plan.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ConditionDefinitionPlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConditionDefinitionPlan, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ConditionDefinitionPrecondition(backboneelement.BackboneElement):
    """ Observation that suggets this condition.
    
    An observation that suggests that this condition applies.
    """
    
    resource_type = "ConditionDefinitionPrecondition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code for relevant Observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ sensitive | specific.
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ Value of Observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Value of Observation.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(ConditionDefinitionPrecondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConditionDefinitionPrecondition, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("type", "type", str, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
        ])
        return js


class ConditionDefinitionQuestionnaire(backboneelement.BackboneElement):
    """ Questionnaire for this condition.
    """
    
    resource_type = "ConditionDefinitionQuestionnaire"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.purpose = None
        """ preadmit | diff-diagnosis | outcome.
        Type `str`. """
        
        self.reference = None
        """ Specific Questionnaire.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ConditionDefinitionQuestionnaire, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConditionDefinitionQuestionnaire, self).elementProperties()
        js.extend([
            ("purpose", "purpose", str, False, None, True),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import usagecontext
