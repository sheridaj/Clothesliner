project_home="/Users/jmoxon/Clothesliner/"
csv_home="/Users/jmoxon/Clothesliner/testload.csv"

import sys, os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from clothes.models import *

import csv
dataReader = csv.reader(open(csv_home, "rU"), delimiter=',')

for row in dataReader:
#    add_des = Designer()
 #   add_des.name = row[0]
  #  add_des.webAddress = row[2]
   # add_des.save()
    designer = Designer.objects.get(name = row[1])
    style = Style.objects.get(name = row[2])
    pant=Pant()
    pant.designer= designer
    pant.style = style
    pant.waist=row[7]
    pant.front_rise=row[8]
    pant.back_rise=row[9]
    pant.hips=row[10]
    pant.inseam=row[11]
    pant.thigh=row[12]
    pant.knee=row[13]
    pant.outseam=row[14]
    pant.designer_waist=row[3]
    pant.designer_inseam=row[4]
    pant.save() 
