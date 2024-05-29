# Replace Multiple Spaces with single space

import re
line = 'abc  def      ghi    ktm'
## match whitespace present once or more times
pattern = r'\s+'
## replace with single space
replace =' '
print(re.sub(pattern, replace, line))