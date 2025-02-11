import json
from typing import Any


def most_spoken_languages():
    with open('./ex_1/countries_data.json', mode='r+', encoding='utf-8') as countries_file:
        ten_countries = dict()
        list_languages: list[dict[str, Any]] = []
        countries_datas: list[dict[str, Any]] = json.load(countries_file)
        existed_languages = {language_name for dict_language in countries_datas for language_name in
                             dict_language.get('languages')}
        print(existed_languages)
