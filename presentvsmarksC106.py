import csv
import numpy as np
import pandas as pd

def getdatasource(data_path):
    rollno=[]
    dayspresent=[]
    with open(data_path)as f:
        csvreader=csv.DictReader(f)
        for row in csvreader:
            rollno.append(float(row['RollNo']))
            dayspresent.append(float(row['DaysPresent']))
    return{"x":rollno,"y":dayspresent}

def findcorrelation(data_source):
    correlation=np.corrcoef(data_source['x'],data_source['y'])
    print(correlation[0,1])

def setup():
    data_path="studentmarksvspresentday.csv"
    data_source=getdatasource(data_path)
    findcorrelation(data_source)

setup()