"""ORM models"""

from datetime import datetime

from peewee import Model, PrimaryKeyField, ForeignKeyField, CharField, \
    DateTimeField, BooleanField

from his.config import config
from his.orm import Account

from homeinfo.peewee import MySQLDatabase

__all__ = ['TransactionLog']


class ImmoBitModel(Model):
    """Generic model for ImmoBit's tables"""

    class Meta:
        database = MySQLDatabase(
            'his_fs',
            host=config.db['HOST'],
            user=config.db['USER'],
            passwd=config.db['PASSWD'],
            closing=True)
        schema = database.database

    id = PrimaryKeyField()


class TransactionLog(ImmoBitModel):
    """Stores real estate transactions"""

    class Meta:
        db_table = 'transaction_log'

    account = ForeignKeyField(Account, db_column='account')
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
                else:
                    print('action', self.action, sep='=', flush=True)
            else:
                print('objektnr_extern', self.objektnr_extern,
                      sep='=', flush=True)
        else:
            print('account', self.account, sep='=', flush=True)

    @property
    def duration(self):
        """Calculates the duration"""
        return self.end - self.start
