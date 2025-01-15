age = abs(int(input('Your age: ')))

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
if age >= 18:
    print('You are old enough to drive')
else:
    print(f'You are not old enough to drive, need more {18 - age} years')

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 10
your_age = int(input('Your age: '))

if my_age < 0 or your_age < 0:
    print('Either ages are not valid.')
elif my_age > 0 and your_age > 0:
    if my_age > your_age:
        if my_age - your_age == 1:
            print(f'My age is {my_age - your_age} year difference than yours.')
        else:
            print(f'My age is {my_age - your_age} years difference than yours.')
    else:
        if your_age - age == 1:
            print(f'Your age is {your_age - age} year difference than mine.')
        else:
            print(f'Your age is {your_age - age} years difference than mine.')
else:
    print('You and me are in the same age.')


#
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:


#  * If the person is married and if he lives in Finland, print the information in the following format:
