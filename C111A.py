import pandas as pd
import plotly.figure_factory as ff
import statistics 
import csv
import random
import plotly.graph_objects as go
df = pd.read_csv('data1.csv')
data = df['Math_score'].to_list()
fig =ff.create_distplot([data],['Math Score'],show_hist=False)
fig.show()
mean1 = statistics.mean(data)
median = statistics.median(data)
standDiviation = statistics.stdev(data)
print(mean1)
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
first_Start,first_End= mean-standDiviation,mean+ standDiviation
Second_Start,Second_End = mean - (2*standDiviation),mean +(2*standDiviation)
Thrid_Start,Thrid_End = mean- (3*standDiviation),mean +(3*standDiviation)
fig = ff.create_distplot([meanList],['Math_score'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y =[0,0.20],mode ='lines', name ='Mean'))
fig.add_trace(go.Scatter(x=[first_Start,first_Start],y = [0,0.20],mode ='lines', name ='First Start'))
fig.add_trace(go.Scatter(x=[first_End,first_End],y = [0,0.20],mode ='lines', name ='First End'))
fig.add_trace(go.Scatter(x=[Second_Start,Second_Start],y = [0,0.20],mode ='lines', name ='Second Start'))
fig.add_trace(go.Scatter(x=[Second_End,Second_End],y = [0,0.20],mode ='lines', name ='Second End'))
fig.add_trace(go.Scatter(x=[Thrid_Start,Thrid_Start],y = [0,0.20],mode ='lines', name ='Thrid Start'))
fig.add_trace(go.Scatter(x=[Thrid_End,Thrid_End],y = [0,0.20],mode ='lines', name ='Thrid End'))
fig.show()
zScore = (mean -mean1)/standDiviation
print(zScore)
