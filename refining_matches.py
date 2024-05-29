# Refining matches with re.match

import re
# line ="This is python regex tutorial. We are using python3"
line ="python regex tutorial. We are using python3"

pat =r'\bpython'
match_ob = re.match(pat, line)
if match_ob:
    print(match_ob)
    print('matched from thepattern:', match_ob.group())
    print('startingindex:', match_ob.start())
    print('ending index:', match_ob.end()-1)
    print('Length:', match_ob.end()-match_ob.start())
else:
    print('No match found')