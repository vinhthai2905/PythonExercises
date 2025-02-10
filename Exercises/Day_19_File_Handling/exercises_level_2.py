import json
from collections import Counter


def most_spoken_languages():
    with open('./ex_1/countries_data.json', mode='r+', encoding='utf-8') as countries_file:
        countries_datas = json.load(countries_file)

        language_counter = Counter()

        for country in countries_datas:
            languages = country.get('languages', [])
            language_counter.update(languages)

        most_common_languages = language_counter.most_common(10)

        print(language_counter)
        for language, count in most_common_languages:
            print(f'{language}: {count}')


most_spoken_languages()

test = Counter('test')

print(test)