"""WSGI interface."""

from wsgilib import Application

from immobit.wsgi.attachments import get_attachment, add_attachment, \
    patch_attachment, delete_attachment
from immobit.wsgi.contacts import get_contacts
from immobit.wsgi.portals import get_portals
from immobit.wsgi.realestates import get_real_estates, get_real_estate, \
    add_real_estate, delete_real_estate, patch_real_estate

__all__ = ['APPLICATION']


APPLICATION = Application('ImmoBit', debug=True, cors=True)
APPLICATION.route('/attachments/<int:ident>', methods=['GET'])(get_attachment)
APPLICATION.route('/attachments/<int:ident>', methods=['POST'])(add_attachment)
APPLICATION.route('/attachments/<int:ident>', methods=['PATCH', 'PUT'])(
    patch_attachment)
APPLICATION.route('/attachments/<int:ident>', methods=['DELETE'])(
    delete_attachment)
APPLICATION.route('/contacts', methods=['GET'])(get_contacts)
APPLICATION.route('/portals', methods=['GET'])(get_portals)
APPLICATION.route('/realestates', methods=['GET'])(get_real_estates)
APPLICATION.route('/realestates/<int:ident>', methods=['GET'])(get_real_estate)
APPLICATION.route('/realestates/', methods=['POST'])(add_real_estate)
APPLICATION.route('/realestates/<int:ident>', methods=['DELETE'])(
    delete_real_estate)
APPLICATION.route('/realestates/<int:ident>', methods=['PATCH'])(
    patch_real_estate)
