def num_translate_adv(a):
    list_num = {
        'Null': 'Ноль',
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
        'Ten': 'Десять'
    }
    for key, value in list_num.items():
        if a.islower() and a.capitalize() == key:
            return value.lower()
        elif a == key:
            return value
        else:
            continue


print(num_translate_adv('three'))


