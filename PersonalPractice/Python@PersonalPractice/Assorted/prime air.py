from collections import defaultdict
max_miles_till_now = float('-inf')
res = defaultdict(list)

for f in fRoute:
id1 = f[0]
miles1 = f[1]

if miles1 >= maxTravelDist:
continue

for r in rRoute:
id2, miles2 = r[0], r[1]

if miles2 >= maxTravelDist:
  continue

if miles1 + miles2 <= maxTravelDist and miles1+miles2 >= max_miles_till_now:
  res[miles1 + miles2].append([id1,id2])
  max_miles_till_now = miles1 + miles2
return res[max_miles_till_now ]
