# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
thirty_string = 'Thirty'
days_string = 'Days'
of_string = 'of'
python_string = 'Python'
strings = ['Thirty', 'Days', 'Of', 'Python']
combined_strings = ' '.join(strings)
print(f'Fully combined string: {thirty_string} {days_string} {of_string} {python_string}')
print(f'Fully combined string: {combined_strings}')

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding_strings = ['Coding', 'For', 'All']
combined_strings = ' '.join(coding_strings)
print(f'Fully combined string: {combined_strings}')

# Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding for all'

# Print the variable company using print().
print(f'Name of the company: {company}')

# Print the length of the company string using len() method and print().
print(f'The length of the "Company" is: {len(company)}')

# Change all the characters to uppercase letters using upper() method.
print(f'The upper case of "Company" is: {company.upper()}')

# Change all the characters to lowercase letters using lower() method.
print(f'The upper case of "Company" is: {company.lower()}')

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(f'The capitalize of "Company" is: {company.capitalize()}')

# Cut(slice) out the first word of Coding For All string.
sliced_string = company[0:6]
print(f'Sliced string: {sliced_string}')

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
find_string = input('Specify the string you want to find: ')
if company.__contains__(find_string.capitalize()):
    print('It is existed.')
else:
    print('Not existed.')

# Replace the word coding in the string 'Coding For All' to Python.
replaced_word = input('Specify the word you want to change: ')
print(company.replace('Coding', replaced_word))


# Change Python for Everyone to Python for All using the replace method or other methods.
# Split the string 'Coding For All' using space as the separator (split()) .
split_string = company.split()
print(split_string)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company_strings = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
split_company_string = company_strings.split(', ')
print(f'Company strings after being splitting: {split_company_string}')

# What is the character at index 0 in the string Coding For All.
# What is the last index of the string Coding For All.
# What character is at index 10 in "Coding For All" string.
# Create an acronym or an abbreviation for the name 'Python For Everyone'.

phrase = 'Python For Everyone'
acronym = ''.join(word[0] for word in phrase.split())
print(acronym)

# Create an acronym or an abbreviation for the name 'Coding For All'.
# Use index to determine the position of the first occurrence of C in Coding For All.
cfa_phrase = 'Coding For All'
print(cfa_phrase.index('C'))
print(cfa_phrase.index('or', 5))

# Use index to determine the position of the first occurrence of F in Coding For All.
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
start_index = sentence.find('because because because')
end_index = start_index + len('because because because')
sliced_sentence = sentence[start_index:end_index + 1]
print(sliced_sentence)

# Does ''Coding For All' start with a substring Coding?
# Does 'Coding For All' end with a substring coding?
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# Use the new line escape sequence to separate the following sentences.