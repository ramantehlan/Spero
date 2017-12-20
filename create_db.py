# WARNING: NOT FOR USE IN PRODUCTION AFTER REAL DATA EXISTS!!!!!!!!!!!!!!!!!!!!!!
'''
This script creates the database tables in the SQLite file.
Update this file as you update your database.
'''
import os, sys
import importlib

# Don't forget to import your own models!
from app.models import *

conf = load_config('app/config.yaml')

sqlite_dbs  = [ conf['databases']['dev']
                # add more here if multiple DBs
              ]

# Remove DBs
for fname in sqlite_dbs:
  try:
    print ("Removing {0}.".format(fname))
    os.remove(fname)
  except OSError:
    pass

# Creates DBs
for fname in sqlite_dbs:
  if os.path.isfile(fname):
    print ("Database {0} should not exist at this point!".format(fname))
  print ("Creating empty SQLite file: {0}.".format(fname))
  open(fname, 'a').close()


def class_from_name (module_name, class_name):
  # load the module, will raise ImportError if module cannot be loaded
  # m = __import__(module_name, globals(), locals(), class_name)
  # get the class, will raise AttributeError if class cannot be found
  c = getattr(module_name, class_name)
  return c

"""This file creates the database and fills it with some dummy run it after you have made changes to the models pages."""
def get_classes (db):
  classes = []
  for str in conf['models'][db]:
    print ("\tCreating model for '{0}'".format(str))
    c = class_from_name(sys.modules[__name__], str)
    classes.append(c)
  return classes


mainDB.create_tables(get_classes('mainDB'))

# Adding dummy data

refugee = Refugees( firstName = "Scott",
                    lastName="Johnson",
                    username="scottj",
                    location="Burton St. Lexington, KY",
                    experience="1 year",
                    education="High School",
                    age=33,
                    socialsecurity=121324435
                  ).save()

refugee = Refugees( firstName = "Ahmad",
                    lastName="Hafiz",
                    username="hafiza",
                    location="112 Safari St. Dubai 20827",
                    experience="4 years",
                    education="Bachelor's Degree",
                    age=26,
                    socialsecurity=121321213124
                  ).save()


asylum =  Asylums( firstName = "Kenaria", lastName="Brown", username="brownk").save()
asylum =  Asylums( firstName = "Halima", lastName="Azizi", username="halima").save()

employer =  Employers( firstName = "Aqueel", lastName="Dawood", username="davood").save()
employer =  Employers( firstName = "Muhammad", lastName="Shatri", username="shatri").save()
employer =  Employers( firstName = "Matthew", lastName="Jadud", username="matthew").save()
employer =  Employers( firstName = "Mario", lastName="Robins", username="marior").save()

job = Jobs(employer=1, title="Car Washer", address="24 Lexington Ave, CA, USA", salary="$8/hour" ).save()
job = Jobs(employer=2, title="Front-end Developer", address="65 Burton Ave, KY, USA", salary="$15/hour" ).save()
job = Jobs(employer=3, title="Maintenance Technician", address="344 Lexington Ave, CA, USA", salary="$7/hour" ).save()
job = Jobs(employer=4, title="Driver", address="75 Alto Ave, CA, USA", salary="$11/hour" ).save()
job = Jobs(employer=1, title="Cashier", address="190 Burton Ave, MA, USA", salary="$9/hour" ).save()
job = Jobs(employer=2, title="Painter Wanted", address="90 San Luis Ave, NY, USA", salary="$9/hour" ).save()
job = Jobs(employer=3, title="Post Office", address="232 Morro Ave, CA, USA", salary="$9/hour" ).save()
