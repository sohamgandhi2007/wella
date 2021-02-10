import csv
import numpy as np
import pandas as pd

def getdatasource(data_path):
    coffe=[]
    slepp=[]
    with open(data_path)as f:
        csvreader=csv.DictReader(f)
        for row in csvreader:
            coffe.append(float(row['Coffe']))
            slepp.append(float(row['Slepp']))
    return{"x":coffe,"y":slepp}

def findcorrelation(data_source):
    correlation=np.corrcoef(data_source['x'],data_source['y'])
    print(correlation[0,1])

def setup():
    data_path="coffevsslepp.csv"
    data_source=getdatasource(data_path)
    findcorrelation(data_source)

setup()