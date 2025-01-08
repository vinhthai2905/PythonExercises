import math

first_name = 'Vinh'
last_name = 'Thai'
print('Length of my name is:', len(first_name))

# Compare the length of your first name and your last name

if len(first_name) > len(last_name):
    print('First name is longer than last name.')
elif len(first_name) < len(last_name):
    print('Last name is longer than first name.')
else:
    print('First name and last name are of equal length.')

# 4. Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4

# 5. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print('Total is:', total)

# 6. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print('Minus is:', diff)

# 7. Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print('Multiple is:', product)

# 8. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print('Division is:', division)

# 9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two
print('Remainder is:', remainder)

# 10. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = pow(5,4)
print('Exp is', exp)

# 11. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print('Floor division is: ', floor_division)

# 12. The radius of a circle is 30 meters.
PI = 3.14

# 13. Calculate the area of a circle and assign the value to a variable name of area_of_circle
# 14. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# 15. Take radius as user input and calculate the area.
# 16. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('Your first name? ')
last_name = input('Your last name? ')
country = input('Your country? ')
age = input('Your age? ')

print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)

# 17. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

help('keywords')