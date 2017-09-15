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
int(strname) will change the string to a number.
then create the dictionary using index 0 of the array
'''
def makedict(filename):
    d=dict()
    for line in open(filename):
        row=line.split()
        if len(row)==2:
            d[row[0]]=row[1]
    return d
        
     
      

print makedict("occupations.csv")

        

