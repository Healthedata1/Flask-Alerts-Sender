#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-dce2165f (http://hl7.org/fhir/StructureDefinition/ClinicalUseIssue) on 2019-06-14.
#  2019, SMART Health IT.


from . import domainresource

class ClinicalUseIssue(domainresource.DomainResource):
    """ ClinicalUseIssue.
    
    A single item of clinical particulars - an indication, contraindication,
    interaction etc. for a medicinal product.
    """
    
    resource_type = "ClinicalUseIssue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contraindication = None
        """ Specifics for when this is a contraindication.
        Type `ClinicalUseIssueContraindication` (represented as `dict` in JSON). """
        
        self.description = None
        """ General description.
        Type `str`. """
        
        self.indication = None
        """ Specifics for when this is an indication.
        Type `ClinicalUseIssueIndication` (represented as `dict` in JSON). """
        
        self.interaction = None
        """ Specifics for when this is an interaction.
        Type `ClinicalUseIssueInteraction` (represented as `dict` in JSON). """
        
        self.population = None
        """ The population group to which this applies.
        List of `Population` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ The medication or procedure for which this is an indication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type = None
        """ indication | contraindication | interaction | undesirable-effect |
        other.
        Type `str`. """
        
        self.undesirableEffect = None
        """ UndesirableEffect.
        Type `ClinicalUseIssueUndesirableEffect` (represented as `dict` in JSON). """
        
        super(ClinicalUseIssue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalUseIssue, self).elementProperties()
        js.extend([
            ("contraindication", "contraindication", ClinicalUseIssueContraindication, False, None, False),
            ("description", "description", str, False, None, False),
            ("indication", "indication", ClinicalUseIssueIndication, False, None, False),
            ("interaction", "interaction", ClinicalUseIssueInteraction, False, None, False),
            ("population", "population", population.Population, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("type", "type", str, False, None, True),
            ("undesirableEffect", "undesirableEffect", ClinicalUseIssueUndesirableEffect, False, None, False),
        ])
        return js


from . import backboneelement

class ClinicalUseIssueContraindication(backboneelement.BackboneElement):
    """ Specifics for when this is a contraindication.
    """
    
    resource_type = "ClinicalUseIssueContraindication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comorbidity = None
        """ A comorbidity (concurrent condition) or coinfection.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.diseaseStatus = None
        """ The status of the disease or symptom for the contraindication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diseaseSymptomProcedure = None
        """ The disease, symptom or procedure for the contraindication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.indication = None
        """ The indication which this is a contraidication for.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.otherTherapy = None
        """ Information about the use of the medicinal product in relation to
        other therapies described as part of the indication.
        List of `ClinicalUseIssueContraindicationOtherTherapy` items (represented as `dict` in JSON). """
        
        super(ClinicalUseIssueContraindication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalUseIssueContraindication, self).elementProperties()
        js.extend([
            ("comorbidity", "comorbidity", codeableconcept.CodeableConcept, True, None, False),
            ("diseaseStatus", "diseaseStatus", codeableconcept.CodeableConcept, False, None, False),
            ("diseaseSymptomProcedure", "diseaseSymptomProcedure", codeableconcept.CodeableConcept, False, None, False),
            ("indication", "indication", fhirreference.FHIRReference, True, None, False),
            ("otherTherapy", "otherTherapy", ClinicalUseIssueContraindicationOtherTherapy, True, None, False),
        ])
        return js


class ClinicalUseIssueContraindicationOtherTherapy(backboneelement.BackboneElement):
    """ Information about the use of the medicinal product in relation to other
    therapies described as part of the indication.
    """
    
    resource_type = "ClinicalUseIssueContraindicationOtherTherapy"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.medicationCodeableConcept = None
        """ Reference to a specific medication (active substance, medicinal
        product or class of products) as part of an indication or
        contraindication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ Reference to a specific medication (active substance, medicinal
        product or class of products) as part of an indication or
        contraindication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.therapyRelationshipType = None
        """ The type of relationship between the medicinal product indication
        or contraindication and another therapy.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClinicalUseIssueContraindicationOtherTherapy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalUseIssueContraindicationOtherTherapy, self).elementProperties()
        js.extend([
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("therapyRelationshipType", "therapyRelationshipType", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ClinicalUseIssueIndication(backboneelement.BackboneElement):
    """ Specifics for when this is an indication.
    """
    
    resource_type = "ClinicalUseIssueIndication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comorbidity = None
        """ A comorbidity (concurrent condition) or coinfection as part of the
        indication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.diseaseStatus = None
        """ The status of the disease or symptom for the indication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diseaseSymptomProcedure = None
        """ The disease, symptom or procedure for the indication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.duration = None
        """ For an indication - timing or duration information.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.intendedEffect = None
        """ For an indication - the intended effect, aim or strategy to be
        achieved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.otherTherapy = None
        """ Information about the use of the medicinal product in relation to
        other therapies described as part of the contraindication.
        List of `ClinicalUseIssueContraindicationOtherTherapy` items (represented as `dict` in JSON). """
        
        self.undesirableEffect = None
        """ For an indicaton - the specific undesirable effects of the
        medicinal product.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ClinicalUseIssueIndication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalUseIssueIndication, self).elementProperties()
        js.extend([
            ("comorbidity", "comorbidity", codeableconcept.CodeableConcept, True, None, False),
            ("diseaseStatus", "diseaseStatus", codeableconcept.CodeableConcept, False, None, False),
            ("diseaseSymptomProcedure", "diseaseSymptomProcedure", codeableconcept.CodeableConcept, False, None, False),
            ("duration", "duration", quantity.Quantity, False, None, False),
            ("intendedEffect", "intendedEffect", codeableconcept.CodeableConcept, False, None, False),
            ("otherTherapy", "otherTherapy", ClinicalUseIssueContraindicationOtherTherapy, True, None, False),
            ("undesirableEffect", "undesirableEffect", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class ClinicalUseIssueInteraction(backboneelement.BackboneElement):
    """ Specifics for when this is an interaction.
    """
    
    resource_type = "ClinicalUseIssueInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.effect = None
        """ The effect of the interaction, for example "reduced gastric
        absorption of primary medication".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.incidence = None
        """ The incidence of the interaction, e.g. theoretical, observed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.interactant = None
        """ The specific medication, food or laboratory test that interacts.
        List of `ClinicalUseIssueInteractionInteractant` items (represented as `dict` in JSON). """
        
        self.management = None
        """ Actions for managing the interaction.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ The type of the interaction e.g. drug-drug interaction, drug-food
        interaction, drug-lab test interaction.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClinicalUseIssueInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalUseIssueInteraction, self).elementProperties()
        js.extend([
            ("effect", "effect", codeableconcept.CodeableConcept, False, None, False),
            ("incidence", "incidence", codeableconcept.CodeableConcept, False, None, False),
            ("interactant", "interactant", ClinicalUseIssueInteractionInteractant, True, None, False),
            ("management", "management", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ClinicalUseIssueInteractionInteractant(backboneelement.BackboneElement):
    """ The specific medication, food or laboratory test that interacts.
    """
    
    resource_type = "ClinicalUseIssueInteractionInteractant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.itemCodeableConcept = None
        """ The specific medication, food or laboratory test that interacts.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.itemReference = None
        """ The specific medication, food or laboratory test that interacts.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ClinicalUseIssueInteractionInteractant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalUseIssueInteractionInteractant, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
        ])
        return js


class ClinicalUseIssueUndesirableEffect(backboneelement.BackboneElement):
    """ UndesirableEffect.
    
    Describe the undesirable effects of the medicinal product.
    """
    
    resource_type = "ClinicalUseIssueUndesirableEffect"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.classification = None
        """ Classification of the effect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.frequencyOfOccurrence = None
        """ The frequency of occurrence of the effect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.symptomConditionEffect = None
        """ The symptom, condition or undesirable effect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClinicalUseIssueUndesirableEffect, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalUseIssueUndesirableEffect, self).elementProperties()
        js.extend([
            ("classification", "classification", codeableconcept.CodeableConcept, False, None, False),
            ("frequencyOfOccurrence", "frequencyOfOccurrence", codeableconcept.CodeableConcept, False, None, False),
            ("symptomConditionEffect", "symptomConditionEffect", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import population
from . import quantity
