import re

test_pattern = r'^a{3,5}aa'

string_test = 'aaaaaa'

test_special_pattern = r'a\|b'

string_test_2 = r'ayes'

if re.search(test_pattern, string_test):
    print('yes')
else:
    print('no')

if re.match(test_special_pattern, string_test_2):
    print('yes')
else:
    print('no')

regex_pattern = r'([a-zA-Z]+)\s(\w+)'  # . any character, * any character zero or more times
txt = 'Apple and banana are fruits'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']


paragraph = ('I love teaching. '
             'If you do not love teaching what else can you love. '
             'I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.')

paragraph_pattern = r'love+'

matches = re.findall(paragraph_pattern, paragraph)
print(matches)






