"""Error message definitions."""

from his import HIS_MESSAGE_FACILITY


__all__ = [
    'INVALID_REAL_ESTATE_ID',
    'NO_SUCH_REAL_ESTATE',
    'REAL_ESTATE_CREATED',
    'CANNOT_ADD_REAL_ESTATE',
    'REAL_ESTATE_EXISTS',
    'CANNOT_DELETE_REAL_ESTATE',
    'REAL_ESTATE_UPDATED',
    'REAL_ESTATE_DELETED',
    'NO_SUCH_ATTACHMENT',
    'ATTACHMENT_CREATED',
    'ATTACHMENT_DELETED',
    'ATTACHMENT_EXISTS',
    'ATTACHMENT_LIMIT_EXCEEDED']


IMMOBIT_MESSAGE_DOMAIN = HIS_MESSAGE_FACILITY.domain('immobit')
IMMOBIT_MESSAGE = IMMOBIT_MESSAGE_DOMAIN.message
INVALID_REAL_ESTATE_ID = IMMOBIT_MESSAGE('Invalid real estate ID.', status=422)
NO_SUCH_REAL_ESTATE = IMMOBIT_MESSAGE(
    'The requested real estate does not exist.', status=404)
REAL_ESTATE_CREATED = IMMOBIT_MESSAGE(
    'The real estate has been created.', status=201)
CANNOT_ADD_REAL_ESTATE = IMMOBIT_MESSAGE(
    'Could not add the real estate.', status=500)
REAL_ESTATE_EXISTS = IMMOBIT_MESSAGE(
    'The real estate already exists.', status=409)
CANNOT_DELETE_REAL_ESTATE = IMMOBIT_MESSAGE(
    'The real estate could not be deleted.', status=500)
REAL_ESTATE_UPDATED = IMMOBIT_MESSAGE(
    'The real estate has been updated.', status=200)
REAL_ESTATE_DELETED = IMMOBIT_MESSAGE(
    'The real estate has been deleted.', status=200)
NO_SUCH_ATTACHMENT = IMMOBIT_MESSAGE(
    'The requested attachment does not exist.', status=404)
ATTACHMENT_CREATED = IMMOBIT_MESSAGE(
    'The attachment has been created.', status=201)
ATTACHMENT_DELETED = IMMOBIT_MESSAGE(
    'The attachment has been deleted.', status=200)
ATTACHMENT_EXISTS = IMMOBIT_MESSAGE(
    'The attachment already exists.', status=409)
ATTACHMENT_LIMIT_EXCEEDED = IMMOBIT_MESSAGE(
    'You have reached your attachment quota.', status=403)
