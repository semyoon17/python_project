import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 560]


def result_func():
    for n, i in enumerate(src):
        if src[n] > src[n-1]:
            yield i


print(list(result_func()))

print(sys.getsizeof(result_func()))

a = list(result_func())
print(sys.getsizeof(a))
