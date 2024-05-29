# Using re.compile

import re
line ="This is python regex tutorial using python3"
pat =r'\bpython\d'
print('using re.search:', re.search(pat, line))
print('using re.findal:',re.findall(pat, line))
print('using re.match:',re.match(pat, line))
pat_ob= re.compile(pat)
print('Pattern Object:' , pat_ob)
print('using re.compile with re.search:', pat_ob.search(line))
print('using re.compile with re.findall:', pat_ob.findall(line))
print('using re.compile with re.match:', pat_ob.match(line))