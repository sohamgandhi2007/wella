import csv
import pandas as pd 
import statistics

df=pd.read_csv("props.csv")
height_list=df['Height(Inches)'].to_list()
weight_list=df['Weight(Pounds)'].to_list()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)

height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

height_stdev=statistics.stdev(height_list)
weight_stdev=statistics.stdev(weight_list)

heightfirst_stdev_start,heightfirst_stdev_end=height_mean-height_stdev,height_mean+height_stdev
heightsecond_stdev_start,heightsecond_stdev_end=height_mean-(2*height_stdev),height_mean+(2*height_stdev)
heightthird_stdev_start,heightthird_stdev_end=height_mean-(3*height_stdev),height_mean+(3*height_stdev)

weightfirst_stdev_start,weightfirst_stdev_end=weight_mean-weight_stdev,weight_mean+weight_stdev
weightsecond_stdev_start,weightsecond_stdev_end=weight_mean-(2*weight_stdev),weight_mean+(2*weight_stdev)
weightthird_stdev_start,weightthird_stdev_end=weight_mean-(3*weight_stdev),weight_mean+(3*weight_stdev)

height_listofdata_within1stdev=[result for result in height_list if result>heightfirst_stdev_start and result<heightfirst_stdev_end]
height_listofdata_within2stdev=[result for result in height_list if result>heightsecond_stdev_start and result<heightsecond_stdev_end]
height_listofdata_within3stdev=[result for result in height_list if result>heightthird_stdev_start and result<heightthird_stdev_end]

weight_listofdata_within1stdev=[result for result in weight_list if result>weightfirst_stdev_start and result<weightfirst_stdev_end]
weight_listofdata_within2stdev=[result for result in weight_list if result>weightsecond_stdev_start and result<weightsecond_stdev_end]
weight_listofdata_within3stdev=[result for result in weight_list if result>weightthird_stdev_start and result<weightthird_stdev_end]

print(len(height_listofdata_within1stdev)*100.0/len(height_list))
print(len(height_listofdata_within2stdev)*100.0/len(height_list))
print(len(height_listofdata_within3stdev)*100.0/len(height_list))