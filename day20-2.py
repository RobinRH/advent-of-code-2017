# answer -> 502

import sys
import csv
from math import *

class Point:

    def __init__(self, pav, id):
        self.position = pav[0]
        self.velocity = pav[1]
        self.acceleration = pav[2]
        self.id = id

    def updateVelocity(self):
        for i in range(3):
            self.velocity[i] += self.acceleration[i]

    def updateLocation(self):
        for i in range(3):
            self.position[i] += self.velocity[i]


    def __str__(self):
        return ' : '.join([str(self.position), str(self.velocity), str(self.acceleration)])
        

# p=<-11104,1791,5208>, v=<-6,36,-84>, a=<19,-5,-4>

def parse(s):
    #p=<-11104,1791,5208>
    s = s.replace('p=<', '').replace('v=<', '').replace('a=<', '').replace('>', '')
    values = map(lambda x: int(x), s.split(','))
    return values

def removeCollisions(points):
    pointsToRemove = set()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            ipt = points[i]
            jpt = points[j]
            if (ipt.position[0] == jpt.position[0]) and (ipt.position[1] == jpt.position[1]) and (ipt.position[2] == jpt.position[2]):
                pointsToRemove.add(ipt)
                pointsToRemove.add(jpt)

    if len(pointsToRemove) > 0:
        print "removing this many points: ", len(pointsToRemove)
    
    pointsToRemove = list(pointsToRemove)
    for p in range(len(pointsToRemove)):
        ptRemove = pointsToRemove[p]
        points.remove(ptRemove)

    return len(pointsToRemove)

filename = sys.argv[1]
points = []
id = 0
with open(filename, 'r') as f:
    for row in f:
        parts = row.split(', ')
        pav = map(lambda x: parse(x), parts)
        pt = Point(pav, id)
        print pt
        points.append(pt)
        id += 1


'''
smallSet = []
for d in range(50):
    smallSet.append(points[d])

points = smallSet
'''

removed = 0
removeCollisions(points)
# run it until you don't see anymore collisions (and hope you're right)
for t1 in range(200):
    for t2 in range(1): 
        # update location
        for p in points:
            p.updateVelocity()
            p.updateLocation()

        # remove collisions
        removed += removeCollisions(points)

        # update velocity
        #for pt in points:
        #    pt.updateVelocity()

    print t1, t2

print removed
print len(points)