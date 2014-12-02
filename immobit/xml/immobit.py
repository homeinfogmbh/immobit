# ./immobit.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ae19f6daa6405a49b67a68d4e4aac013c3185d9e
# Generated 2014-12-02 14:25:23.869629 by PyXB version 1.2.5-DEV using Python 3.4.2.final.0
# Namespace http://xml.homeinfo.de/schema/his/immobit

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:abd39190-7a26-11e4-a610-7427eaa9df7d')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5-DEV'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://xml.homeinfo.de/schema/his/immobit', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://xml.homeinfo.de/schema/his/immobit}DataType
class DataType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                A set of available data transfer types
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 183, 4)
    _Documentation = '\n                A set of available data transfer types\n            '
DataType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DataType, enum_prefix=None)
DataType.IS24CSV = DataType._CF_enumeration.addEnumeration(unicode_value='IS24CSV', tag='IS24CSV')
DataType.OpenImmo = DataType._CF_enumeration.addEnumeration(unicode_value='OpenImmo', tag='OpenImmo')
DataType._InitializeFacetMap(DataType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DataType', DataType)

# Complex type {http://xml.homeinfo.de/schema/his/immobit}ImmoBit with content type ELEMENT_ONLY
class ImmoBit (pyxb.binding.basis.complexTypeDefinition):
    """
                ImmoBit root node type
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ImmoBit')
    _XSDLocation = pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element stats uses Python identifier stats
    __stats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats'), 'stats', '__httpxml_homeinfo_deschemahisimmobit_ImmoBit_stats', True, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 18, 16), )

    
    stats = property(__stats.value, __stats.set, None, None)

    
    # Element realestate uses Python identifier realestate
    __realestate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'realestate'), 'realestate', '__httpxml_homeinfo_deschemahisimmobit_ImmoBit_realestate', True, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 19, 16), )

    
    realestate = property(__realestate.value, __realestate.set, None, None)

    
    # Element openimmo uses Python identifier openimmo
    __openimmo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'openimmo'), 'openimmo', '__httpxml_homeinfo_deschemahisimmobit_ImmoBit_openimmo', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 20, 16), )

    
    openimmo = property(__openimmo.value, __openimmo.set, None, None)

    
    # Element portal uses Python identifier portal
    __portal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'portal'), 'portal', '__httpxml_homeinfo_deschemahisimmobit_ImmoBit_portal', True, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 21, 16), )

    
    portal = property(__portal.value, __portal.set, None, None)

    
    # Element media uses Python identifier media
    __media = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'media'), 'media', '__httpxml_homeinfo_deschemahisimmobit_ImmoBit_media', True, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 22, 16), )

    
    media = property(__media.value, __media.set, None, None)

    _ElementMap.update({
        __stats.name() : __stats,
        __realestate.name() : __realestate,
        __openimmo.name() : __openimmo,
        __portal.name() : __portal,
        __media.name() : __media
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ImmoBit', ImmoBit)


# Complex type {http://xml.homeinfo.de/schema/his/immobit}Stats with content type ELEMENT_ONLY
class Stats (pyxb.binding.basis.complexTypeDefinition):
    """
                An object that contains statistics
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Stats')
    _XSDLocation = pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 29, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpxml_homeinfo_deschemahisimmobit_Stats_id', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 36, 12), )

    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __id.name() : __id
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Stats', Stats)


# Complex type {http://xml.homeinfo.de/schema/his/immobit}RealEstate with content type ELEMENT_ONLY
class RealEstate (pyxb.binding.basis.complexTypeDefinition):
    """
                Brief information about a real estate
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RealEstate')
    _XSDLocation = pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 43, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpxml_homeinfo_deschemahisimmobit_RealEstate_id', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 50, 12), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element thumbnail uses Python identifier thumbnail
    __thumbnail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'thumbnail'), 'thumbnail', '__httpxml_homeinfo_deschemahisimmobit_RealEstate_thumbnail', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 51, 12), )

    
    thumbnail = property(__thumbnail.value, __thumbnail.set, None, None)

    
    # Element city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'city'), 'city', '__httpxml_homeinfo_deschemahisimmobit_RealEstate_city', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 52, 12), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element zip uses Python identifier zip
    __zip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'zip'), 'zip', '__httpxml_homeinfo_deschemahisimmobit_RealEstate_zip', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 53, 12), )

    
    zip = property(__zip.value, __zip.set, None, None)

    
    # Element street uses Python identifier street
    __street = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'street'), 'street', '__httpxml_homeinfo_deschemahisimmobit_RealEstate_street', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 54, 12), )

    
    street = property(__street.value, __street.set, None, None)

    
    # Element house_number uses Python identifier house_number
    __house_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'house_number'), 'house_number', '__httpxml_homeinfo_deschemahisimmobit_RealEstate_house_number', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 55, 12), )

    
    house_number = property(__house_number.value, __house_number.set, None, None)

    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpxml_homeinfo_deschemahisimmobit_RealEstate_type', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 56, 12), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element portal uses Python identifier portal
    __portal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'portal'), 'portal', '__httpxml_homeinfo_deschemahisimmobit_RealEstate_portal', True, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 57, 12), )

    
    portal = property(__portal.value, __portal.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __thumbnail.name() : __thumbnail,
        __city.name() : __city,
        __zip.name() : __zip,
        __street.name() : __street,
        __house_number.name() : __house_number,
        __type.name() : __type,
        __portal.name() : __portal
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RealEstate', RealEstate)


# Complex type {http://xml.homeinfo.de/schema/his/immobit}OpenImmo with content type ELEMENT_ONLY
class OpenImmo (pyxb.binding.basis.complexTypeDefinition):
    """
                A valid OpenImmo document
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OpenImmo')
    _XSDLocation = pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 63, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'OpenImmo', OpenImmo)


