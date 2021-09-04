File = open("sum.txt","r")

lt = 0
for line in File:
        lt += int(line.rstrip())
print str(lt)[:10]
