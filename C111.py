import pandas as pd
import plotly.figure_factory as ff
import statistics 
import csv
import random
import plotly.graph_objects as go
df = pd.read_csv('studentMarks.csv')
data = df['Math_score'].to_list()
fig =ff.create_distplot([data],['Math Score'],show_hist=False)
fig.show()
mean = statistics.mean(data)
median = statistics.median(data)
standDiviation = statistics.stdev(data)
print(mean)
print(median)
print(standDiviation)
def randomsetofMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data) -1)
        value =data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
meanList=[]
for i in range(0,1000):
    set = randomsetofMean(100)
    meanList.append(set)
standDiviation = statistics.stdev(meanList)
mean =statistics.mean(meanList)
print(mean)
print(standDiviation)
fig = ff.create_distplot([meanList],['Math_score'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y =[0,0.20],mode ='lines', name ='Mean'))
fig.show()