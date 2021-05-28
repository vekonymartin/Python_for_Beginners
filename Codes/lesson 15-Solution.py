# Task 1 - print the poem
print("""I wandered lonely as a cloud
That floats on high o’er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
\tBeside the lake, beneath the trees,
\tFluttering and dancing in the breeze.""")

# Task 2 - volume of a cone
radius = int(input("What is the radius of the circle?\n"))
height = int(input("What is the height of the cone?\n"))
volume = (radius ** 2 * 3.14) * height / 3
print("The volume of the cone is", volume, "units.")

# Task 3 - swap variables in two different ways
a = 10
b = 20
# option 1
a, b = b, a
# option 2
temp = a
a = b
b = temp

# Task 4 - string to list to integers
numbers = input("Give me a series of numbers:\n")
numbers_list = numbers.split(",")
for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
print(numbers_list)

# Task 5 - make two list from one
list_1 = [4, 8, 15, 16, 23, 42]
i = 0
list_2 = []
list_3 = []
while i < len(list_1):
    if i % 2 == 0:
        list_2.append(list_1[i])
    else:
        list_3.append(list_1[i])
    i += 1
print(list_2)
print(list_3)

# Task 6 - most popular fruit
items = ["strawberry", "grape", "apple", "orange", "watermelon", "banana", "lemon", "avocado", "other"]
popularity = [15, 17, 16, 10, 9, 18, 7, 5, 3]
number_one = items[0]
for i in range(len(popularity)-1):
    if popularity[i+1] > popularity[i]:
        number_one = items[i+1]
print("The most popular fruit is", number_one)

# Task 7 - modulo 7
numbers = [61, 70, 12, 34, 76, 94, 26, 93, 10, 1, 90, 71, 32, 89, 97, 41, 95, 6, 18, 20, 73, 46, 21, 31, 72, 22]
print(numbers)
mod_7 = False
while not mod_7:
    mod_7 = True
    for i in range(len(numbers)):
        if numbers[i] % 7 != 0:
            numbers[i] += 1
            mod_7 = False
print(numbers)

# Task 8 - number of vowels
text = "The way to get started is to quit talking and begin doing."
print(text)
vowels = "aeiou"
number_of_vowels = 0
for i in text:
    if i in vowels:
        number_of_vowels += 1
print("There are", number_of_vowels, "vowels in this text.")

# Task 9 - sum of first n integers
n = int(input("How many numbers you want to sum?\n"))
sum = 0
for i in range(n+1):
    sum += i
print("The sum of the first", n, "integers is", sum)

# Task 10 - cows and bulls/ master mind
puzzle = "3618"
tips = 0
isPlaying = True
while isPlaying:
    cows = 0
    bulls = 0
    tip = input("Tip a four digits number:\n")
    for i in range(len(tip)):
        if tip[i] == puzzle[i]:
            cows += 1
        elif tip[i] in puzzle:
            bulls += 1
    tips += 1
    if cows == 4:
        isPlaying = False
    else:
        print("cows: " + str(cows))
        print("bulls: " + str(bulls))
print("Well done. The number was", puzzle,". You got it in", tips, "tips.")

# Task 11 - finding anagrams
word_1 = "Amy"
word_2 = "May"
if len(word_1) == len(word_2):
    if sorted(word_1.lower()) == sorted(word_2.lower()):
        print("These are anagrams.")
    else:
        print("These are not anagrams.")
else:
    print("These are not anagrams.")