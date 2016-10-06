"""WSGI interface"""

from traceback import format_exc

from pyxb.exceptions_ import PyXBException
from peewee import DoesNotExist

from homeinfo.crm import Customer
from homeinfo.lib.wsgi import XML

from openimmo import openimmo, factories
from openimmo.openimmo import Umfang

from openimmodb3.orm import Immobilie

from his.api.handlers import AuthorizedService

from .errors import FileTooLarge, InvalidOpenimmoData, InvalidDOM, \
    NoSuchRealEstate, RealEstatedAdded, CannotAddRealEstate, \
    RealEstateExists, NoRealEstateSpecified, CannotDeleteRealEstate, \
    RealEstateUpdated, RealEstateDeleted


__all__ = ['Immobit']


class Immobit(AuthorizedService):
    """Handles requests for ImmoBit"""

    NODE = 'immobit'
    NAME = 'ImmoBit'
    DESCRIPTION = 'Immobiliendatenverwaltung'
    PROMOTE = True

    def _add(self, dom):
        """Adds a new real estate"""
        try:
            ident = Immobilie.add(self.customer, dom)
        except Exception:
            self.logger.error(format_exc())
            raise CannotAddRealEstate() from None
        else:
            if ident:
                return RealEstatedAdded()
            else:
                raise CannotAddRealEstate() from None

    def _anbieter(self):
        """Returns all real estates for the respective customer"""
        anbieter = factories.anbieter(repr(self.customer), str(self.customer))

        for immobilie in Immobilie.by_cid(self.customer):
            anbieter.immobilie.append(immobilie.dom)

        return XML(anbieter)

    def _immobilie(self, objektnr_extern):
        """Returns the respective real estate of the respective customer"""
        try:
            immobilie = Immobilie.get(
                (Immobilie.customer == self.customer) &
                (Immobilie.objektnr_extern == objektnr_extern))
        except DoesNotExist:
            raise NoSuchRealEstate(objektnr_extern) from None
        else:
            return XML(immobilie)

    def _update(self, immobilie, dom):
        """Updates the respective real estate"""
        immobilie.openimmo_obid = dom.openimmo_obid
        immobilie.objektnr_intern = dom.immobilie.objektnr_intern
        immobilie.objektnr_extern = dom.immobilie.objektnr_extern
        immobilie.data = dom.toxml(encoding='utf-8')  # New!
        immobilie.save()
        return RealEstateUpdated()

    def _delete(self, objektnr_extern):
        """Deletes the respective real estate"""
        try:
            immobilie = Immobilie.get(
                (Immobilie.customer == self.customer) &
                (Immobilie.objektnr_extern == self.resource))
        except DoesNotExist:
            raise NoSuchRealEstate(self.resource) from None
        else:
            try:
                result = immobilie.remove(portals=True)
            except Exception:
                result = False

            if result:
                return RealEstateDeleted()
            else:
                raise CannotDeleteRealEstate() from None

    @property
    def filters(self):
        """Returns filters"""
        try:
            filter_str = self.query_dict['filter']
        except KeyError:
            return []
        else:
            return [f for f in filter_str.split(',') if f]

    @property
    def dom(self):
        """Returns the posted openimmo-compliant DOM"""
        try:
            data = self.file.read()
        except MemoryError:
            raise FileTooLarge() from None
        else:
            try:
                return openimmo.CreateFromDocument(data)
            except PyXBException:
                raise InvalidOpenimmoData(format_exc()) from None

    def post(self):
        """Posts real estate data"""
        dom = self.dom

        # Verify DOM as openimmo.immobilie
        if isinstance(dom, openimmo.immobilie().__class__):
            try:
                Immobilie.get(Immobilie.objektnr_extern == dom.objektnr_extern)
            except DoesNotExist:
                return self._add(dom)
            else:
                raise RealEstateExists()
        else:
            raise InvalidDOM()

    def get(self):
        """Handles GET requests"""
        if self.resource is None:
            return self._anbieter()
        else:
            return self._immobilie(self.resource)

    def put(self):
        """Updates real estates"""
        if self.resource is None:
            raise NoRealEstateSpecified()
        else:
            try:
                immobilie = Immobilie.get(
                    (Immobilie.customer == self.customer) &
                    (Immobilie.objektnr_extern == self.resource))
            except DoesNotExist:
                raise NoSuchRealEstate(self.resource) from None
            else:
                dom = self.dom

                if isinstance(dom, openimmo.immobilie().__class__):
                    return self._update(immobilie, dom)
                else:
                    raise InvalidDOM()

    def delete(self):
        """Removes real estates"""
        if self.resource is None:
            raise NoRealEstateSpecified()
        else:
            return self._delete(self.resource)
