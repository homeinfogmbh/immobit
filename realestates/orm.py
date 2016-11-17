"""ORM models"""

from datetime import datetime

from peewee import ForeignKeyField, CharField, DateTimeField, BooleanField

from homeinfo.crm import Customer
from his.orm import service_table, HISModel, Account

__all__ = ['TransactionLog']


@service_table('realestates')
class TransactionLog(HISModel):
    """Stores real estate transactions"""

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
