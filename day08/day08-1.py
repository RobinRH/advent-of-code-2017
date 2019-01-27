#answer -> 4416
import csv
import sys

filename = sys.argv[1]

# example: b inc 5 if a > 1
class Instruction:

    def __init__(self, register, action, amount, ifRegister, ifOperator, ifAmount):
        self.register = register
        self.action = action
        self.amount = amount
        self.ifRegister = ifRegister
        self.ifOperator = ifOperator
        self.ifAmount = ifAmount


instructions = []
#registerNames = set()
registers = dict()
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        instructions.append(Instruction(row[0], row[1], int(row[2]), row[4], row[5], int(row[6])))
        #registerNames.add(row[0])
        registers[row[0]] = 0

# example: b inc 5 if a > 1
for ins in instructions:
    # determine if condition is true
    isTrue = False
    # get the register value
    regValue = registers[ins.ifRegister]
    # get the value to compare
    compValue = ins.ifAmount
    if ins.ifOperator == '==':
        isTrue = (regValue == compValue)
    elif ins.ifOperator == '!=':
        isTrue = (regValue != compValue)
    elif ins.ifOperator == '<':
        isTrue = (regValue < compValue)
    elif ins.ifOperator == '<=':
        isTrue = (regValue <= compValue)
    elif ins.ifOperator == '>':
        isTrue = (regValue > compValue)
    elif ins.ifOperator == '>=':
        isTrue = (regValue >= compValue)

    if isTrue:
        currentRegValue = registers[ins.register]
        if ins.action == 'inc':
            registers[ins.register] = currentRegValue + ins.amount
        else:
            registers[ins.register] = currentRegValue - ins.amount

maxRegister = max(registers.values())
print registers.values()

print maxRegister
        

      
