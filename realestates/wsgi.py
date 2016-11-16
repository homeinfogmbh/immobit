"""WSGI interface"""

from json import loads
from traceback import format_exc

from peewee import DoesNotExist

from openimmodb import OpenImmoDBError, IncompleteDataError, ConsistencyError,\
    RealEstateExists, Transaction, Immobilie
from homeinfo.lib.wsgi import JSON, Error, InternalServerError, OK

from his.api.handlers import AuthorizedService

from .orm import TransactionLog

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

    @property
    def filters(self):
        """Returns filters"""
        try:
            filter_str = self.params['filter']
        except KeyError:
            return []
        else:
            return [f for f in filter_str.split(',') if f.strip()]

    def _add_real_estate(self, dictionary):
        """Adds the real estate represented by the dictionary"""
        try:
            with Transaction(logger=self.logger) as transaction:
                transaction.add(self.customer, dict=dictionary)
        except IncompleteDataError as e:
            raise Error('Incomplete data: {}'.format(
                e.element), status=400) from None
        except RealEstateExists:
            raise Error('Real estate exists', status=400) from None
        except ConsistencyError:
            raise Error('Data inconsistent', status=400) from None
        except OpenImmoDBError:
            raise Error('Unspecified database error:\n{}'.format(
                format_exc())) from None
        else:
            return transaction

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
            raise Error('Posted data is not UTF-8', status=400) from None
        else:
            try:
                dictionary = loads(text)
            except ValueError:
                raise Error(
                    'Invalid JSON:\n{}'.format(text), status=400) from None
            else:
                try:
                    objektnr_extern = dictionary['verwaltung_techn'][
                        'objektnr_extern']
                except (KeyError, TypeError):
                    objektnr_extern = None

                with TransactionLog(
                        account=self.account,
                        objektnr_extern=objektnr_extern,
                        action='CREATE') as log:
                    if self._add_real_estate(dictionary):
                        log.success = True
                        return OK('Real estate added')
                    else:
                        return Error('Could not add real estate', status=500)

    def delete(self):
        """Removes real estates"""
        if self.resource is None:
            raise Error('No real estate specified', status=400) from None
        else:
            # XXX: debug
            self.logger.info('Resource:', self.resource, type(self.resource))
            print(self.environ.get('PATH_INFO'), flush=True)

            try:
                immobilie = Immobilie.fetch(self.customer, self.resource)
            except DoesNotExist:
                raise Error('No such real estate: {}'.format(
                    self.resource), status=400) from None
            else:
                with TransactionLog(
                        account=self.account,
                        objektnr_extern=self.resource,
                        action='DELETE') as log:
                    try:
                        immobilie.remove()
                    except Exception:
                        raise InternalServerError(
                            'Could not delete real estate:\n{}'.format(
                                format_exc())) from None
                    else:
                        log.success = True
                        return OK('Real estate deleted')

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
                with TransactionLog(
                        account=self.account,
                        objektnr_extern=self.resource,
                        action='DELETE') as log:
                    try:
                        immobilie.patch(self.data)
                    except Exception:
                        raise InternalServerError(
                            'Could not patch real estate:\n{}'.format(
                                format_exc())) from None
                    else:
                        log.success = True
                        return OK('Real estate patched')

    def options(self):
        """Returns options information"""
        return OK()
