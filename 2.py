
my_list = []

for i in range(1, 1000):
    if i % 2 != 0:
        my_list.append(i**3 + 17)
print(my_list)

my_list_1 = []


def sum_of_digits(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s


for k in my_list:
    if sum_of_digits(k) % 7 == 0:
        my_list_1.append(k)

print(my_list_1)
print(sum(my_list_1))


