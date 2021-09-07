"""
import sys

f = open("new.txt")
print f.read()
# 42850541

for i, lines in enumerate(f):
    print lines
    print "\n \n i" , i


    

    name = str(i) + '.' + 'txt'
    newfile = open(name,'w')
    newfile.write()
    newfile.close
     for lineno, line in enumerate(bigfile)
"""


lines_per_file = 1
smallfile = None

with open('E:\soa\Posts.xml') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
        print smallfile
    if smallfile:
        smallfile.close()
        
    
