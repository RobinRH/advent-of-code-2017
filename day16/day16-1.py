#answer -> cgpfhdnambekjiol

import csv
import sys

class Step:

    def __init__(self, stepString):
        pass

    def move(self, current):
        return current

    def toString(self):
        print ""

class TranslationStep(Step):

    def __init__(self, stepString):
        # "sn"
        stepString = stepString.replace('s', '')
        self.length = int(stepString)

    def move(self, current):
        slen = len(current)
        newstring = current[slen - self.length:] + current[0:slen - self.length]
        return newstring

    def toString(self):
        return "s:" + str(self.length)

class SwapPositionStep(Step):

    def __init__(self, stepString):
        # "xi/j"
        stepString = stepString.replace('x', '')
        parts = stepString.split('/')
        self.i = int(parts[0])
        self.j = int(parts[1])

    def move(self, current):
        temp = current[self.i]
        current[self.i] = current[self.j]
        current[self.j] = temp
        return current

    def toString(self):
        return 'x:' + str(self.i) + '/' + str(self.j)   

class SwapProgramsStep(Step):

    def __init__(self, stepString):
        # "pa/b"
        stepString = stepString[1:]
        parts = stepString.split('/')
        self.a = parts[0]
        self.b = parts[1]

    def move(self, current):
        aloc = current.index(self.a)
        bloc = current.index(self.b)
        temp = current[aloc]
        current[aloc] = current[bloc]
        current[bloc] = temp
        return current
        
    def toString(self):
        return "p:" + self.a + '/' + self.b 

filename = sys.argv[1]
stepStrings = []
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        stepStrings = row


current = list('abcdefghijklmnop')
#current = list('abcde')
steps = []
for step in stepStrings:
    if step.startswith('s'):
        steps.append(TranslationStep(step))
    
    if step.startswith('x'):
        steps.append(SwapPositionStep(step))

    if step.startswith('p'):
        steps.append(SwapProgramsStep(step))

stepStringTest = map(lambda x : x.toString(), steps)
print stepStringTest[0:10]

for step in steps:
    current = step.move(current)

print current
current = ''.join(current)
print current


'''
# test for swap programs
programs = list('abcdefgh')
print programs
sp = SwapProgramsStep("pd/g")
programs = sp.move(programs)
print sp.toString()
print programs

# test for swap positions
programs = list('abcdefgh')
print programs
sp = SwapPositionStep("x1/3")
programs = sp.move(programs)
print sp.toString()
print programs


# test for translation

s = list('abcdefgh')
ss = TranslationStep('s6')
print ss.toString()
s = ss.move(s)
print s

'''


