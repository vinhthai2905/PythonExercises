from math import expm1


def sum_of_five_nums(*args):
    sum_args = 0
    print(args)
    for i in range(len(args)):
        try:
            sum_args += args[i]
        except Exception as e:
            print(f'Value: {args[i]} at index {i}', e.__repr__())
    return sum_args

lst = [1, 2, 3, 4, 5, 'Hello']
print(sum_of_five_nums(*lst))

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Thai', 'country':'Finland', 'city':'Helsinki', 'age':250}

print(unpacking_person_info(**dct)) # Thai lives in Finland, Helsinki. He is 250 years old.