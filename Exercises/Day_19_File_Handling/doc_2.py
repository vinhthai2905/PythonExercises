import json
from math import expm1

from typing_extensions import TextIO

person_2 = b'''{
    "name": "Thai",
    "country": "VietNam",
    "city": "DaNang",
    "skills": ["JavaScrip", "React", "Python"]
}'''

print(type(person_2))


test = r'ddwdwdwdw'

person = '''{
    "name": "Thai",
    "country": "VietNam",
    "city": "DaNang",
    "skills": ["JavaScript", "React", "Python"]
}'''

person_test = {
    "name": "Thai",
    "country": "VietNam",
    "city": "DaNang",
    "skills": ['JavaScript', 'React', 'Python']
}

try:
    dict_person: dict = json.loads(person)
    person_json = json.dumps(dict_person, indent=6)
except Exception as e:
    print(e.__repr__())
else:
    with open('./files/json_test.json', 'w+', encoding='utf-8') as json_file:
        json_file.write(json.dumps(dict_person))
        json_file.seek(0, 0)
        json_file_infos: dict = json.load(json_file)
        print(f'The type of json_file_infos: ', type(json_file_infos))

    print(f'The class of skills in dict_person', type(dict_person.get('skills')))
    for information in dict_person:
        try:
            print(information)
            print(type(information))
        except Exception as e:
            print(e)





