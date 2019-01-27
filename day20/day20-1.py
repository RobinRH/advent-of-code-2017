# answer -> 300

import sys
import csv
from math import *

class Point:

    def __init__(self, pav, id):
        self.position = pav[0]
        self.velocity = pav[1]
        self.acceleration = pav[2]
        self.id = id

    def __str__(self):
        return ' : '.join([str(self.position), str(self.velocity), str(self.acceleration)])
        

# p=<-11104,1791,5208>, v=<-6,36,-84>, a=<19,-5,-4>

def parse(s):
    #p=<-11104,1791,5208>
    s = s.replace('p=<', '').replace('v=<', '').replace('a=<', '').replace('>', '')
    values = map(lambda x: int(x), s.split(','))
    return values

filename = sys.argv[1]
points = []
id = 0
with open(filename, 'r') as f:
    for row in f:
        parts = row.split(', ')
        pav = map(lambda x: parse(x), parts)
        pt = Point(pav, id)
        points.append(pt)
        id += 1

# find largest acceleration, abs
minAcc = 1000000
minPt = None
for pt in points:
    accl = reduce(lambda x, y: abs(x) + abs(y), pt.acceleration)
    if accl < minAcc:
        minAcc = accl
        minPt = pt

print minPt.id, minAcc