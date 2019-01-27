# answer -> 1141
import sys

with open(sys.argv[1], 'r') as content_file:
    content = content_file.read()

chars = list(content)
ilist = map(lambda x: int(x), chars)

sum = 0
for i in range(len(ilist)-1):
    if ilist[i] == ilist[i+1]:
        sum += ilist[i]

if (ilist[-1] == ilist[0]):
    sum += ilist[0]

print sum
