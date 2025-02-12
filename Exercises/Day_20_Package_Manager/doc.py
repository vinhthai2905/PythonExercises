from typing import Any

import requests
import json

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

response_data = requests.get(url)

session = requests.Session()

r = requests.post('https://httpbin.org/post', data={'key': 'value'})

print(f'This is response: { response_data}')
print(f'This is response status code: {response_data.status_code}')
print(f'This is response header: {response_data.headers}')

github_datas_response = session.get('https://api.github.com/events')

print(type(github_datas_response.text))

print(f'This is Git responses: {json.dumps(github_datas_response.json()[0:1], indent=4)}')


list_test: list[dict[Any, Any]] = github_datas_response.json()
for item in list_test[0:1]:
    print(type(item))

try:
    list_dicts_github: list[dict[Any, Any]] = github_datas_response.json()
except Exception as e:
    print(e.__repr__())
else:
    with(open('./Json_Files/github.json', 'w+', encoding='utf-8')) as json_file:
            json_file.write(json.dumps(list_dicts_github, indent=4))


