it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print('The length of the set:', len(it_companies))

# Add 'Twitter' to it_companies
it_companies.update({'Twitter'})
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update({'Python', 'Javascript', 'FastAPI'})
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.difference_update({'Google'})
print(it_companies)
# What is the difference between remove and discard