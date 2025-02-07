import os

try:
    with open('files/test.txt', mode='r') as f:
        print(f.read())
except Exception as e:
    print(e)


try:
    print(os.ctermid())
except Exception as e:
    print(e.__repr__())


string_test = '''I 
                am 
                a 
                god'''

print(string_test)

print('This is ending test.')