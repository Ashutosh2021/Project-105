import csv 
import math

with open("data.csv","r",newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


length = len(file_data)
sum_of_numbers = 0

for marks in file_data:
   sum_of_numbers+=float(marks[0])

mean = sum_of_numbers/length

print("Mean :",mean)

sd1 = 0

for num in file_data:
    sd1 = float((float(num[0])-mean)**2+sd1)

sd2 = float(sd1/(length-1))
sd = math.sqrt(sd2)

print("Standard Deviation :",sd)