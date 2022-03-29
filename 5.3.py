

def get_tuple():
    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена', 'Александр', 'Алексей', 'Марина'
    ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]
    for n, i in enumerate(tutors):
        try:
            yield i,  klasses[n]
        except IndexError:
            yield i, None

    return


a = get_tuple()

for i in a:
    print(i)
print(tuple(a))
