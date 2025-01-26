import re

test_pattern = r'^a{3,5}aa'

string_test = 'aaaaa'

if re.search(test_pattern, string_test):
    print('yes')
else:
    print('no')





