# answer: 1898341
input = 344
point0 = 0
point1 = 5935
skip = input
size = 5936

pos = 1
for i in range(5936, 50000000):
    pos = pos + skip + 1
    if pos > size:
        pos = pos - size
    size += 1
    if pos == 1:
        point1 = i
        print "*", point1
    # print pos, point1, size


'''
* 10545
* 41867
* 45544
* 187773
* 474004
* 1898341 - correct!
'''


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
799704 - not sure about this one, couldn't repro
'''
