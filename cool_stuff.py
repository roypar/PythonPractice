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


# for num in fibonacci_gen(10):
#     print(num)


# List of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


# function that filters vowels
def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if letter in vowels:
        return True
    else:
        return False


# filteredVowels = list(filter(filterVowels, letters))
# print(filteredVowels)

# Dictionary filtering
classics = [
    {"name": "The Avengers", "year": 1999},
    {"name": "The Inglorious", "year": 2000},
    {"name": "Fantastic Five", "year": 1995},
    {"name": "Avenging Heros", "year": 2005},
    {"name": "Unwanted Heroism", "year": 2000},
]

key_word = 'hero'
input_with_key = [[entry, key_word] for entry in classics]


def filterClassic(sample):
    if sample[1].lower() in sample[0]['name'].lower():
        return True
    else:
        return False


# filteredClassic = filter(filterClassic, input_with_key)
# names = [sample[0]['name'] for sample in filteredClassic]
# print(names)


#Map function trials
def my_func(x, y):
    return x**2+y**2

x_vals = [1,2,3,4,5]
y_vals = [4,2,6,1,3]

output = map(my_func, x_vals, y_vals)
output_2 = map(lambda x,y: x**3+y**3, x_vals, y_vals)

# print(list(output))
# print(list(output_2))

#Reduce function trials
import functools

annual_rets = [1,5.2,-1.3,4.8,10.2,-50,50,25.3]
# annual_rets = [1,10,10]
final_ret = functools.reduce(lambda x,y:x*(1+y/100),annual_rets)-1
print(final_ret)