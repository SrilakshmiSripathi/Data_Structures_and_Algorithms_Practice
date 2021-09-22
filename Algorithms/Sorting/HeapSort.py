def heapsort(lst):
    
  # in pseudo-code, heapify only called once, so inline it here
  for start in range((len(lst)-2)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst
 
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    right = root *2 +2
    if child > end:
        break
    if right <= end and lst[child] < lst[right]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      return
print heapsort([101,2,300,4,5,650,7,88,9,90,10,11,12,13,14,15,46,50,80])
