import os

bytes_size = [10 ** i for i in range(2, 6)]

folder = 'D:\\PycharmProjects\\pythonProject\\HW'
files = [getattr(os.stat(f'{folder}\\{item}'), 'st_size')
         for item in os.listdir(folder) if os.path.isfile(f'{folder}\\{item}')]

dict_bytes = {}

for i in files:
    if i < bytes_size[0]:
        dict_bytes_i = {bytes_size[0]: len([i for i in files if i < bytes_size[0]])}
        dict_bytes.update(dict_bytes_i)
for i in files:
    if bytes_size[0] < i <= bytes_size[1]:
        dict_bytes_i = {bytes_size[1]: len([i for i in files if bytes_size[0] < i <= bytes_size[1]])}
        dict_bytes.update(dict_bytes_i)
for i in files:
    if bytes_size[1] < i <= bytes_size[2]:
        dict_bytes_i = {bytes_size[2]: len([i for i in files if bytes_size[1] < i <= bytes_size[2]])}
        dict_bytes.update(dict_bytes_i)

print(dict_bytes)

print(files)
