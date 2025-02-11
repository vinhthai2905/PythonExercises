import re

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
