"""WSGI service for web-based access"""

from peewee import DoesNotExist

from homeinfo.lib.wsgi import Error, OK, WsgiApp
from openimmo import openimmo
from openimmodb3.db import Immobilie


class OpenImmoDBController(WsgiApp):
    """Main controller"""

    def get(self):
        """Posts data under the respective resource"""
        if len(self.path == 3):
            try:
                cid = int(self.path[-1])
            except (TypeError, ValueError):
                return Error('Customer ID must be an integer')
            else:
                openimmo_obid = int(self.path[-1])
                try:
                    immobilie = openimmo.CreateFromDocument(data)
                except:
                    return Error('Invalid data', status_code=400)
                else:
                    try:
                        immobilie.toxml()
                    except:
                        return Error('Flawed data', status_code=400)
                    else:
                        try:
                            openimmo_obid = immobilie.openimmo_obid
                        except AttributeError:
                            return Error('Not a real estate')
                        else:
                            try:
                                Immobilie.get(
                                    (Immobilie.customer == cid) &
                                    (Immobilie.openimmo_obid == openimmo_obid))
                            except DoesNotExist:
                                record = Immobilie.add(cid, immobilie)
                                return OK(record.id)
                            else:
                                return Error('Real estate already exists')

    def post(self, data):
        """Posts data under the respective resource"""
        if len(self.path == 2):
            try:
                cid = int(self.path[-1])
            except (TypeError, ValueError):
                return Error('Customer ID must be an integer')
            else:
                try:
                    immobilie = openimmo.CreateFromDocument(data)
                except:
                    return Error('Invalid data', status_code=400)
                else:
                    try:
                        immobilie.toxml()
                    except:
                        return Error('Flawed data', status_code=400)
                    else:
                        try:
                            openimmo_obid = immobilie.openimmo_obid
                        except AttributeError:
                            return Error('Not a real estate')
                        else:
                            try:
                                Immobilie.get(
                                    (Immobilie.customer == cid) &
                                    (Immobilie.openimmo_obid == openimmo_obid))
                            except DoesNotExist:
                                record = Immobilie.add(cid, immobilie)
                                return OK(record.id)
                            else:
                                return Error('Real estate already exists')
