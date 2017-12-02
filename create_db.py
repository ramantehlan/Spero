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
users = Users(  firstName = "Scott",
                lastName  = "Heggen",
                username  = "heggens",
                age       = 33,
                program   = "1"
             ).save()

users = Users(  firstName = "Matt",
                lastName  = "Jadud",
                username  = "jadudm",
                age       = 39,
                program   = "2"
             ).save()           
             
prog = Programs ( programName = "Computer and Information Science",
                  abbreviation = "CSC"
                ).save()

prog = Programs ( programName = "Technology and Applied Design",
                  abbreviation = "TAD"
                ).save()

course =  Courses ( courseName = "Software Design and Implementation",
                    coursePrefix = "CSC",
                    courseNumber = 226,
                    pid = 1,
                    instructor = 1
                  ).save()

course =  Courses ( courseName = "Electricity and Electronics",
                    coursePrefix = "TAD",
                    courseNumber = 265,
                    pid = 2,
                    instructor = 2
                  ).save()
