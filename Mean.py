import csv
with open("height-wieght.csv",newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)

newdata=[]

for i in range(len(filedata)):
    n=filedata[i][1]
    newdata.append(float(n))

m=len(newdata)
total=0

for x in newdata:
    total=total+x

mean=total/m

print("mean="+str(mean))