# Searching a string for patterns using re.search

import re
line ="This is python regex tutorial. We are using python3"
pat =r'\bpython'
print(re.search(pat, line))

# match_obj = re.search(pat, line, flags=0)
print(re.match(pat,line))