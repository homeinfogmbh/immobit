"""Error message definitions."""

from wsgilib import JSONMessage


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
    'ATTACHMENT_LIMIT_EXCEEDED'
]


INVALID_REAL_ESTATE_ID = JSONMessage('Invalid real estate ID.', status=422)
NO_SUCH_REAL_ESTATE = JSONMessage(
    'The requested real estate does not exist.', status=404)
REAL_ESTATE_CREATED = JSONMessage(
    'The real estate has been created.', status=201)
CANNOT_ADD_REAL_ESTATE = JSONMessage(
    'Could not add the real estate.', status=500)
REAL_ESTATE_EXISTS = JSONMessage(
    'The real estate already exists.', status=409)
CANNOT_DELETE_REAL_ESTATE = JSONMessage(
    'The real estate could not be deleted.', status=500)
REAL_ESTATE_UPDATED = JSONMessage(
    'The real estate has been updated.', status=200)
REAL_ESTATE_DELETED = JSONMessage(
    'The real estate has been deleted.', status=200)
NO_SUCH_ATTACHMENT = JSONMessage(
    'The requested attachment does not exist.', status=404)
ATTACHMENT_CREATED = JSONMessage(
    'The attachment has been created.', status=201)
ATTACHMENT_DELETED = JSONMessage(
    'The attachment has been deleted.', status=200)
ATTACHMENT_LIMIT_EXCEEDED = JSONMessage(
    'You have reached your attachment quota.', status=403)
