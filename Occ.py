'''
Team B2-4ac- Bayan Berri, Alessandro Cartegni
SoftDev1 pd7
HW03: StI/O: Divine your Destiny!
2017-09-14
'''
import random

## Separate all of the rows of the csv


def makedict(filename):
    d = dict()
   # s = open(filename).read()
    #print s
    for line in open(filename):
        newline= line[line.rfind("n")]
       # d=dict(,line[line.rfind(',')+1:len(line)+1])
        d[line[0:line.rfind(',')]] = line[line.rfind(',')+1:len(line)-1]
    #print d
    return d            
def make_float(d):
    for k in d:
        try:
            d[k]=float(d[k])
        except:
            d[k]=d[k]
    return d

print make_float(makedict("occupations.csv"))

        

