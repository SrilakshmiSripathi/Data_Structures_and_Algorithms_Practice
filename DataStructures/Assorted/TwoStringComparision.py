str1 = "abcd aabc bd"
str2 = "aaa aa"

a = str1.split(" ")
b = str2.split(" ")

details = []
for i in range(0, min(len(a),len(b)), 1):
    count = 0
    if a < b:
        count += 1
    else:
        pass
    details.append(count)
print(details)
    

#[print(a,b) for a, b in zip(a, b)) if a < b]
