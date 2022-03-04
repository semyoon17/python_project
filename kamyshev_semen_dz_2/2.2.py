my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, n in enumerate(my_list):
    if n.isdigit():
        my_list[i] = (f'"{int(n):02d}"')
    elif n[1:].isdigit():
        my_list[i] = (f'"{n[0]}{int(n[1:]):02d}"')

my_list_new = ' '.join(my_list)

print(my_list_new)
