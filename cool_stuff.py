# Trying out generators
def series_generator(low, high):
    while low < high:
        yield low
        low += 1


# for num in series_generator(1, 10):
#     print(num)


def fibonacci_gen(limit = 100):
    num_1 = 0
    num_2 = 1
    count = 0

    while count < limit:
        spit = num_1 + num_2
        yield spit
        num_1 = num_2
        num_2 = spit
        count += 1


for num in fibonacci_gen(10):
    print(num)