# answer -> 4416
# answer -> 5199

import io
import operator

# c inc -20 if c == 10

instructions = []
registers = {}
operators = {
    '>' : operator.gt,
    '<' : operator.lt,
    '>=' : operator.ge,
    '<=' : operator.le,
    '==' : operator.eq,
    '!=' : operator.ne
}
highest = 0
for line in open('input08.txt', 'r'):
    parts = [w for w in line.split() if w]
    regTarget = parts[0]
    regTest = parts[4]
    change = int(parts[2]) if parts[1] == 'inc' else -int(parts[2])
    opTest = operators[parts[5]]
    amtTest = int(parts[6])
    instructions.append((regTarget, change, regTest, opTest, amtTest))
    registers[parts[0]] = 0
    registers[parts[4]] = 0

for regTarget, change, regTest, opTest, amtTest in instructions:
    if (opTest(registers[regTest], amtTest)):
        registers[regTarget] = registers[regTarget] + change
    highest = max(highest, max(list(registers.values())))

print('part 1: ', max(list(registers.values())))
print('part 2: ', highest)

