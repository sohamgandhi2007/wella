import csv
with open("C-104.csv",newline="")as f:
    reader=csv.reader(f)
    data1=list(reader)
data1.pop(0)

newdata=[]

for trash in range(len(data1)):
    n=data1[trash][1]
    newdata.append(float(n))

findmean=len(newdata)
t=0

for x in newdata:
    total=total+x

mean=t/findmean

print("mean="+str(mean))