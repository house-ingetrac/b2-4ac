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
    d = dict()
   # s = open(filename).read()
    #print s
    for line in open(filename):
        if line[0]=='"':
            ctr=1
            while line[ctr]< len(line):
                if line[ctr]!= '"':
                    ctr+=1
                else:
                    d= dict(line[0:ctr+1],line [ctr+1:])

        else:
            cntr=len(line)
            while cntr!=0:
                if line[cntr]==",":
                    d=(dict(line[0:ctr],line[ctr:len(line)+1]))
            ctr-=1
    print d
            
makedict("occupations.csv")

        

