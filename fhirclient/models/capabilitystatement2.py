#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-dce2165f (http://hl7.org/fhir/StructureDefinition/CapabilityStatement2) on 2019-06-14.
#  2019, SMART Health IT.


from . import domainresource

class CapabilityStatement2(domainresource.DomainResource):
    """ A statement of system capabilities.
    
    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server for a particular version of FHIR that may be used as a
    statement of actual server functionality or a statement of required or
    desired server implementation.
    """
    
    resource_type = "CapabilityStatement2"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the capability statement2.
        Type `str`. """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.fhirVersion = None
        """ FHIR Version the system supports.
        Type `str`. """
        
        self.format = None
        """ formats supported (xml | json | ttl | mime type).
        List of `str` items. """
        
        self.implementation = None
        """ If this describes a specific instance.
        Type `CapabilityStatement2Implementation` (represented as `dict` in JSON). """
        
        self.implementationGuide = None
        """ Implementation guides supported.
        List of `str` items. """
        
        self.imports = None
        """ Canonical URL of another capability statement this adds to.
        List of `str` items. """
        
        self.instantiates = None
        """ Canonical URL of another capability statement this implements.
        List of `str` items. """
        
        self.jurisdiction = None
        """ Intended jurisdiction for capability statement2 (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.kind = None
        """ instance | capability | requirements.
        Type `str`. """
        
        self.name = None
        """ Name for this capability statement2 (computer friendly).
        Type `str`. """
        
        self.patchFormat = None
        """ Patch formats supported.
        List of `str` items. """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ Why this capability statement2 is defined.
        Type `str`. """
        
        self.rest = None
        """ If the endpoint is a RESTful one.
        List of `CapabilityStatement2Rest` items (represented as `dict` in JSON). """
        
        self.software = None
        """ Software that is covered by this capability statement.
        Type `CapabilityStatement2Software` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.title = None
        """ Name for this capability statement2 (human friendly).
        Type `str`. """
        
        self.url = None
        """ Canonical identifier for this capability statement2, represented as
        a URI (globally unique).
        Type `str`. """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the capability statement2.
        Type `str`. """
        
        super(CapabilityStatement2, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatement2, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, True),
            ("format", "format", str, True, None, True),
            ("implementation", "implementation", CapabilityStatement2Implementation, False, None, False),
            ("implementationGuide", "implementationGuide", str, True, None, False),
            ("imports", "imports", str, True, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("patchFormat", "patchFormat", str, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("rest", "rest", CapabilityStatement2Rest, True, None, False),
            ("software", "software", CapabilityStatement2Software, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class CapabilityStatement2Implementation(backboneelement.BackboneElement):
    """ If this describes a specific instance.
    
    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """
    
    resource_type = "CapabilityStatement2Implementation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.custodian = None
        """ Organization that manages the data.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.description = None
        """ Describes this specific instance.
        Type `str`. """
        
        self.url = None
        """ Base URL for the installation.
        Type `str`. """
        
        super(CapabilityStatement2Implementation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatement2Implementation, self).elementProperties()
        js.extend([
            ("custodian", "custodian", fhirreference.FHIRReference, False, None, False),
            ("description", "description", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


class CapabilityStatement2Rest(backboneelement.BackboneElement):
    """ If the endpoint is a RESTful one.
    
    A definition of the restful capabilities of the solution, if any.
    """
    
    resource_type = "CapabilityStatement2Rest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compartment = None
        """ Compartments served/used by system.
        List of `str` items. """
        
        self.documentation = None
        """ General description of implementation.
        Type `str`. """
        
        self.interaction = None
        """ What operations are supported?.
        List of `CapabilityStatement2RestInteraction` items (represented as `dict` in JSON). """
        
        self.mode = None
        """ client | server.
        Type `str`. """
        
        self.operation = None
        """ Definition of a system level operation.
        List of `CapabilityStatement2RestResourceOperation` items (represented as `dict` in JSON). """
        
        self.resource = None
        """ Resource served on the REST interface.
        List of `CapabilityStatement2RestResource` items (represented as `dict` in JSON). """
        
        self.searchParam = None
        """ Search parameters for searching all resources.
        List of `CapabilityStatement2RestResourceSearchParam` items (represented as `dict` in JSON). """
        
        super(CapabilityStatement2Rest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatement2Rest, self).elementProperties()
        js.extend([
            ("compartment", "compartment", str, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("interaction", "interaction", CapabilityStatement2RestInteraction, True, None, False),
            ("mode", "mode", str, False, None, True),
            ("operation", "operation", CapabilityStatement2RestResourceOperation, True, None, False),
            ("resource", "resource", CapabilityStatement2RestResource, True, None, False),
            ("searchParam", "searchParam", CapabilityStatement2RestResourceSearchParam, True, None, False),
        ])
        return js


class CapabilityStatement2RestInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.
    
    A specification of restful operations supported by the system.
    """
    
    resource_type = "CapabilityStatement2RestInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ transaction | batch | search-system | history-system.
        Type `str`. """
        
        self.documentation = None
        """ Anything special about operation behavior.
        Type `str`. """
        
        super(CapabilityStatement2RestInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatement2RestInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


class CapabilityStatement2RestResource(backboneelement.BackboneElement):
    """ Resource served on the REST interface.
    
    A specification of the restful capabilities of the solution for a specific
    resource type.
    """
    
    resource_type = "CapabilityStatement2RestResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ Additional information about the use of the resource type.
        Type `str`. """
        
        self.interaction = None
        """ What operations are supported?.
        List of `CapabilityStatement2RestResourceInteraction` items (represented as `dict` in JSON). """
        
        self.operation = None
        """ Definition of a resource operation.
        List of `CapabilityStatement2RestResourceOperation` items (represented as `dict` in JSON). """
        
        self.profile = None
        """ Base System profile for all uses of resource.
        Type `str`. """
        
        self.searchParam = None
        """ Search parameters supported by implementation.
        List of `CapabilityStatement2RestResourceSearchParam` items (represented as `dict` in JSON). """
        
        self.supportedProfile = None
        """ Profiles for use cases supported.
        List of `str` items. """
        
        self.type = None
        """ A resource type that is supported.
        Type `str`. """
        
        super(CapabilityStatement2RestResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatement2RestResource, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("interaction", "interaction", CapabilityStatement2RestResourceInteraction, True, None, False),
            ("operation", "operation", CapabilityStatement2RestResourceOperation, True, None, False),
            ("profile", "profile", str, False, None, False),
            ("searchParam", "searchParam", CapabilityStatement2RestResourceSearchParam, True, None, False),
            ("supportedProfile", "supportedProfile", str, True, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class CapabilityStatement2RestResourceInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.
    
    Identifies a restful operation supported by the solution.
    """
    
    resource_type = "CapabilityStatement2RestResourceInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ read | vread | update | patch | delete | history-instance |
        history-type | create | search-type.
        Type `str`. """
        
        self.documentation = None
        """ Anything special about operation behavior.
        Type `str`. """
        
        super(CapabilityStatement2RestResourceInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatement2RestResourceInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


class CapabilityStatement2RestResourceOperation(backboneelement.BackboneElement):
    """ Definition of a resource operation.
    
    Definition of an operation or a named query together with its parameters
    and their meaning and type. Consult the definition of the operation for
    details about how to invoke the operation, and the parameters.
    """
    
    resource_type = "CapabilityStatement2RestResourceOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ The defined operation/query.
        Type `str`. """
        
        self.documentation = None
        """ Specific details about operation behavior.
        Type `str`. """
        
        self.name = None
        """ Name by which the operation/query is invoked.
        Type `str`. """
        
        super(CapabilityStatement2RestResourceOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatement2RestResourceOperation, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
            ("name", "name", str, False, None, True),
        ])
        return js


class CapabilityStatement2RestResourceSearchParam(backboneelement.BackboneElement):
    """ Search parameters supported by implementation.
    
    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """
    
    resource_type = "CapabilityStatement2RestResourceSearchParam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ Source of definition for parameter.
        Type `str`. """
        
        self.documentation = None
        """ Server-specific usage.
        Type `str`. """
        
        self.name = None
        """ Name of search parameter.
        Type `str`. """
        
        self.type = None
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `str`. """
        
        super(CapabilityStatement2RestResourceSearchParam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatement2RestResourceSearchParam, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


class CapabilityStatement2Software(backboneelement.BackboneElement):
    """ Software that is covered by this capability statement.
    
    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """
    
    resource_type = "CapabilityStatement2Software"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ A name the software is known by.
        Type `str`. """
        
        self.releaseDate = None
        """ Date this version was released.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.version = None
        """ Version covered by this statement.
        Type `str`. """
        
        super(CapabilityStatement2Software, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatement2Software, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("releaseDate", "releaseDate", fhirdate.FHIRDate, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext
