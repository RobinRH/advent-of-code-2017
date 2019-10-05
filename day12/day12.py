# answer -> 169
# answer -> 179

import io

# part 1

# 1327 <-> 100, 1069, 1170, 1441, 1641
file = open('input12.txt', 'r')
data = [x.strip().replace('<->', '').replace(',','').split() for x in file]
rules = { d[0]: d[1:] for d in data}

def getSet(value, rules):
    setValue = set([value])
    length = len(setValue)
    addedNew = True
    while addedNew:
        length = len(setValue)
        for number in setValue:
            setValue = setValue.union((set(rules[number])))
        addedNew = True if len(setValue) != length else False
    return(setValue)


print('part 1: ', len(getSet('0', rules)))

# part 2

# this algorithm removes all the rules dictionary entries
groups = []
while len(rules.keys()) > 0:
    # get the first key value
    value = list(rules.keys())[0]
    groups.append(value)
    valueSet = getSet(value, rules)
    # remove all those from the rules
    for item in valueSet:
        del rules[item]

print('part 2: ', len(groups))

