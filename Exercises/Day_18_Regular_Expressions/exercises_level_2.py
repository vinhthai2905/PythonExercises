import re

plus_pattern =  r'\b\d+\b(?![\d-])'
minus_pattern = r'-\d+'

points = '-12 -4 -3 -1 0 4 8'

plus_numbers = re.findall(plus_pattern, points)
print(plus_numbers)

minus_numbers = re.findall(minus_pattern, points)
print(minus_numbers)


lst = ['first_name', 'first-name', '1first_name', 'firstname']

def is_valid_variable(*args):
    info_lst = []
    valid_variable_pattern = r'^[a-z]+_?[a-z]+$'

    for variable in args:
        if re.match(valid_variable_pattern, variable):
            print(f'This {variable} is valid')
            info_lst.append(variable)
        else:
            print(f'This {variable} is invalid')

    return info_lst

valid_variables_list = is_valid_variable(*lst)