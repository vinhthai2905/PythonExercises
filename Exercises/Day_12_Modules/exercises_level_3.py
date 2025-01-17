import random

def shuffle_list(lst):
    shuffled_lst = lst.copy()
    random.shuffle(shuffled_lst)
    return shuffled_lst

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6]
shuffled_numbers_list = shuffle_list(numbers_list)
print(shuffled_numbers_list)

def random_numbers_array(n):
    random_number_list = list()
    for index in range(n):
        random_generated_number = random.randrange(9)

        while random_generated_number in random_number_list:
            random_generated_number = random.randrange(9)

        random_number_list.append(random_generated_number)
    return random_number_list

n = int(input('How many number in an array: '))

print(random_numbers_array(n))