import csv
with open("height-wieght.csv",newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)

new_data=[]

for i in range(len(filedata)):
    n=filedata[i][1]
    new_data.append(float(n))

n=len(new_data)
new_data.sort()

print(n)
if n%2==0:
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median=(median1+median2)/2

else:
    median=new_data[n//2]

print(median)