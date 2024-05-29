import re
number = input('Enter phone number: ')
pattern =r'\d{3}[ ]\d{3}[ ]\d{4}$'
if re.match(pattern, number):
    print("Match")
else:
    print("No Match")