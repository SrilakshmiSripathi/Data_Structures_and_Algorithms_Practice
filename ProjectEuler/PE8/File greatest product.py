# read file
File = open("numbers8.txt",'r')

# make it a list
lt = []
for line in File:
        lt += line.rstrip()

# calculate max product

maximum = 1
for i in range(len(lt)):
    k = 1
    for j in range(i,i+13):
        try:
            k *= int(lt[j])
            if k >= maximum:
                maximum = k
        except IndexError:
            break
print maximum
