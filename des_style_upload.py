project_home="/Users/jmoxon/Clothesliner/"
csv_home="/Users/jmoxon/Clothesliner/testload.csv"

import sys, os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from clothes.models import *

import csv
dataReader = csv.reader(open(csv_home, "rU"), delimiter=',')

for row in dataReader:
    add = Style()
    add.name=row[2]
    add.save()
