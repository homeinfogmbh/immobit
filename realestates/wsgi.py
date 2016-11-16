"""WSGI interface"""

from datetime import date
from json import loads
from traceback import format_exc

from peewee import DoesNotExist

from openimmodb import Transaction, Immobilie
from homeinfo.lib.wsgi import JSON, Error, InternalServerError, OK

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

            for immobilie in Immobilie.select().where(
                    Immobilie._customer == self.customer):
                real_estates.append(immobilie.to_dict())

            return JSON({'immobilie': real_estates})
        else:
            try:
                immobilie = Immobilie.fetch(self.customer, self.resource)
            except DoesNotExist:
                raise Error('No such real estate: {}'.format(
                    self.resource), status=400) from None
            else:
                try:
                    return JSON(immobilie.to_dict())
                except Exception:
                    raise InternalServerError(format_exc()) from None

    def post(self):
        """Adds new real estates"""
        try:
            text = self.data.decode('utf-8')
        except UnicodeDecodeError:
            raise DebugError('Could not decode posted data to unicode.')
        else:
            # XXX: Debug
            self.logger.info('Received Text:')
            print(text, flush=True)

            try:
                dictionary = loads(text)
            except ValueError:
                raise Error('Could not create dictionary from text')
            else:
                with Transaction() as transaction:
                    transaction.add(self.customer, dict=dictionary)

                if transaction:
                    return OK('Transaction succeeded')
                else:
                    return Error('Transaction failed:\n{}'.format(
                        transaction.traceback.print_tb()), status=400)

    def delete(self):
        """Removes real estates"""
        if self.resource is None:
            raise Error('No real estate specified', status=400) from None
        else:
            try:
                immobilie = Immobilie.fetch(self.customer, self.resource)
            except DoesNotExist:
                raise Error('No such real estate: {}'.format(
                    self.resource), status=400) from None
            else:
                try:
                    immobilie.remove()
                except Exception:
                    raise InternalServerError(
                        'Could not delete real estate:\n{}'.format(
                            format_exc())) from None

    def put(self):
        """Overrides real estates"""
        return self.patch()

    def patch(self):
        """Partially updates real estates"""
        if self.resource is None:
            raise Error('No real estate specified', status=400) from None
        else:
            try:
                immobilie = Immobilie.fetch(self.customer, self.resource)
            except DoesNotExist:
                raise Error('No such real estate: {}'.format(
                    self.resource), status=400) from None
            else:
                try:
                    immobilie.patch(self.data)
                except Exception:
                    raise InternalServerError(
                        'Could not patch real estate:\n{}'.format(
                            format_exc())) from None

    def options(self):
        """Returns options information"""
        return OK()
