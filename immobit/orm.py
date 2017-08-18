"""ORM models"""

from datetime import datetime

from peewee import DoesNotExist, Model, PrimaryKeyField, ForeignKeyField, \
    CharField, DateTimeField, BooleanField

from homeinfo.crm import Customer
from his.orm import his_db, Account

__all__ = ['TransactionLog', 'CustomerPortal']


database = his_db('immobit')


class ImmoBitModel(Model):
    """Basic immobit model"""

    id = PrimaryKeyField()

    class Meta:
        database = database
        schema = database.database


class TransactionLog(ImmoBitModel):
    """Stores real estate transactions"""

    class Meta:
        db_table = 'transaction_log'

    account = ForeignKeyField(Account, db_column='account')
    customer = ForeignKeyField(Customer, db_column='customer')
    objektnr_extern = CharField(255)
    action = CharField(6)  # CREATE, UPDATE, DELETE
    success = BooleanField(default=False)
    start = DateTimeField()
    end = DateTimeField()

    def __enter__(self):
        """Initialize a new transaction"""
        self.start = datetime.now()
        return self

    def __exit__(self, *_):
        """Store transaction iff it is complete"""
        if self.account is not None:
            if self.objektnr_extern is not None:
                if self.action is not None:
                    self.end = datetime.now()
                    self.save()

    @property
    def duration(self):
        """Calculates the duration"""
        return self.end - self.start


class CustomerPortal(ImmoBitModel):
    """Configures customer-portal mappings"""

    class Meta:
        db_table = 'customer_portal'

    customer = ForeignKeyField(Customer, db_column='customer')
    portal = CharField(32)

    @classmethod
    def add(cls, customer, portal):
        """Adds a customer-portal mapping"""
        try:
            return cls.get((cls.customer == customer) & (cls.portal == portal))
        except DoesNotExist:
            customer_portal = cls()
            customer_portal.customer = customer
            customer_portal.portal = portal
            customer_portal.save()
            return customer_portal
