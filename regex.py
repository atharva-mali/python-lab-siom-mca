# import re

# mystr = "test 12 testing 123 testing 78 testing 456"
# list1 = re.findall(r'\s+', mystr)

# count = 0
# for _ in list1:
#     count += 1

# print(count)

# Example 2
import re

mystr = "test 12 testing 123 testing 78 testing 456"
print(re.findall(r'\w+',mystr))
print(re.findall(r'\w{6,}', mystr))



