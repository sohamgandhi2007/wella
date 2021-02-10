import csv
import numpy as np
import pandas as pd
import plotly_express as px

def getdatasource(data_path):
    sizeoftv=[]
    avgtimespent=[]
    with open(data_path)as f:
        csvreader=csv.DictReader(f)
        for row in csvreader:
            sizeoftv.append(float(row['SizeofTV']))
            avgtimespent.append(float(row['Averagetime']))
    return{"x":sizeoftv,"y":avgtimespent}

def findcorrelation(data_source):
    correlation=np.corrcoef(data_source['x'],data_source['y'])
    print(correlation[0,1])

def setup():
    data_path="sizevstime.csv"
    data_source=getdatasource(data_path)
    findcorrelation(data_source)

setup()