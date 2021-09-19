import re

f = open('input.txt', 'r')
p = ''
for line in f:
    p = p + (line)
data = re.findall(r'(?![0-9])\w+', p)

wc_hashtable = {}
for words in data:
    wc_hashtable[words] = wc_hashtable.get(words, 0) + 1
print wc_hashtable
print len(wc_hashtable)
