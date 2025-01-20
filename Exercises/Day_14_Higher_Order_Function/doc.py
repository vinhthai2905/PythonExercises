def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

print(sum([1, 2, 3, 4, 5]))

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Using the outer_function to create a new function
add_five = outer_function(5)
print(add_five)

# Now add_five is a function that adds 5 to its argument
result = add_five(10)  # result is 15
print(result)
