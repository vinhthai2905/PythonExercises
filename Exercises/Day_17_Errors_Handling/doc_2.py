values = [1, 2, 3, 4, 5, 0 , 'Hello']

for value in values:
    if value is not int():
        raise Exception()