# Complex type {http://xml.homeinfo.de/schema/his/immobit}Portal with content type EMPTY
class Portal (pyxb.binding.basis.complexTypeDefinition):
    """
                An abstract portal
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Portal')
    _XSDLocation = pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 77, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Portal', Portal)


# Complex type {http://xml.homeinfo.de/schema/his/immobit}Media with content type EMPTY
class Media (pyxb.binding.basis.complexTypeDefinition):
    """
                Media data
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Media')
    _XSDLocation = pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 128, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Media', Media)


# Complex type {http://xml.homeinfo.de/schema/his/immobit}File with content type ELEMENT_ONLY
class File (pyxb.binding.basis.complexTypeDefinition):
    """
                File data
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'File')
    _XSDLocation = pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 151, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element data uses Python identifier data
    __data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'data'), 'data', '__httpxml_homeinfo_deschemahisimmobit_File_data', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 158, 12), )

    
    data = property(__data.value, __data.set, None, None)

    
    # Element sha256 uses Python identifier sha256
    __sha256 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sha256'), 'sha256', '__httpxml_homeinfo_deschemahisimmobit_File_sha256', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 159, 12), )

    
    sha256 = property(__sha256.value, __sha256.set, None, None)

    
    # Element mime uses Python identifier mime
    __mime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mime'), 'mime', '__httpxml_homeinfo_deschemahisimmobit_File_mime', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 160, 12), )

    
    mime = property(__mime.value, __mime.set, None, None)

    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__httpxml_homeinfo_deschemahisimmobit_File_title', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 161, 12), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element path uses Python identifier path
    __path = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'path'), 'path', '__httpxml_homeinfo_deschemahisimmobit_File_path', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 162, 12), )

    
    path = property(__path.value, __path.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpxml_homeinfo_deschemahisimmobit_File_name', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 163, 12), )

    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __data.name() : __data,
        __sha256.name() : __sha256,
        __mime.name() : __mime,
        __title.name() : __title,
        __path.name() : __path,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'File', File)


# Complex type {http://xml.homeinfo.de/schema/his/immobit}DataTransfer with content type ELEMENT_ONLY
class DataTransfer (pyxb.binding.basis.complexTypeDefinition):
    """
                Data transfer
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataTransfer')
    _XSDLocation = pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 169, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpxml_homeinfo_deschemahisimmobit_DataTransfer_type', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 176, 12), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element data uses Python identifier data
    __data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'data'), 'data', '__httpxml_homeinfo_deschemahisimmobit_DataTransfer_data', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 177, 12), )

    
    data = property(__data.value, __data.set, None, None)

    _ElementMap.update({
        __type.name() : __type,
        __data.name() : __data
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DataTransfer', DataTransfer)


# Complex type {http://xml.homeinfo.de/schema/his/immobit}SearchQuery with content type ELEMENT_ONLY
class SearchQuery (pyxb.binding.basis.complexTypeDefinition):
    """
                A real estate search query
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SearchQuery')
    _XSDLocation = pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 209, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__httpxml_homeinfo_deschemahisimmobit_SearchQuery_category', True, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 216, 12), )

    
    category = property(__category.value, __category.set, None, None)

    
    # Element pattern uses Python identifier pattern
    __pattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pattern'), 'pattern', '__httpxml_homeinfo_deschemahisimmobit_SearchQuery_pattern', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 217, 12), )

    
    pattern = property(__pattern.value, __pattern.set, None, None)

    _ElementMap.update({
        __category.name() : __category,
        __pattern.name() : __pattern
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SearchQuery', SearchQuery)


# Complex type {http://xml.homeinfo.de/schema/his/immobit}FTPPortal with content type ELEMENT_ONLY
class FTPPortal (Portal):
    """
                An FTP portal
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FTPPortal')
    _XSDLocation = pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 87, 4)
    _ElementMap = Portal._ElementMap.copy()
    _AttributeMap = Portal._AttributeMap.copy()
    # Base type is Portal
    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpxml_homeinfo_deschemahisimmobit_FTPPortal_id', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 96, 20), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpxml_homeinfo_deschemahisimmobit_FTPPortal_name', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 97, 20), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element user uses Python identifier user
    __user = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'user'), 'user', '__httpxml_homeinfo_deschemahisimmobit_FTPPortal_user', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 98, 20), )

    
    user = property(__user.value, __user.set, None, None)

    
    # Element password uses Python identifier password
    __password = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'password'), 'password', '__httpxml_homeinfo_deschemahisimmobit_FTPPortal_password', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 99, 20), )

    
    password = property(__password.value, __password.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __name.name() : __name,
        __user.name() : __user,
        __password.name() : __password
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'FTPPortal', FTPPortal)


