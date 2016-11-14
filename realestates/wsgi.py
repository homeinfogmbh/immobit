"""WSGI interface"""

from datetime import date
from json import loads
from traceback import format_exc
from tempfile import NamedTemporaryFile

from openimmodb import Immobilie

from homeinfo.lib.wsgi import JSON, OK

from his.api.handlers import AuthorizedService

# from .errors import NoSuchRealEstate, \
#    RealEstatedAdded, CannotAddRealEstate, RealEstateExists, \
#    NoRealEstateSpecified, CannotDeleteRealEstate, RealEstateUpdated, \
#    RealEstateDeleted

__all__ = ['RealEstates']


class DebugError(JSON):
    """Error for debugging"""

    def __init__(self, msg, file=None, status=400):
        dictionary = {
            'msg': msg,
            'stacktrace': format_exc()}

        if file is not None:
            dictionary['file'] = file

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
            real_estates = []

            for immobilie in Immobilie.get(
                    Immobilie._customer == self.customer):
                real_estates.append(immobilie.to_dict())

            return JSON({'immobilie': real_estates})
        else:
            immobilie = Immobilie.fetch(self.customer, self.resource)
            return JSON(immobilie.to_dict())

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
                with NamedTemporaryFile(delete=False) as tmp:
                    tmp.write(text)

                raise DebugError(
                    'Could not create dictionary from text.', file=tmp.name)
            else:
                try:
                    records = list(Immobilie.from_dict(
                        dictionary, customer=self.customer))
                except Exception:
                    self.logger.error('Error while generating records')
                    print(format_exc(), flush=True)
                else:
                    for record in records:
                        try:
                            record.save()
                        except Exception:
                            self.logger.error(
                                'Could not save record: {}'.format(record))
                            print(format_exc(), flush=True)

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
