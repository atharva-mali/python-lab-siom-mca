import re
line = "This is python regex tutorial. We are using python3"
pat=r'\bpython'
match_ob= re.search(pat, line)
print('matched fromthe pattern:', match_ob.group())
print('startingindex:', match_ob.start())
print('ending index:', match_ob.end()-1)
print('Length:' , match_ob.end()- match_ob.start())