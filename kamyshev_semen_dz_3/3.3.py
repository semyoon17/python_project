def thesaurus(names):
    names_dict = {}
    for i, s in enumerate(names):
        if s.startswith(s[0]):
            same_names = list(filter(lambda el: el.startswith(s[0]), names))
            names_dict_i = {s[0]: same_names}
            names_dict.update(names_dict_i)
    return names_dict


list_names = ['Марина', 'Катя', 'Карина', 'Маша', 'Ангелина', 'Андрей']

print(thesaurus(list_names))

