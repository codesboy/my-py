import re

string = '42.2万' #42.2
string1 = '209万' #200

r = re.findall('\d.+\d',string1)
print(r)