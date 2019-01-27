# test -> 588
startA = 65
startB = 8921

# real -> 638
startA = 289
startB = 629

factorA = 16807
factorB = 48271

divisor = 2147483647

# last 16 bits are equal if (x % 16) are equal

nextA = startA
nextB = startB
matches = 0
for i in range(40000000):
    nextA = (nextA * factorA) % divisor
    nextB = (nextB * factorB) % divisor
    # get the lowest 16 bits
    if (nextA % 65536) == (nextB % 65536) :
        matches += 1
    
print matches
