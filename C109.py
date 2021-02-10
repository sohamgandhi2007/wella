import csv
import pandas as pd 
import statistics

df=pd.read_csv("C109.csv")
math_list=df['Math(score)'].to_list()
read_list=df['Reading(score)'].to_list()

math_mean=statistics.mean(math_list)
read_mean=statistics.mean(read_list)

math_median=statistics.median(math_list)
read_median=statistics.median(read_list)

math_mode=statistics.mode(math_list)
read_mode=statistics.mode(read_list)

math_stdev=statistics.stdev(math_list)
read_stdev=statistics.stdev(read_list)

mathfirst_stdev_start,mathfirst_stdev_end=math_mean-math_stdev,math_mean+math_stdev
mathsecond_stdev_start,mathsecond_stdev_end=math_mean-(2*math_stdev),math_mean+(2*math_stdev)
maththird_stdev_start,maththird_stdev_end=math_mean-(3*math_stdev),math_mean+(3*math_stdev)

readfirst_stdev_start,readfirst_stdev_end=read_mean-read_stdev,read_mean+read_stdev
readsecond_stdev_start,readsecond_stdev_end=read_mean-(2*read_stdev),read_mean+(2*read_stdev)
readthird_stdev_start,readthird_stdev_end=read_mean-(3*read_stdev),read_mean+(3*read_stdev)

math_listofdata_within1stdev=[result for result in math_list if result>mathfirst_stdev_start and result<mathfirst_stdev_end]
math_listofdata_within2stdev=[result for result in math_list if result>mathsecond_stdev_start and result<mathsecond_stdev_end]
math_listofdata_within3stdev=[result for result in math_list if result>maththird_stdev_start and result<maththird_stdev_end]

read_listofdata_within1stdev=[result for result in read_list if result>readfirst_stdev_start and result<readfirst_stdev_end]
read_listofdata_within2stdev=[result for result in read_list if result>readsecond_stdev_start and result<readsecond_stdev_end]
read_listofdata_within3stdev=[result for result in read_list if result>readthird_stdev_start and result<readthird_stdev_end]

print(len(math_listofdata_within1stdev)*100.0/len(math_list))
print(len(math_listofdata_within2stdev)*100.0/len(math_list))
print(len(math_listofdata_within3stdev)*100.0/len(math_list))

print(len(read_listofdata_within1stdev)*100.0/len(read_list))
print(len(read_listofdata_within2stdev)*100.0/len(read_list))
print(len(read_listofdata_within3stdev)*100.0/len(read_list))