# Complex type {http://xml.homeinfo.de/schema/his/immobit}RestPortal with content type ELEMENT_ONLY
class RestPortal (Portal):
    """
                A Rest portal
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RestPortal')
    _XSDLocation = pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 107, 4)
    _ElementMap = Portal._ElementMap.copy()
    _AttributeMap = Portal._AttributeMap.copy()
    # Base type is Portal
    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpxml_homeinfo_deschemahisimmobit_RestPortal_id', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 116, 20), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpxml_homeinfo_deschemahisimmobit_RestPortal_name', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 117, 20), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element user uses Python identifier user
    __user = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'user'), 'user', '__httpxml_homeinfo_deschemahisimmobit_RestPortal_user', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 118, 20), )

    
    user = property(__user.value, __user.set, None, None)

    
    # Element access_token uses Python identifier access_token
    __access_token = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'access_token'), 'access_token', '__httpxml_homeinfo_deschemahisimmobit_RestPortal_access_token', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 119, 20), )

    
    access_token = property(__access_token.value, __access_token.set, None, None)

    
    # Element access_token_secret uses Python identifier access_token_secret
    __access_token_secret = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'access_token_secret'), 'access_token_secret', '__httpxml_homeinfo_deschemahisimmobit_RestPortal_access_token_secret', False, pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 120, 20), )

    
    access_token_secret = property(__access_token_secret.value, __access_token_secret.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __name.name() : __name,
        __user.name() : __user,
        __access_token.name() : __access_token,
        __access_token_secret.name() : __access_token_secret
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RestPortal', RestPortal)


# Complex type {http://xml.homeinfo.de/schema/his/immobit}Thumbnail with content type ELEMENT_ONLY
class Thumbnail (File):
    """
                Media thumbnail preview
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Thumbnail')
    _XSDLocation = pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 138, 4)
    _ElementMap = File._ElementMap.copy()
    _AttributeMap = File._AttributeMap.copy()
    # Base type is File
    
    # Element data (data) inherited from {http://xml.homeinfo.de/schema/his/immobit}File
    
    # Element sha256 (sha256) inherited from {http://xml.homeinfo.de/schema/his/immobit}File
    
    # Element mime (mime) inherited from {http://xml.homeinfo.de/schema/his/immobit}File
    
    # Element title (title) inherited from {http://xml.homeinfo.de/schema/his/immobit}File
    
    # Element path (path) inherited from {http://xml.homeinfo.de/schema/his/immobit}File
    
    # Element name (name) inherited from {http://xml.homeinfo.de/schema/his/immobit}File
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Thumbnail', Thumbnail)


