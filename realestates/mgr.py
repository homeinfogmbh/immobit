"""Managers"""

from peewee import DoesNotExist

from openimmodb import Anhang
from homeinfo.lib.wsgi import OK, Binary, InternalServerError

from .errors import NoAttachmentSpecified, NoSuchAttachment


class AttachmentManager():
    """Manages real estate attachments"""

    def __init__(self, immobilie, sha256sum):
        """Sets immobilie DOM and SHA-256 hex string"""
        self.immobilie = immobilie
        self.sha256sum = sha256sum

    @property
    def anhang(self):
        """Returns the respective Anhang ORM model"""
        try:
            return Anhang.get(
                (Anhang._immobilie == self.immobilie) &
                (Anhang.sha256sum == self.sha256sum))
        except DoesNotExist:
            raise NoSuchAttachment() from None

    @property
    def data(self):
        """Returns the respective data"""
        return self.anhang.data

    def get(self):
        """Gets the respective data"""
        if self.sha256sum is None:
            raise NoAttachmentSpecified() from None
        else:
            return Binary(self.data)

    def add(self, path):
        """Adds an attachment"""
        if self.anhang.link_to(path):
            return OK()
        else:
            raise InternalServerError('Could not create link') from None
