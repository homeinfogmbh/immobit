"""Error message definitions"""

from his.api.messages import locales, HISMessage


__all__ = [
    'RealEstatesMessage',
    'IdMismatch',

    'InvalidRealEstateID',
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


@locales('/etc/his.d/locale/immobit.ini')
class RealEstatesMessage(HISMessage):
    """Basic real estates message"""

    pass


class IdMismatch(RealEstatesMessage):
    """Indicates that the IDs of a real estate do not match"""

    STATUS = 400


class InvalidRealEstateID(RealEstatesMessage):
    """Indicates that the provided data is not a valid real estate ID"""

    STATUS = 422


class NoSuchRealEstate(RealEstatesMessage):
    """Indicates that the requested real estate does not exist"""

    STATUS = 404


class RealEstatedCreated(RealEstatesMessage):
    """Indicates that the real estate was successfully created"""

    STATUS = 201


class CannotAddRealEstate(RealEstatesMessage):
    """Indicates that the respective real estate could not be added"""

    STATUS = 500


class RealEstateExists(RealEstatesMessage):
    """Indicates that the respective real estate already exists"""

    STATUS = 409


class NoRealEstateSpecified(RealEstatesMessage):
    """Indicates that no real estate was specified"""

    STATUS = 400


class CannotDeleteRealEstate(RealEstatesMessage):
    """Indicates that the respective real estate could not be deleted"""

    STATUS = 500


class RealEstateUpdated(RealEstatesMessage):
    """Indicates that the real estate has been updated"""

    STATUS = 200


class RealEstateDeleted(RealEstatesMessage):
    """Indicates that the real estate has been deleted"""

    STATUS = 200


class NoAttachmentSpecified(RealEstatesMessage):
    """Indicates that no attachment was specified"""

    STATUS = 400


class NoSuchAttachment(RealEstatesMessage):
    """Indicates that the requested attachment does not exist"""

    STATUS = 404


class AttachmentCreated(RealEstatesMessage):
    """Indicates that the attachment was successfully created"""

    STATUS = 201


class AttachmentDeleted(RealEstatesMessage):
    """Indicates that the attachment has been deleted"""

    STATUS = 200


class NoDataForAttachment(RealEstatesMessage):
    """Indicates that the requested attachment
    does not yet have data stored
    """

    STATUS = 412


class AttachmentExists(RealEstatesMessage):
    """Indicates that the respective attachment already exists"""

    STATUS = 409


class AttachmentLimitExceeded(RealEstatesMessage):
    """Indicates that the limit for attachments has been exceeded"""

    STATUS = 403


class ForeignAttachmentAccess(RealEstatesMessage):
    """Indicates an attempted access of a foreign attachment"""

    STATUS = 403
