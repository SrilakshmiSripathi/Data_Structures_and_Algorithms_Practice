def find(F, B, T):
    ans = [0, 0, 0]
    F = sorted([x, i] for i,x in F)
    for idy,y in B:
        f = 0
        end = len(F)
        z = T - y
        while f != end:
            m = int((f + end)/2)
            if F[m][0] <= z:
                f = m+1
            else:
                end = m
        if f != 0 and y+F[f-1][0] > ans[0]:
            ans = [y+F[f-1][0], F[f-1][1], idy]
    return ans
        
print (find([(1,3000),(2,5000),(3,7000),(4,10000)],
	 [(1,2000),(2,3000),(3,4000), [4,5000]], 10000))
