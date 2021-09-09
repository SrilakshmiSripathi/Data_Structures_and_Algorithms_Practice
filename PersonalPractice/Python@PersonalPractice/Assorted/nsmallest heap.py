import heapq

def nsmallest(T,val):
    """Input: Heap T of n elements and query key-val
        Output: Elements in heap less than val"""
    p = 0
    # Check if the keys less than val are present in heap 
    while p <= val and len(T) != 0:
        p = heapq.heappop(T)
        print p

T = [17,4,5,6,15,9,7,16,25,14,12,11,8,20,3,10,13,2]
heapq.heapify(T)
nsmallest(T,40)
nsmallest(T,7)
