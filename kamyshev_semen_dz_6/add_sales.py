import sys

with open('sales.txt', 'a', encoding='UTF-8') as f:
    f.write(f'{sys.argv[1]}\n')
exit()