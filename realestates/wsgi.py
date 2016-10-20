"""WSGI interface"""

from datetime import date
from json import loads
from traceback import format_exc

from peewee import DoesNotExist

from homeinfo.lib.wsgi import JSON

from his.api.handlers import AuthorizedService

from .errors import NoSuchRealEstate, \
    RealEstatedAdded, CannotAddRealEstate, RealEstateExists, \
    NoRealEstateSpecified, CannotDeleteRealEstate, RealEstateUpdated, \
    RealEstateDeleted


__all__ = ['RealEstates']


class DebugError(JSON):
    """Error for debugging"""

    def __init__(self, msg, status=400):
        dictionary = {
            'msg': msg,
            'stacktrace': format_exc()}
        super().__init__(dictionary, status=status)


class RealEstates(AuthorizedService):
    """Handles requests for ImmoBit"""

    NODE = 'realestates'
    NAME = 'ImmoBit'
    DESCRIPTION = 'Immobiliendatenverwaltung'
    PROMOTE = True

    _stub_real_estate = {
        'objektkategorie': {
            'nutzungsart': {
                'WOHNEN': True,
                'GEWERBE': False},
            'vermarktungsart': {
                'KAUF': False,
                'MIETE_PACHT': True},
            'objektart': {
                'wohnung': [
                    {'wohnungtyp': 'ETAGE'}]}},
        'kontaktperson': {
            'email_direkt': 'foo@bar.com',
            'name': 'Mustermann',
            'vorname': 'Max'},
        'verwaltung_techn': {
            'objektnr_extern': '12fn101-g34',
            'openimmo_obid': 'KM0123456789',
            'stand_vom': str(date.today())}}

    @property
    def filters(self):
        """Returns filters"""
        try:
            filter_str = self.params['filter']
        except KeyError:
            return []
        else:
            return [f for f in filter_str.split(',') if f.strip()]

    def get(self):
        """Returns available real estates"""
        # Stub!
        if self.resource is None:
            dictionary = {
                'immobilie': [self._stub_real_estate]}
            return JSON(dictionary)
        else:
            self._stub_real_estate['verwaltung_techn']['objektnr_extern'] = \
                self.resource
            return JSON(self._stub_real_estate)

    def post(self):
        """Adds new real estates"""
        # XXX: Stub!
        try:
            text = self.data.decode('utf-8')
        except UnicodeDecodeError:
            raise DebugError('Could not decode posted data to unicode.')
        else:
            try:
                dictionary = loads(text)
            except ValueError:
                raise DebugError('Could not create dictionary from text.')
            else:
                return JSON(dictionary)

    def delete(self):
        """Removes real estates"""
        raise NotImplementedError()

    def put(self):
        """Overrides real estates"""
        raise NotImplementedError()

    def patch(self):
        """Partially updates real estates"""
        raise NotImplementedError()

    def options(self):
        """Returns options information"""
        return OK()