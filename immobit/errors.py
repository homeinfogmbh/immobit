"""Error message definitions"""

from his.api.locale import Language
from his.api.errors import HISMessage


__all__ = [
    'InvalidOpenimmoData',
    'InvalidDOM',
    'NoSuchRealEstate',
    'RealEstatedAdded',
    'CannotAddRealEstate',
    'RealEstateExists',
    'NoRealEstateSpecified',
    'CannotDeleteRealEstate',
    'RealEstateUpdated',
    'RealEstateDeleted']


class InvalidOpenimmoData(HISMessage):
    """Indicates invalid OpenImmo XML data"""

    STATUS = 400
    LOCALE = {
        Language.DE_DE: 'Ungültige OpenImmo Daten.',
        Language.EN_US: 'Invalid OpenImmo data.'}

    def __init__(self, stacktrace, charset='utf-8', cors=None):
        data = {'stacktrace': stacktrace}
        super().__init__(charset=charset, cors=cors, data=data)


class InvalidDOM(HISMessage):
    """Indicates an invalid DOM"""

    STATUS = 400
    LOCALE = {
        Language.DE_DE: 'Ungültiges Dokument-Objekt-Modell.',
        Language.EN_US: 'Invalid document object model.'}


class NoSuchRealEstate(HISMessage):
    """Indicates that the requested real estate does not exist"""

    STATUS = 400
    LOCALE = {
        Language.DE_DE: 'Keine solche Immobilie.',
        Language.EN_US: 'No such real estate.'}

    def __init__(self, objektnr_extern, charset='utf-8', cors=None):
        data = {'objektnr_extern': objektnr_extern}
        super().__init__(charset=charset, cors=cors, data=data)


class RealEstatedAdded(HISMessage):
    """Indicates that a file was successfully added"""

    STATUS = 200
    LOCALE = {
        Language.DE_DE: 'Immobilie erstellt.',
        Language.EN_US: 'Real estate added.'}


class CannotAddRealEstate(HISMessage):
    """Indicates that the respective real estate could not be added"""

    STATUS = 500
    LOCALE = {
        Language.DE_DE: 'Immobilie konnte nicht gespeichert werden.',
        Language.EN_US: 'Could not add real estate.'}


class RealEstateExists(HISMessage):
    """Indicates that the respective real estate already exists"""

    STATUS = 400
    LOCALE = {
        Language.DE_DE: 'Immobilie existiert bereits.',
        Language.EN_US: 'Real estate already exists.'}


class NoRealEstateSpecified(HISMessage):
    """Indicates that no real estate was specified"""

    STATUS = 400
    LOCALE = {
        Language.DE_DE: 'Keine Immobilie angegeben.',
        Language.EN_US: 'No real estate specified.'}


class CannotDeleteRealEstate(HISMessage):
    """Indicates that the respective real estate could not be deleted"""

    STATUS = 500
    LOCALE = {
        Language.DE_DE: 'Immobilie konnte nicht gelöscht werden.',
        Language.EN_US: 'Could not delete real estate.'}


class RealEstateUpdated(HISMessage):
    """Indicates that the real estate has been updated"""

    STATUS = 200
    LOCALE = {
        Language.DE_DE: 'Immobilie aktualisiert.',
        Language.EN_US: 'Real estate updated.'}


class RealEstateDeleted(HISMessage):
    """Indicates that the real estate has been deleted"""

    STATUS = 200
    LOCALE = {
        Language.DE_DE: 'Immobilie gelöscht.',
        Language.EN_US: 'Real estate deleted.'}
