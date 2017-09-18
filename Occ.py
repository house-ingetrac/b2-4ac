'''
Team B2-4ac- Bayan Berri, Alessandro Cartegni
SoftDev1 pd7
HW03: StI/O: Divine your Destiny!
2017-09-14
'''
import random

def makedict(filename):
    d = dict()
    for line in open(filename):
        newline= line[line.rfind("n")]
        d[line[0:line.rfind(',')]] = line[line.rfind(',')+1:len(line)-1]#deals with the categories that include commas
    #print d
    return d

#make string numbers into floats
def make_float(d):
    for k in d:
        try:
            d[k]=float(d[k])
        except:
            d[k]=d[k]
    return d

#makes an array to then select a random choice
def make_arr(d):
    jobs=[]
    for k in d:
        if type(d[k])!= str and k!="Total":
            ctr= int(d[k]*10)
            while ctr!=0:
                jobs.append(k)
                ctr-=1
    return jobs

#final selection
def get_random(arr):
    return random.choice(arr)
    
        
#output
print get_random(make_arr(make_float(makedict("occupations.csv"))))
#print len(make_arr(make_float(makedict("occupations.csv"))))

 

