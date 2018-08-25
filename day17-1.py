# test
#input = 3 # answer : 638

#real
input = 344 # answer : 996

class Node:

    def __init__(self, value, ptr):
        self.value = value
        self.ptr = ptr


current = Node(0, None)
current.ptr = current
zeroptr = current

for i in range(1, 2018):
    # move forward "input" steps
    for j in range(input):
        current = current.ptr
    # insert the next node
    newNode = Node(i, current.ptr)
    current.ptr = newNode
    if current.value == 0: print zeroptr.ptr.value
    current = newNode

# what is the current node pointing at
print current.ptr.value

def printLoop(current, length):
    output = ''
    for i in range(length):
        output += str(current.value)
        current = current.ptr
    print output

#printLoop(current, 10)
'''
1
7
14
15
89
246
2344
2726
5935
10545
41867
45544
187773
474004
799704
'''
