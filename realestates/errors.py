"""Error message definitions"""

from his.api.locale import Language
from his.api.errors import HISMessage


__all__ = [
    'InvalidJSON',
    'IdMismatch',

    'NoSuchRealEstate',
    'RealEstatedCreated',
    'CannotAddRealEstate',
    'RealEstateExists',
    'NoRealEstateSpecified',
    'CannotDeleteRealEstate',
    'RealEstateUpdated',
    'RealEstateDeleted',

    'NoAttachmentSpecified',
    'AttachmentCreated',
    'NoDataForAttachment',
    'NoSuchAttachment',
    'AttachmentExists',
    'AttachmentLimitExceeded',
    'ForeignAttachmentAccess']


class InvalidJSON(HISMessage):
    """Indicates invalid JSON data"""

    STATUS = 400
    LOCALE = {
        Language.DE_DE: 'Ungültiges JSON-Dokument.',
        Language.EN_US: 'Invalid JSON document.'}


class IdMismatch(HISMessage):
    """Indicates that the IDs of a real estate do not match"""

    STATUS = 400
    LOCALE = {
        Language.DE_DE: 'IDs stimmen nicht überein.',
        Language.EN_US: 'ID mismatch.'}


class NoSuchRealEstate(HISMessage):
    """Indicates that the requested real estate does not exist"""

    STATUS = 404
    LOCALE = {
        Language.DE_DE: 'Keine solche Immobilie.',
        Language.EN_US: 'No such real estate.'}

    def __init__(self, objektnr_extern, charset='utf-8', cors=None):
        data = {'objektnr_extern': objektnr_extern}
        super().__init__(charset=charset, cors=cors, data=data)


class RealEstatedCreated(HISMessage):
    """Indicates that the real estate was successfully created"""

    STATUS = 201
    LOCALE = {
        Language.DE_DE: 'Immobilie erstellt.',
        Language.EN_US: 'Real estate created.'}


class CannotAddRealEstate(HISMessage):
    """Indicates that the respective real estate could not be added"""

    STATUS = 500
    LOCALE = {
        Language.DE_DE: 'Immobilie konnte nicht gespeichert werden.',
        Language.EN_US: 'Could not add real estate.'}


class RealEstateExists(HISMessage):
    """Indicates that the respective real estate already exists"""

    STATUS = 409
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


class NoAttachmentSpecified(HISMessage):
    """Indicates that no attachment was specified"""

    STATUS = 400
    LOCALE = {
        Language.DE_DE: 'Kein Anhang angegeben.',
        Language.EN_US: 'No attachment specified.'}


class NoSuchAttachment(HISMessage):
    """Indicates that the requested attachment does not exist"""

    STATUS = 404
    LOCALE = {
        Language.DE_DE: 'Kein solcher Anhang.',
        Language.EN_US: 'No such attachment.'}


class AttachmentCreated(HISMessage):
    """Indicates that the attachment was successfully created"""

    STATUS = 201
    LOCALE = {
        Language.DE_DE: 'Anhang erstellt.',
        Language.EN_US: 'Attachment created.'}

    def __init__(self, uuid, charset='utf-8', cors=None):
        """Adds the respective SHA-256 sum to the message"""
        super().__init__(charset=charset, cors=cors, data={'uuid': uuid})


class AttachmentDeleted(HISMessage):
    """Indicates that the attachment has been deleted"""

    STATUS = 200
    LOCALE = {
        Language.DE_DE: 'Anhang gelöscht.',
        Language.EN_US: 'Attachment deleted.'}


class NoDataForAttachment(HISMessage):
    """Indicates that the requested attachment
    does not yet have data stored
    """

    STATUS = 412
    LOCALE = {
        Language.DE_DE: 'Keine Daten für Anhang.',
        Language.EN_US: 'No data for attachment.'}


class AttachmentExists(HISMessage):
    """Indicates that the respective attachment already exists"""

    STATUS = 409
    LOCALE = {
        Language.DE_DE: 'Anhang existiert bereits.',
        Language.EN_US: 'Attachment already exists.'}


class AttachmentLimitExceeded(HISMessage):
    """Indicates that the limit for attachments has been exceeded"""

    STATUS = 403
    LOCALE = {
        Language.DE_DE: 'Zu viele Anhänge.',
        Language.EN_US: 'Attachment limit exceeded.'}


class ForeignAttachmentAccess(HISMessage):
    """Indicates an attempted access of a foreign attachment"""

    STATUS = 403
    LOCALE = {
        Language.DE_DE: 'Versuchter Zugriff auf fremden Anhang.',
        Language.EN_US: 'Foreign attachment access.'}
