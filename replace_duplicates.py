import re
line = 'This this is a Python Python tutorial'
## reference to the first half of that pattern
pattern =r'(\w+) \1'
## replace with single space
replace = r'\1'

print(re.sub(pattern, replace, line, flags=re.IGNORECASE))
