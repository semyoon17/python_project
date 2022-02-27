my_list = []
r = 'процент'
t = 'процента'
k = 'процентов'
for i in range(1, 101):
    my_list.append(i)

print(my_list)

for i in my_list:
    if 21 <= i <= 100 and i % 10 == 1:
        print(f' {i} {r} ')
    elif 21 <= i <= 100 and (i % 10 == 2 or i % 10 == 3 or i % 10 == 4):
        print(f' {i} {t} ')
    elif 21 <= i <= 100 and (i % 10 == 5 or i % 10 == 6 or i % 10 == 7 or i % 10 == 8 or i % 10 == 9):
        print(f' {i} {k} ')
    elif 5 <= i <= 20 or i == 100 or i % 10 == 0:
        print(f' {i} {k} ')
    elif i == 1:
        print(f' {i} {r} ')
    else:
        print(f' {i} {t} ')

