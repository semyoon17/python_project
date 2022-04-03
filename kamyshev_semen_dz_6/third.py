with open('users.csv', 'r', encoding='UTF-8') as users, open('hobby.csv', 'r', encoding='UTF-8') as hobbies:
    my_dict = {}
    name = users.read().splitlines()
    hobby = hobbies.read().splitlines()
    if len(name) < len(hobby):
        print(1)
    else:
        for n, i in enumerate(name):
            try:
                new_item = {i: hobby[n]}
                my_dict.update(new_item)
            except IndexError:
                new_item = {i: None}
                my_dict.update(new_item)
        with open('dict.txt', 'w', encoding='UTF-8') as dict_d:
            dict_d.write(str(my_dict))


print(my_dict)
