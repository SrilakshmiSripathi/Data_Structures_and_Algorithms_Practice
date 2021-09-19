# Two Color Dutch Flag

def Sort2colors(a):
    """ Input: array of unsorted colors, assuming 1 be first
        color, 2 be second color.
        Output: Inplace sorted array """
    j = len(inp)-1
    i = 0
    while i <= j: 
        if inp[i] == 1:
            i = i + 1
        elif inp[j] == 2:
            j = j - 1
        else:
            inp[i], inp[j] = inp[j], inp[i]
            i = i + 1
            j = j - 1
    return inp

inp = [1,2,2,1,2,1,2,1,2,1,1]
inp2 = [2,2,2,1,2,1,2,1,1,2]

print Sort2colors(inp),Sort2colors(inp2)


