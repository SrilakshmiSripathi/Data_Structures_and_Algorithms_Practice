# Bob's Bolt

def SortBobBolts(lsA, lsB):
    A = {}
    for bolts in lsA:
        A.update({bolts:0})
    pairs = []
    for bolts in lsB:
        if bolts in A:
            pairs.append([bolts, bolts])
            del (A[bolts])
        print A
    return pairs


l1 = ['#', '^', '$', '%', '!', '@', '~', '(', ')',]
l2 = ['#', '^', '$', '%', '!', '@', '~', '(', ')',]

b1 = [5, 7, 2, 1, 8, 9, 12, 15, 16, 99, 55, 41, 53, 67]
b2 = [9, 67, 12, 15, 8, 1, 53, 16, 99, 5, 41, 7, 2, 55]
print SortBobBolts(l1, l2)
print SortBobBolts(b1, b2)
