import re

f =open('who.txt', 'r')

for eachline in f:
    eachline = eachline.rstrip('\n')
    print(re.split(r'\s\s+|\t', eachline))
    
f.close()