immobit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'immobit'), ImmoBit, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 6, 4))
Namespace.addCategoryObject('elementBinding', immobit.name().localName(), immobit)



ImmoBit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats'), Stats, scope=ImmoBit, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 18, 16)))

ImmoBit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'realestate'), RealEstate, scope=ImmoBit, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 19, 16)))

ImmoBit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'openimmo'), OpenImmo, scope=ImmoBit, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 20, 16)))

ImmoBit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'portal'), Portal, scope=ImmoBit, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 21, 16)))

ImmoBit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'media'), Media, scope=ImmoBit, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 22, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 18, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 19, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 21, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 22, 16))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ImmoBit._UseForTag(pyxb.namespace.ExpandedName(None, 'stats')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 18, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ImmoBit._UseForTag(pyxb.namespace.ExpandedName(None, 'realestate')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 19, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ImmoBit._UseForTag(pyxb.namespace.ExpandedName(None, 'openimmo')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 20, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ImmoBit._UseForTag(pyxb.namespace.ExpandedName(None, 'portal')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 21, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ImmoBit._UseForTag(pyxb.namespace.ExpandedName(None, 'media')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 22, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ImmoBit._Automaton = _BuildAutomaton()




Stats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'id'), pyxb.binding.datatypes.integer, scope=Stats, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 36, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 36, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Stats._UseForTag(pyxb.namespace.ExpandedName(None, 'id')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 36, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Stats._Automaton = _BuildAutomaton_()




RealEstate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'id'), pyxb.binding.datatypes.integer, scope=RealEstate, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 50, 12)))

RealEstate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'thumbnail'), Thumbnail, scope=RealEstate, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 51, 12)))

RealEstate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'city'), pyxb.binding.datatypes.string, scope=RealEstate, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 52, 12)))

RealEstate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'zip'), pyxb.binding.datatypes.string, scope=RealEstate, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 53, 12)))

RealEstate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'street'), pyxb.binding.datatypes.string, scope=RealEstate, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 54, 12)))

RealEstate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'house_number'), pyxb.binding.datatypes.string, scope=RealEstate, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 55, 12)))

RealEstate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), pyxb.binding.datatypes.string, scope=RealEstate, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 56, 12)))

RealEstate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'portal'), Portal, scope=RealEstate, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 57, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 57, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RealEstate._UseForTag(pyxb.namespace.ExpandedName(None, 'id')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 50, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RealEstate._UseForTag(pyxb.namespace.ExpandedName(None, 'thumbnail')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 51, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RealEstate._UseForTag(pyxb.namespace.ExpandedName(None, 'city')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 52, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RealEstate._UseForTag(pyxb.namespace.ExpandedName(None, 'zip')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 53, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RealEstate._UseForTag(pyxb.namespace.ExpandedName(None, 'street')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 54, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RealEstate._UseForTag(pyxb.namespace.ExpandedName(None, 'house_number')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 55, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RealEstate._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 56, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RealEstate._UseForTag(pyxb.namespace.ExpandedName(None, 'portal')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 57, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RealEstate._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 70, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OpenImmo._Automaton = _BuildAutomaton_3()




File._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'data'), pyxb.binding.datatypes.base64Binary, scope=File, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 158, 12)))

File._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sha256'), pyxb.binding.datatypes.string, scope=File, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 159, 12)))

File._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mime'), pyxb.binding.datatypes.string, scope=File, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 160, 12)))

File._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'title'), pyxb.binding.datatypes.string, scope=File, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 161, 12)))

