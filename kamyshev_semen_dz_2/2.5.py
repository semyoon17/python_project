#функция проверки число целое или нет? спер из инета , признаюсь
def is_int(x):
    temp = str(x)  # конвертируем в str для проверок
    i = 0  # счетчик
    while i < len(temp):
        if temp[i] == '.':  # проверяем является ли целым / узнаем индекс нуля

            while i + 1 < len(temp):  # пробегаемся по индексам после "."
                if temp[i + 1] != '0':  # если после "." не ноль - не Int
                    return False
                i += 1
            else:
                return True
        i += 1
    else:
        return True  # если "." нет - следовательно Int


my_list = [2.53, 28.54, 26, 32.43, 51, 6.32, 84.38, 63.1, 21.06]
print(id(my_list))

for i, n in enumerate(my_list):
    if is_int(n):
        my_list[i] = (f'{n} руб 00 коп')
    else:
        my_list[i] = (f'{int(n*100//100)} руб {int(n*100%100):02d} коп')

#Выводим цены через запятую

print(', '.join(my_list), end='\n')
print(my_list)
# выводим топ 5 цен
sort_list = sorted(my_list, reverse=True)
print(sort_list[:5])
#сортируем по убыванию и доказываем , что айдишник сохранился
my_list.sort()
print(my_list)
print(id(my_list))
