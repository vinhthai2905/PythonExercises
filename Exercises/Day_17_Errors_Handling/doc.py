import sys
import logging


try:
    print(10 + '5')
except Exception as e:
    print(e.__repr__())
    print(e)
else:
    print('Everything worked.')

print(5+20)

values = [1, 2, 3, 4, 5, 0, 'Hello']



for value in values:
    try:
        print(10 / int(value))
    except Exception as e:
        print(f'Error at "{value}" ', e.__repr__())
