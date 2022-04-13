import os
import shutil

os.mkdir('templates')

for item in os.walk('my_project'):
    for item_s in item:
        if type(item_s) == str and item_s[item_s.find('templates'):] == 'templates':
            shutil.move(f'{item_s}/{str(os.listdir(item_s)[0])}', 'templates')










