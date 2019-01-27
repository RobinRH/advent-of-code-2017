# test -> 309
startA = 65
startB = 8921

# real -> 343
startA = 289
startB = 629

factorA = 16807
factorB = 48271

divisor = 2147483647

# last 16 bits are equal if (x % 16) are equal

def getNext(current, factor, divisor, multiple):
    next = (current * factor) % divisor
    while (next % multiple) != 0:
        next = (next * factor) % divisor
    return next

nextA = startA
nextB = startB
matches = 0
for i in range(5000000):
    nextA = getNext(nextA, factorA, divisor, 4)
    nextB = getNext(nextB, factorB, divisor, 8)
    #print nextA, nextB
    if (nextA % 65536) == (nextB % 65536) :
        #print bin(nextA % 16), bin(nextB % 16)
        matches += 1
    
print matches
