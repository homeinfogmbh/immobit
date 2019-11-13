"""ORM models."""

from datetime import datetime
from enum import Enum

from peewee import BooleanField
from peewee import CharField
from peewee import DateTimeField
from peewee import ForeignKeyField
from peewee import Model

from his import Account
from mdb import Customer
from peeweeplus import MySQLDatabase, EnumField

from immobit.config import CONFIG


__all__ = ['TransactionLog', 'CustomerPortal']


DATABASE = MySQLDatabase.from_config(CONFIG['db'])


class Action(Enum):
    """Possible openimmo actions."""

    CREATE = 'CREATE'
    REPLACE = 'REPLACE'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'


class ImmoBitModel(Model):
    """Basic immobit model."""

    class Meta:     # pylint: disable=C0111,R0903
        database = DATABASE
        schema = database.database


class TransactionLog(ImmoBitModel):
    """Stores real estate transactions."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'transaction_log'

    account = ForeignKeyField(Account, column_name='account')
    customer = ForeignKeyField(Customer, column_name='customer')
    objektnr_extern = CharField(255)
    action = EnumField(Action)
    success = BooleanField(default=False)
    start = DateTimeField()
    end = DateTimeField()

    def __enter__(self):
        """Initialize a new transaction."""
        self.start = datetime.now()
        return self

    def __exit__(self, *_):
        """Store transaction iff it is complete."""
        if self.account is not None:
            if self.objektnr_extern is not None:
                if self.action is not None:
                    self.end = datetime.now()
                    self.save()

    @property
    def duration(self):
        """Calculates the duration."""
        return self.end - self.start


class CustomerPortal(ImmoBitModel):
    """Configures customer-portal mappings."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'customer_portal'

    customer = ForeignKeyField(Customer, column_name='customer')
    portal = CharField(32)

    @classmethod
    def add(cls, customer, portal):
        """Adds a customer-portal mapping."""
        try:
            return cls.get((cls.customer == customer) & (cls.portal == portal))
        except cls.DoesNotExist:
            customer_portal = cls()
            customer_portal.customer = customer
            customer_portal.portal = portal
            customer_portal.save()
            return customer_portal
