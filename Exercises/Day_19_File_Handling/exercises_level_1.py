import json
from typing import Any
# Write a function which count number of lines and number of words in a text.
# All the files are in the data the folder:
# a) Read obama_speech.txt file and count number of lines and words
with open('./ex_1/donald_speech.txt', mode='r+', encoding='utf-8') as donald_file:
    line_count = 0
    word_count = 0
    list_speech = donald_file.readlines()
    for line in list_speech:
        line_count += 1
        word_count += len(line) - line.count(' ')

    print(f'Line count: {line_count}, Word count: {word_count}')

# b) Read michelle_obama_speech.txt file and count number of lines and words
with open('./ex_1/michelle_obama_speech.txt', mode='r+', encoding='utf-8') as michelle_file:
    line_count = 0
    word_count = 0
    list_speech = michelle_file.readlines()
    for line in list_speech:
        if len(line) - line.count(' ') == 1:
            continue
        else:
            line_count += 1
            word_count += len(line) - line.count(' ')

    print(f'Line count: {line_count}, Word count: {word_count}')
# c) Read donald_speech.txt file and count number of lines and words d)
# Read melina_trump_speech.txt file and count number of lines and words

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

def most_spoken_languages():
    with open('./ex_1/countries_data.json', mode='r+', encoding='utf-8') as countries_file:
        ten_countries = dict()
        existed_languages = list()
        list_languages: list[dict[str, Any]] = []
        countries_datas: list[dict[str, Any]] = json.load(countries_file)

        for dict_country in countries_datas:
            for language in dict_country.get('languages'):
                if language in existed_languages:
                    for existed_lang in list_languages:
                        if language == existed_lang.get('language_name'):
                            existed_lang['used_count'] += 1
                            continue
                else:
                    existed_languages.append(language)
                    list_languages.append({
                        'language_name': language,
                        'used_count': 1
                    })

        return list_languages

list_languages = most_spoken_languages()

print(list_languages)
