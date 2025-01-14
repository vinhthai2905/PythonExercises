dog = {
    'name': 'blue',
    'breed': 'husky',
    'legs': 4,
    'ages': 2,
}

student = {
    'first_name': 'Bui',
    'last_name': 'Vinh Thai',
    'gender': 'male',
    'age': 22,
    'martial status': 'single',
    'skills': ['IT', 'English', 'Math'],
    'country': 'VietNam',
    'city': 'DN',

}

# Create an empty dictionary called dog
# Add name, color, breed, legs, age to the dog dictionary
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# Get the length of the student dictionary
print('Length of the student:', len(student))

# Get the value of skills and check the data type, it should be a list
print('Data type of skills:,', type(student.get('skills')))
print('Values of skills:', student.get('skills'))
# Modify the skills values by adding one or two skills
student.get('skills').extend({'Physic', 'Chemistry'})
print(student.get('skills'))

# Get the dictionary keys as a list
list_keys = list(student.keys())
print(list_keys)

# Get the dictionary values as a list
list_values = list(student.values())
print(list_values)

# Change the dictionary to a list of tuples using items() method
student['skills'] = tuple(student['skills'])
set_values_student = set(student.items())
print(set_values_student)

# Delete one of the items in the dictionary
# Delete one of the dictionaries




