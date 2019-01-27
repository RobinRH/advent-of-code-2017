# answer 1632

import csv
import sys

filename = sys.argv[1]
layers = dict()

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=':')
    for row in reader:
        layer = map((lambda x : int(x)), row)
        layers[layer[0]] = layer[1]

def getLayerAtTime(depth, time):
    # find the remainder of depth * 2
    remainder = time % ((depth - 1) * 2)
    if remainder < depth:
        return remainder
    else:
        return depth*2 - remainder


maxTime = max(layers.keys())

collisions = []

for time in range(maxTime + 1):
    if time in layers.keys():
        scannerLocation = getLayerAtTime(layers[time], time)
        if scannerLocation == 0:
            collisions.append(time)

# calculate severity
severity = 0
for c in collisions:
    severity += c * layers[c]

print severity
    
