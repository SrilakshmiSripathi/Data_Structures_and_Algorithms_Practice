def uniqueOccurrences(arr):
        #if len(arr) == 1: return "true"
        arr = sorted(arr)
        d = {}
        for i in arr:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        occurences = []
        for k,v in d.items():
            print(k,v)
            if v in occurences:
                print(occurences)
                return ("false")
            else:
                occurences.append(v)
        return "true"

a =[1,2]
print(uniqueOccurrences(a))
arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(uniqueOccurrences(arr))

b = [1,2,2,1,1,3]
print(uniqueOccurrences(b))
