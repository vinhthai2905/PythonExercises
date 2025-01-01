import sys

numbers = [1, 2, 3, 4, 5]
strings_lists = ['a', 'b', 'c']

print(any(numbers))

print(bool())

my_string = "coding's345"

print(my_string.isdigit())


## BIN()
## Return the binary representation of an integer.

print(bin(1))

# BREAKPOINT()
# STOP AT THE BREAKPOINT LINE TO DEBUGGING

## breakpoint()

#BYTEARRAY()

print(bytearray(numbers))

#BYTE()

print(bytes(numbers))

# Callable()

print(callable(numbers))

# chr()

x = chr(523)
print("chr() function: " + x)

# ClassMethod()

class Student:

    total_student = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.total_student+=1

    @classmethod
    def student_count(cls):
        return f'Total # students: {cls.total_student}'


print(f'Total students: ', Student.student_count())

John = Student('John', '2.74')

# Compile()

# Complex()
x = complex('5')
print(f'Complex {x}')

# Delattr()

delattr(John,'name')

print(John.gpa)

#dict()

schools = dict({'1': 1})
print(schools.get('2', 'Not found'))

# dir()
# Return list of things in current scope

dict()
print(dir(John))

print('Get attribute for John: ' + John.__getattribute__('gpa'))

def greet(**kwargs):
    for key, value in kwargs.items():
        kwargs.items()
        print(f"{key}: {value}")

greet(name="Alice", age=25, city="New York")


# DivMod()

print(divmod(12,3))

from typing import TypeVar, List, FrozenSet

T = TypeVar('T')

def element(items: List[T]) -> T:
    return items[0]

# Usage
print(element([1, 2, 3]))
print(element(['a', 'b', 'c']))


#Enumarate()

number_list = enumerate(numbers, 0)

number_list_2 = dict(a=1, b=2, c=3)


print(list(number_list_2.values()))

# Filter()

# Define a function that returns True for even numbers
def is_even(num):
    return bool(num % 2 == 0)

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to get even numbers
even_numbers = filter(is_even, numbers)

# Convert the filter object to a list and print it
print(list(even_numbers))

## Float()

x = float()

## Format()


name = "Alice"
age = 30

formatted_string = "Name: {}, Age: {}".format(name, age)
print(formatted_string)  # Output: Name: Alice, Age: 30

## Frozenset()
# Same thing as set but immutable

numbers_set = frozenset([1,2,3,4,5])

print('Set of numbers: ', numbers_set)

read_only: FrozenSet[str] = frozenset({'read'})
read_write: FrozenSet[str] = frozenset({'read', 'write'})
admin: FrozenSet[str] = frozenset({'read', 'write', 'delete'})

roles: dict[FrozenSet[str], str] = {
    read_only: 'Viewer',
    read_write: 'Editor',
    admin: 'Administrator'
}

permissions: frozenset[str] = frozenset({'write', 'read'})
role: str = roles.get(permissions, 'Unknown')

print('The current role is:', role)

egg_sandwich_ingredient: frozenset[str] = frozenset({'bread', 'eggs'})
beef_sandwich_ingredient: frozenset[str] = frozenset({'bread', 'beefs'})

recipes : dict[FrozenSet[str], str] = {
    egg_sandwich_ingredient: 'Egg Sandwich',
    beef_sandwich_ingredient: 'Beef Sandwich'
}

user_recipe = frozenset({'bread', 'eggs'})

print('The user.s recipe:', recipes.get(user_recipe, 'Not found'))
## Getattr()

print('GPA of John is:', getattr(John, 'gpa'))

#Global

print('All available variables: ', globals())

#Hasattr()

if hasattr(John, 'gpa'):
    print('Yes, John do have gpa attr')

#Hash()

print('The value of this object: ', hash(numbers_set))
print(id(number_list))

#Help()

#Hex()

#id()

#int

#isInstance

test = (1,2,3,4)
print(isinstance(John, Student))

#isSubclass()