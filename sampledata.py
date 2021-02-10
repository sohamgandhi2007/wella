import csv
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import plotly.graph_objects as go 

df=pd.read_csv("sampledata.csv")
data=df["average"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    
    mean=statistics.mean(dataset)
    return mean
    
def showfig(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["average"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode ="lines"))
    fig.show()

def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=random_set_of_mean(100)
        meanlist.append(setofmeans)

    showfig(meanlist)
    mean=statistics.mean(meanlist)
    print("mean of sample distribution is-",mean)
setup()