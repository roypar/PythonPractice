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

# Library catalog
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


filteredClassic = filter(filterClassic, input_with_key)
names = [sample[0]['name'] for sample in filteredClassic]
print(names)
