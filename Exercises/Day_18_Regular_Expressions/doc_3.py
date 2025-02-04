import re

names = ['Finn Bindeballe',
        'Geir Anders Berge',
        'HappyCodingRobot',
        'Ron Cromberge',
        'Sohil']

emails = ['vinhthai2905@aol.com',
          'dwdwdw',
          'testing@gmail.com',
          'vinhthai2905@gmail.com']

pattern = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'

pattern_name = r'^\w+\s+\w+$'

test = ''


for email in emails:
    if re.search(pattern, email):
        print(email)


for name in names:
    matched_name = re.search(pattern_name, name)
    if matched_name:
        print(name)
        print(matched_name.group(1))


