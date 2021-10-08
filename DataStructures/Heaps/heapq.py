import heapq as hq

a = []
#l = [5,6,2,3,4,1]
l = [(5,6),(2,3),(1,4,1)]
for i in range(len(l)):
    hq.heappush(a,l[i])
#print(hq.heappop(a))
print(hq.nsmallest(2,a))
print(hq.nlargest(2,a))




