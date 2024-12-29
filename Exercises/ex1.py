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