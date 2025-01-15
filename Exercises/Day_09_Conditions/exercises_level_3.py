person = {
    'first_name': 'Vinh',
    'last_name': 'Thai',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if person.__contains__('skills'):
    print(f'The middle skill: {person.get('skills')[len(person.get('skills')) // 2]}')
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person.keys():
    if 'Python' in person.get('skills'):
        index = person.get('skills').index('Python')
        print(f'Here is the result in skills list: {person.get('skills')[index]}')

#  * If a person skills has only JavaScript and React,
if person.get('skills') == ['Javascript', 'React']:
    print('He is a front-end developer.')

#  print('He is a front end developer'), if the person skills has Node, Python, MongoDB,
required_skills = ['Node', 'Python', 'MongoDB']
person_skills = person.get('skills', [])

test = list(filter(lambda skill: skill in required_skills, person_skills))
print(test)

if [skill for skill in person.get('skills') if skill in required_skills] == ['Node', 'Python', 'MongoDB']:
    print('He is a front-end developer.')

if filter(lambda skill: skill in person_skills, required_skills) == ['Node', 'Python', 'MongoDB']:
    print('He is a front-end developer.')

if person.get('is_married') == True and person.get('country') == 'England':
    print(f'{person.get('name')} lives in {person.get('country')}. He is married.')


#  print('He is a backend developer'), if the person skills has React, Node and MongoDB,
#  Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

