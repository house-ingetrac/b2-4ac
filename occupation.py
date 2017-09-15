'''
Team B2-4ac- Bayan Berri, Alessandro Cartegni
SoftDev1 pd7
HW03: StI/O: Divine your Destiny!
2017-09-14
'''
import csv
import random

## Separate all of the rows of the csv
'''
for every line in the file:
make a new array/list .
'''


for line in open("occupations.csv"):
    row=line.split()

print row

