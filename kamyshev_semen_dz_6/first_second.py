from requests import get
from collections import Counter

# with open('nginx_logs.txt', 'w', encoding='UTF-8') as f:
#     file = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
#     f.write(file.text)
#     f.close()


# def get_info():
#     with open('nginx_logs.txt', 'r', encoding='UTF-8') as k:
#         for line in k:
#             port = line.find('[')
#             way = line.find('GET')
#             path = line.find('/downloads')
#             path_1 = line.find('HTTP')
#             c = line[0:port-5], line[way:way+3], line[path:path_1-1]
#             yield tuple(c)
#
#
#
# a = get_info()

#for i in a:
#    print(i)


def get_spam():
    with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
        spamers = [line[:line.find('[')-5]for line in f]
        max_spam = max(set(spamers), key=spamers.count)
        return max_spam, spamers.count(max_spam)


print(get_spam())
