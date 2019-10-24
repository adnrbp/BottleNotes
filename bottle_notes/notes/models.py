import peewee
from utils.lib.db import *

class Note(peewee.Model):
    """Note Model.
    A Note is a writing consisting of a title and a description
    """
    title = peewee.CharField()
    description = peewee.TextField()

    class Meta:
        database = db
        db_table = 'Notes'

db.create_tables([Note,], safe=True)
