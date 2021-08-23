import math
import csv
with open('val1.csv' , newline = '') as f:
    reader =  csv.reader(f) 
    file_data = list(reader)
data = file_data[0]
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return(mean)

squared_list = []
for num in data:
    a = int( num ) - mean(data)
    a = a**2
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum = sum + i
result = sum / (len(data) - 1)
sd = math.sqrt(result)
print(sd) 

