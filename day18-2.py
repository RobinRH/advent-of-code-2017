#answer: 8001

import csv
import sys

class Instruction:

    def __init__(self, keywordAndArgs):
        self.keyword = keywordAndArgs[0]

        if keywordAndArgs[1] in 'abcdefghijklmnop':
            self.X = keywordAndArgs[1]
        else:
            self.X = int(keywordAndArgs[1])

        if len(keywordAndArgs) == 3:
            if keywordAndArgs[2] in 'abcdefghijklmnop':
                self.Y = keywordAndArgs[2]
            else:
                self.Y = int(keywordAndArgs[2])
        else:
            self.Y = 0

    def __str__(self):
        return self.keyword + " " + str(self.X) + " " + str(self.Y)

class Machine:

    def __init__(self, instructions):
        regNames = list('abcdefghijklmnop')
        self.registers = dict()
        for r in regNames:
            self.registers[r] = 0
        self.instructions = instructions
        self.counter = 0
        self.sendCount = 0
        self.messageQueue = []
        self.recieveCount = 0
        self.whatwassent = []
        self.whatwasrecieved = []

    def runOne(self):

        inst = self.instructions[self.counter]
        sendValue = 0
        if inst.keyword == 'snd': #send the register value to the other queue
            sendValue = inst.X if (type(inst.X) is int) else self.registers[inst.X]
            #print "sending: ", sendValue
            self.counter += 1
            self.sendCount += 1
            self.whatwassent.append(sendValue)
            return(self.counter, sendValue)
        elif inst.keyword == 'set': # set register X to value Y
            yValue = inst.Y if (type(inst.Y) is int) else self.registers[inst.Y]
            self.registers[inst.X] = yValue
            self.counter += 1
            return(self.counter, None)
        elif inst.keyword == 'add': # increment register X by value Y
            yValue = inst.Y if (type(inst.Y) is int) else self.registers[inst.Y]
            self.registers[inst.X] = self.registers[inst.X] + yValue
            self.counter += 1
            return(self.counter, None)
        elif inst.keyword == 'mul': # multiply register X by value Y
            yValue = inst.Y if (type(inst.Y) is int) else self.registers[inst.Y]
            self.registers[inst.X] = self.registers[inst.X] * yValue
            self.counter += 1
            return(self.counter, None)
        elif inst.keyword == 'mod': # set register X to X % Y
            yValue = inst.Y if (type(inst.Y) is int) else self.registers[inst.Y]
            self.registers[inst.X] = self.registers[inst.X] % yValue
            self.counter += 1
            return(self.counter, None)
        elif inst.keyword == 'rcv': # recieve the next message
            if len(self.messageQueue) > 0:
                self.registers[inst.X] = self.messageQueue[0]
                self.messageQueue.pop(0)
                self.counter += 1
                #print "messageQ receiving: ", self.registers[inst.X], self.messageQueue
                self.recieveCount += 1
                self.whatwasrecieved.append(self.registers[inst.X])
                return(self.counter, None)
            else:
                return(self.counter, None)
        elif inst.keyword == 'jgz': # if X > 0, then jump Y
            xValue = inst.X if (type(inst.X) is int) else self.registers[inst.X]
            yValue = inst.Y if (type(inst.Y) is int) else self.registers[inst.Y]
            if xValue > 0:
                self.counter += yValue
            else:
                self.counter += 1
            return(self.counter, None)
        else:
            print "instruction not found: " + inst.keyword

        return -1
    

filename = sys.argv[1]

total = 0
instructions = []
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        total += 1
        instructions.append(Instruction(row))


machineA = Machine(instructions)
machineB = Machine(instructions)
machineB.registers['p'] = 1

locked = False
done = False
lastA = 0
lastB = 0
msgCount = 0
while not locked and (msgCount < 100000):
    resultA = machineA.runOne()
    resultB = machineB.runOne()
    #print resultA, resultB
    if (resultA[0] == lastA) and (resultB[0] == lastB):
        # deadlock
        print "ended in deadlock"
        print "sendsB: ", machineB.sendCount
        exit()

    if not resultA[1] is None:
        machineB.messageQueue.append(resultA[1])
        #print "machineA sending: ", resultA[1]

    if not resultB[1] is None:
        machineA.messageQueue.append(resultB[1])
        #print "machineB sending: ", resultB[1]

    msgCount += 1
    lastA = resultA[0]
    lastB = resultB[0]

print machineA.registers
print machineB.registers
print machineA.whatwassent, machineB.whatwasrecieved
print len(machineA.whatwassent)
print "runs: ", msgCount
print "sends: ", machineA.sendCount


'''
machine1 = Machine(instructions)
result = -1
while result < 0:
    result = machine1.runOne()

print result

'''