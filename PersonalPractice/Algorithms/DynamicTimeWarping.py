## Dynamic Time Warping
def DTWDistance(t1, t2):
    dtw = [[float('inf') for i in range(len(t2))]\
              for j in range(len(t1))]
    dtw[0][0] = 0

    for i in range(len(t1)):
        for j in range(len(t2)):
            cost = abs(t1[i] - t2[j])
            if i-1 >= 0 or j-1 >= 0:
                dtw[i][j] = cost + min(dtw[i-1][j], dtw[i][j-1], dtw[i-1][j-1])
    print dtw
    monotonic = []           
    i, j = len(dtw)-1, len(dtw[0])-1
    while i >= 0 and j >= 0:
        a = dtw[i][j]
        b = dtw[i-1][j]
        c = dtw[i][j-1]
        d = dtw[i-1][j-1]
        if a <= b and a <= c and a <= d:
            ## correcting index by 1, as we are using 0 indexing
            monotonic.append([i+1, j+1])
        if b < c and b < d:
            i = i-1
            j = j
        elif c < d and c < b:
            i = i
            j = j-1
        else:
            i = i-1
            j = j-1                        
    return monotonic[::-1]

TimeX = (3, 9, 9, 5)
TimeY = (3, 3, 9, 5, 5)
print DTWDistance(TimeX, TimeY)
