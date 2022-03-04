
name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in name_list:
    m = name_list[name_list.index(i)].split()
    up_reg = m[-1].capitalize()
    list_to_str = ''.join([str(elem) for elem in up_reg])
    m[-1] = list_to_str
    k = ' '.join([str(elem) for elem in m])
    name_list[name_list.index(i)] = k


print(name_list)

