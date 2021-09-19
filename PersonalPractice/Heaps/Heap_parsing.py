Heap = [4, 5, 6, 15, 9, 7, 20, 16, 25, 14, 12, 11, 8]
n = len(Heap)
nodes_parsed = []
while n > 1:
    if (n+1)%2 == 0:
        nodes_parsed += [0]
    else:
        nodes_parsed += [1]
    n = n//2

while len(nodes_parsed) != 0:
    x = nodes_parsed.pop()
    if x == 0:
        print "Goto Left node"
    else:
        print "Goto Right node"
