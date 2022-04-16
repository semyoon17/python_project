def type_logger(func):
    def type_log(*args):
        for i in args:
            k = {i: type(i)}
            yield k, type(k)
    return type_log

# @type_logger
def calc_cube(*args):
    for i in args:
        n = i**3
        yield n, type(n)



print(*calc_cube(3.2 , 4, 4))
