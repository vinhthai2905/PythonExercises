numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

for number in range(len(numbers) - 1):
    print(number)


person = {
    'first_name': 'Vinh',
    'last_name': 'Thai',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(person.keys())

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)


# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for _ in range(8):
    for _ in range(7):
        print('#', end=' ')
    print()


for number in range(11):
    print(f'{number} * {number} = {number * number}')

for number in range(101):
    if number % 2 == 0:
        print(number)
    else:
        continue

