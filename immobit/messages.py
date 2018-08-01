"""Error message definitions."""

from his import Message


__all__ = [
    'RealEstatesMessage',

    'InvalidRealEstateID',
    'NoSuchRealEstate',
    'RealEstatedCreated',
    'CannotAddRealEstate',
    'RealEstateExists',
    'NoRealEstateSpecified',
    'CannotDeleteRealEstate',
    'NoRealEstateDataProvided',
    'RealEstateUpdated',
    'RealEstateDeleted',

    'NoAttachmentSpecified',
    'AttachmentCreated',
    'NoDataForAttachment',
    'NoSuchAttachment',
    'AttachmentExists',
    'AttachmentLimitExceeded',
    'ForeignAttachmentAccess']


class ImmoBitMessage(Message):
    """Basic real estates message."""

    DOMAIN = 'immobit'


class InvalidRealEstateID(ImmoBitMessage):
    """Indicates that the provided data is not a valid real estate ID."""

    STATUS = 422


class NoSuchRealEstate(ImmoBitMessage):
    """Indicates that the requested real estate does not exist."""

    STATUS = 404


class RealEstatedCreated(ImmoBitMessage):
    """Indicates that the real estate was successfully created."""

    STATUS = 201


class CannotAddRealEstate(ImmoBitMessage):
    """Indicates that the respective real estate could not be added."""

    STATUS = 500


class RealEstateExists(ImmoBitMessage):
    """Indicates that the respective real estate already exists."""

    STATUS = 409


class NoRealEstateSpecified(ImmoBitMessage):
    """Indicates that no real estate was specified."""

    STATUS = 400


class CannotDeleteRealEstate(ImmoBitMessage):
    """Indicates that the respective real estate could not be deleted."""

    STATUS = 500


class NoRealEstateDataProvided(ImmoBitMessage):
    """Indicates that real estate data was expected but not provieded."""

    STATUS = 400


class RealEstateUpdated(ImmoBitMessage):
    """Indicates that the real estate has been updated."""

    STATUS = 200


class RealEstateDeleted(ImmoBitMessage):
    """Indicates that the real estate has been deleted."""

    STATUS = 200


class NoAttachmentSpecified(ImmoBitMessage):
    """Indicates that no attachment was specified."""

    STATUS = 400


class NoSuchAttachment(ImmoBitMessage):
    """Indicates that the requested attachment does not exist."""

    STATUS = 404


class AttachmentCreated(ImmoBitMessage):
    """Indicates that the attachment was successfully created."""

    STATUS = 201


class AttachmentDeleted(ImmoBitMessage):
    """Indicates that the attachment has been deleted."""

    STATUS = 200


class NoDataForAttachment(ImmoBitMessage):
    """Indicates that the requested attachment
    does not yet have data stored.
    """

    STATUS = 412


class AttachmentExists(ImmoBitMessage):
    """Indicates that the respective attachment already exists."""

    STATUS = 409


class AttachmentLimitExceeded(ImmoBitMessage):
    """Indicates that the limit for attachments has been exceeded."""

    STATUS = 403


class ForeignAttachmentAccess(ImmoBitMessage):
    """Indicates an attempted access of a foreign attachment."""

    STATUS = 403
