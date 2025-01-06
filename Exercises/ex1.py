import typing
import inspect


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

    def __init__(self, student_name, gpa):
        self.name = student_name
        self.gpa = gpa
        Student.total_student+=1

    @property
    def get_student_name(self):
        return 'This is my name', self.name

    def set_student_name(self):
        self.__setattr__('name', name)
        self.name = name

    def del_student_name(self):
        self.__delattr__('name')

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

#iter

test_string = {
    'name' : 'Thai',
    'age' : '25'
}

test_int = {
    1: 'Thai',
    2: '25'
}


new_iter = iter(test_string)


class Blog:
    number_of_blogs = 0

    def __init__(self):
        self._blog_lists = []

    def add_posts_to_list(self, blogs_list: List[str]):
        self._blog_lists.extend(blogs_list)
        Blog.number_of_blogs += self._blog_lists.__len__()

    def get_blogs_list(self) -> List[str]:
        return self._blog_lists

    def __iter__(self):
        return BlogIterator(self)

    @staticmethod
    def get_number_of_blogs():
        return Blog.number_of_blogs


class BlogIterator:
    def __init__(self, blogs: Blog):
        self._blogs = blogs
        self._current = 0
        self.test = blogs.get_blogs_list()

    def __next__(self):
        posts = self._blogs.get_blogs_list()

class GetItemOnly:
    def __init__(self, data: List[int]):
        self.data = data

    def __getitem__(self, index):
        if index < len(self.data):
            return self.data[index]
        else:
            raise IndexError  # Required for iteration to stop


new_list = Blog()



new_list.add_posts_to_list(['1', '2', '3'])

print(new_list.get_blogs_list())

test_iter_new = iter(new_list)

print(next(test_iter_new))

#len()

list()

#Local()

print(locals())

# map()

list_test = [1,2,3,4,5]



mapping = map(lambda x: x*2, list_test)


print(list(mapping))

# max()

list_1 = [1, 2, 3, 4, 5]
list_2 = [7, 8, 9, 10, 11]
print(max(list_1, list_2))

# MemoryView()

#min()

## object()

a = object()

## oct()

print('The oct number of this is: ', oct(2))

# open()

# ord()
print('Testing ord ord() function', ord('t'))

# pow()

# property

property()

class StudentK:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return self.first_name + '-' + self.last_name + '@kteam.com'

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, new_full_name):
        new_first_name, new_last_name = new_full_name.split(' ')
        self.first_name = new_first_name
        self.last_name = new_last_name

student_A = StudentK('Tran', 'Long')

student_A.first_name = 'Nguyen'
student_A.last_name = 'Thai'

print(student_A.first_name)
print(student_A.last_name)
print(student_A.email)
print(student_A.full_name)

student_A.full_name = 'Vinh Thai'

print(student_A.first_name)
print(student_A.last_name)
print(student_A.email)
print(student_A.full_name)




