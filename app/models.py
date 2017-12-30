from peewee import *
import os

# Create a database
from app.loadConfig import *
here = os.path.dirname(__file__)
cfg       = load_config(os.path.join(here, 'config.yaml'))
mainDB    = SqliteDatabase(cfg['databases']['dev'])

# Creates the class that will be used by Peewee to store the database
class dbModel (Model):
  class Meta:
    database = mainDB

"""
When adding new tables to the DB, add a new class here
Also, you must add the table to the config.yaml file

Example of creating a Table

class tableName (dbModel):
  column1       = PrimaryKeyField()
  column2       = TextField()
  column3       = IntegerField()

For more information look at peewee documentation
"""




class Refugees (dbModel):
  uid           = PrimaryKeyField()
  firstName     = TextField()
  lastName      = TextField()
  username      = TextField(unique = True)
  location      = TextField()
  experience    = TextField()
  education     = TextField()
  age           = IntegerField(null = True)
  socialsecurity= IntegerField(unique=True)

class Employers(dbModel):
  uid           = PrimaryKeyField()
  firstName     = TextField()
  lastName      = TextField()
  username      = TextField(unique = True)

class Asylums(dbModel):
  uid           = PrimaryKeyField()
  firstName     = TextField()
  lastName      = TextField()
  username      = TextField(unique = True)

class Jobs(dbModel):
    jid           = PrimaryKeyField()
    employer     =  ForeignKeyField(Employers)
    title         = TextField()
    address       = TextField()
    salary        = TextField()
    description   = TextField()
