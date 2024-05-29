# String using whitespace

import re
my_str = 'NAME="/dev/sda" PARTLABEL="" TYPE="disk"'
## \s+ will match one or more whitespace
text = re.split(r'\s+', my_str)
print(text)