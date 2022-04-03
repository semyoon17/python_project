import sys

with open('sales.txt', 'r', encoding='UTF-8') as f:
    sales = f.readlines()
    try:
        if len(sys.argv) == 1:
            for line in sales:
                print(line)
        elif len(sys.argv) == 2:
            print(*sales[int(sys.argv[1]):])
        elif len(sys.argv) == 3:
            print(*sales[int(sys.argv[1])-1:int(sys.argv[2])])
        elif len(sys.argv) >= 4:
            print('Введи не больше 2 значений')
    except ValueError:
        print('Принимаются только числовые значения')




