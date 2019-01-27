# answer 3834136
# runs for a few minutes

import csv
import sys

filename = sys.argv[1]
layers = dict()

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=':')
    for row in reader:
        layer = map((lambda x : int(x)), row)
        layers[layer[0]] = layer[1]

print layers

def getLayerAtTime(depth, time):
    # find the remainder of depth * 2
    remainder = time % ((depth - 1) * 2)
    if remainder < depth:
        return remainder
    else:
        return depth*2 - remainder

def calculateSeverity(collisions):
    severity = 0
    for c in collisions:
        severity += c * layers[c]
    return severity

maxConfigs = 1
for v in layers.values():
    maxConfigs *= v
        
maxTime = max(layers.keys())

finalDelay = 0
for delay in range(0, 10000000, 2):
    collisions = []
    for time in range(99):
        if time in layers.keys():
            scannerLocation = getLayerAtTime(layers[time], time + delay)
            if scannerLocation == 0:
                collisions.append(time)
    if len(collisions) == 0:
        finalDelay = delay
        print "Found"
        break
    else:
        pass
        #print "severity: " + str(calculateSeverity(collisions))

print finalDelay

