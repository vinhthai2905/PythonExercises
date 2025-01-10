name_1 = 'python'
name_2 = 'dragon'
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in name_1 and name_2:
    print('It existed in both variable')
else:
    print('It does not')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon'
if 'jargon' in sentence:
    print('jargon is existed in sentence')
else:
    print('Does not existed')

# There is no 'on' in both dragon and python
if 'on' not in name_1 and 'on' not in name_2:
    print('There is no "on" in both dragon and python')
else:
    print('It does')

# Find the length of the text python and convert the value to float and convert it to string
float_value = float(len(name_1))
print(float_value)
str_value = str(float_value)
print(str_value)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = input('Type the given number you want to test: ')
if not int(number) % 2 == 0:
    print('This number is not even')
else:
    print('This number is even')

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# Check if type of '10' is equal to type of 10
num_1 = 10
num_2 = '10'
if type(num_1) == type(num_2):
    print('Equal')
else:
    print('Not Equal')

# Check if int('9.8') is equal to 10
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?