File._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'path'), pyxb.binding.datatypes.string, scope=File, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 162, 12)))

File._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=File, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 163, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(File._UseForTag(pyxb.namespace.ExpandedName(None, 'data')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 158, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(File._UseForTag(pyxb.namespace.ExpandedName(None, 'sha256')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 159, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(File._UseForTag(pyxb.namespace.ExpandedName(None, 'mime')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 160, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(File._UseForTag(pyxb.namespace.ExpandedName(None, 'title')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 161, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(File._UseForTag(pyxb.namespace.ExpandedName(None, 'path')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 162, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(File._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 163, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
File._Automaton = _BuildAutomaton_4()




DataTransfer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), DataType, scope=DataTransfer, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 176, 12)))

DataTransfer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'data'), pyxb.binding.datatypes.base64Binary, scope=DataTransfer, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 177, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DataTransfer._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 176, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataTransfer._UseForTag(pyxb.namespace.ExpandedName(None, 'data')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 177, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DataTransfer._Automaton = _BuildAutomaton_5()




SearchQuery._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'category'), pyxb.binding.datatypes.string, scope=SearchQuery, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 216, 12)))

SearchQuery._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pattern'), pyxb.binding.datatypes.string, scope=SearchQuery, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 217, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SearchQuery._UseForTag(pyxb.namespace.ExpandedName(None, 'category')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 216, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SearchQuery._UseForTag(pyxb.namespace.ExpandedName(None, 'pattern')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 217, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SearchQuery._Automaton = _BuildAutomaton_6()




FTPPortal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'id'), pyxb.binding.datatypes.integer, scope=FTPPortal, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 96, 20)))

FTPPortal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=FTPPortal, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 97, 20)))

FTPPortal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'user'), pyxb.binding.datatypes.string, scope=FTPPortal, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 98, 20)))

FTPPortal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'password'), pyxb.binding.datatypes.string, scope=FTPPortal, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 99, 20)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FTPPortal._UseForTag(pyxb.namespace.ExpandedName(None, 'id')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 96, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FTPPortal._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 97, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FTPPortal._UseForTag(pyxb.namespace.ExpandedName(None, 'user')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 98, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FTPPortal._UseForTag(pyxb.namespace.ExpandedName(None, 'password')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 99, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FTPPortal._Automaton = _BuildAutomaton_7()




RestPortal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'id'), pyxb.binding.datatypes.integer, scope=RestPortal, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 116, 20)))

RestPortal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=RestPortal, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 117, 20)))

RestPortal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'user'), pyxb.binding.datatypes.string, scope=RestPortal, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 118, 20)))

RestPortal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'access_token'), pyxb.binding.datatypes.string, scope=RestPortal, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 119, 20)))

RestPortal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'access_token_secret'), pyxb.binding.datatypes.string, scope=RestPortal, location=pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 120, 20)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RestPortal._UseForTag(pyxb.namespace.ExpandedName(None, 'id')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 116, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RestPortal._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 117, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RestPortal._UseForTag(pyxb.namespace.ExpandedName(None, 'user')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 118, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RestPortal._UseForTag(pyxb.namespace.ExpandedName(None, 'access_token')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 119, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RestPortal._UseForTag(pyxb.namespace.ExpandedName(None, 'access_token_secret')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 120, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RestPortal._Automaton = _BuildAutomaton_8()




def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Thumbnail._UseForTag(pyxb.namespace.ExpandedName(None, 'data')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 158, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Thumbnail._UseForTag(pyxb.namespace.ExpandedName(None, 'sha256')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 159, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Thumbnail._UseForTag(pyxb.namespace.ExpandedName(None, 'mime')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 160, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Thumbnail._UseForTag(pyxb.namespace.ExpandedName(None, 'title')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 161, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Thumbnail._UseForTag(pyxb.namespace.ExpandedName(None, 'path')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 162, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Thumbnail._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/rne/Dokumente/Programmierung/python/immobit/doc/immobit.xsd', 163, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Thumbnail._Automaton = _BuildAutomaton_9()

