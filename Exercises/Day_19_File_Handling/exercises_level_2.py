import json
import re
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

# 4 Extract all incoming email addresses as a list from the email_exchange_big.txt file.
try:
    with open('./ex_2/email_exchange.txt', encoding='utf=8') as email_file:
        email_pattern = r'\w+@\w+(\.\w+)+$'
        list_emails = []
        lines = email_file.readlines()
        for line in lines:
            if len(line) == 1:
                continue
            else:
                if re.search(email_pattern, line):
                    email = re.search(email_pattern, line)
                    list_emails.append(email.group())
except Exception as e:
    print(e.__repr__())

set_emails = set(list_emails)
print(set_emails)

# 5 Find the most common words in the English language.
# Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words.
# Your function will return an array of tuples in descending order. Check the output