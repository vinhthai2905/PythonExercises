def counter(start):

    def inc(step=1):
        nonlocal start

        start += step
        print(start)

    return inc



my_inc = counter(5)
my_inc_2 = counter(10)

print(f'1: {my_inc.__code__.co_freevars}')
print(f'1: {my_inc.__closure__}')

my_inc_2()
print(f'2: {my_inc_2.__code__.co_freevars}')
print(f'2: {my_inc_2.__closure__}')

my_inc()
print(f'1: {my_inc.__code__.co_freevars}')
print(f'1: {my_inc.__closure__}')

my_inc_2()
print(f'2: {my_inc_2.__code__.co_freevars}')
print(f'2: {my_inc_2.__closure__}')



# my_inc_2 = counter(10)
#
# print(my_inc)
# print(my_inc_2)
# print(my_inc.__closure__)
# print(my_inc_2.__closure__)




def outer(name):
    a = 25

    def inner(prefix):
        print(prefix, name)

    return inner

my_func = outer('python')
my_func('name is')