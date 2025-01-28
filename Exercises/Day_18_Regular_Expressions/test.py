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






