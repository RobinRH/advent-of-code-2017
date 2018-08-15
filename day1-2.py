#answer -> 950
import sys

with open(sys.argv[1], 'r') as content_file:
    content = content_file.read()
ilist = map(lambda x: int(x), list(content))

length = len(ilist)
skip = length / 2

# now just double the list to avoid the circular thing
ilist.extend(ilist)
extended = ilist
print extended

sum = 0
for i in range(length):
    if extended[i] == extended[i+skip]:
        sum += extended[i]

print sum
