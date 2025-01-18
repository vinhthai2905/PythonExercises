# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_list = [x for x in numbers if x < 0 or x == 0]
print(filtered_list)

# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
list_of_lists_2 =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


flatten_list_1 = [inner_list for outer_list in list_of_lists_2 for inner_list in outer_list]
flatten_list_2 = [number for outer_list in list_of_lists for inner_list in outer_list for number in inner_list]

flatten_list_true = []



for inner_list in list_of_lists:
    for inner_inner_list in inner_list:
        for number in inner_inner_list:
            flatten_list_true.append(number)

print(flatten_list_1)
print(flatten_list_2)

# Using list comprehension create the following list of tuples:

# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

result = [(i, 1, i**1, i**2, i**3, i**4, i**5, i**6) for i in range(11)]
print(result)


# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries_list = [countries_tuple for countries_inner_list in countries for countries_tuple in countries_inner_list]
print(countries_list)
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
# Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
countries_list = [{
    'country': countries_tuple.__getitem__(0),
    'city': countries_tuple.__getitem__(1)
} for countries_inner_list in countries for countries_tuple in countries_inner_list]

print(countries_list)

# Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_list = [' '.join([names_tuples.__getitem__(0), names_tuples.__getitem__(1)]) for names_inner_list in names for names_tuples in names_inner_list]
print(concatenated_list)
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']