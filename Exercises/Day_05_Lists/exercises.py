it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', '10']
# Add an IT company to it_companies
#
# Insert an IT company in the middle of the companies list
#
# Change one of the it_companies names to uppercase (IBM excluded!)

it_companies_new = []

for index, company in enumerate(it_companies):
    if company != 'IBM':
        it_companies[index] = company.upper()

print(it_companies)

# Join the it_companies with a string '#;  '
joined_companies = '#;  '.join(it_companies)
print(joined_companies)


# Check if a certain company exists in the it_companies list.
company = input('Select the company you want: ').upper()
if company in it_companies:
    print('It is exist in the list.', it_companies.__contains__(company))
else:
    print('Does not exist')
# Sort the list using sort() method
#
# Reverse the list in descending order using reverse() method
reversed_list = reversed(it_companies)
print(list(reversed_list))


# Slice out the first 3 companies from the list
sliced_companies = it_companies[:3]
print(sliced_companies)

# Slice out the last 3 companies from the list
sliced_companies_last = it_companies[2:]
print(sliced_companies_last)
# Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2

# Slice out the middle company (or companies if the list length is even)
if len(it_companies) % 2 == 0:
    sliced_middle = it_companies[middle_index-1:middle_index+1]
else:
    sliced_middle = it_companies[middle_index:middle_index+1]

print(sliced_middle)
# Remove the first IT company from the list
#
# Remove the middle IT company or companies from the list
#
# Remove the last IT company from the list
#
# Remove all IT companies from the list
#
# Destroy the IT companies list
it_companies.clear()
print(it_companies)

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_fullstack = front_end.copy()
joined_fullstack.extend(back_end)

print(joined_fullstack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

joined_fullstack.insert(joined_fullstack.index('Redux') + 1, 'Python')
joined_fullstack.insert(joined_fullstack.index('Python') + 1, 'SQL')

print(joined_fullstack)