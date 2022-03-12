import random


def get_jokes(n):
    # Список, в который будем добавлять сформированные шутки
    list_jokes = []
    for i in range(n):
        # Джойним случайно выбранные элементы списка в один элемент нового списка
        joke = ' '.join([random.choice(nouns), random.choice(adverbs), random.choice(adjectives)])
        # добывляем новый элемент в целевой список
        list_jokes.append(joke)
    print(list_jokes)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
get_jokes(5)






