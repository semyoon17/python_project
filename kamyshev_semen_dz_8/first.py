import re


def email_parse(email):
    value = re.split('@', email)
    key = ['username', 'domain']
    if re.search(r'\W', value[1]) is not None:
        mail_dict = {k: v for k, v in zip(key, value)}
        print(mail_dict)
    elif re.search(r"\W", value[1]) is None:
        raise ValueError(f'wrong email: {email}')


email_parse('someone@geekbrains.ru')
