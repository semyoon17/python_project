import os

main_dir = 'my_project'
dirs = ['settings', 'mainapp', 'adminapp', 'authapp']

os.mkdir(main_dir)

for i in dirs:
    if not os.path.exists(os.path.join(main_dir, i)):
        os.makedirs(os.path.join(main_dir, i))
