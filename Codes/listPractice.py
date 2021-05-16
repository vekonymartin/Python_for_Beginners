# Task 1 - make two lists the same
list_1 = [43, 70, 25, 39, 15, 85, 42, 94, 11, 76, 20,  36, 48]
list_2 = [ 36, 44, 20, 96, 69, 15, 27, 14, 87, 67, 97, 43,  8, 22]

print(list_1)
print(list_2)

for i in list_1:
    if i not in list_2:
        list_2.append(i)

for i in list_2:
    if i not in list_1:
        list_1.append(i)

list_1.sort()
list_2.sort()

print(list_1)
print(list_2)

# Task 2 - is the list sorted
list_1 = [1,2,3,4]
print(list_1)

sorted = True
index = 0

while sorted and index < len(list_1) - 1:
    if list_1[index] < list_1[index + 1]:
        index += 1
    else:
        sorted = False

if sorted:
    print("The list is sorted.")
else:
    print("The list is not sorted.")

# Task 3 - 100.  Fibonacci number
fibonacci_numbers = [1, 1]

while len(fibonacci_numbers) < 100:
    fibonacci_numbers.append(fibonacci_numbers[len(fibonacci_numbers)-1] + fibonacci_numbers[len(fibonacci_numbers)-2])
print(fibonacci_numbers[99])

a_1 = 1
a_2 = 1
series = [a_1, a_2]
for i in range(98):
    series.append(series[-2]+series[-1])
print(series[-1])

# Task 4 - 400m running result
names = ["Bob", "Wanda", "Jared", "Emma", "Lisa", "Fred", "George", "Noah", "Rachel"]
times = [123.42, 67.15, 80.70, 118.40, 99.95, 68.22, 71.51, 102.68, 80.88]

for i in range(len(times)):
    for j in range(len(times) - 1):
        if times[j] > times[j + 1]:
            times[j], times[j + 1] = times[j + 1], times[j]
            names[j], names[j + 1] = names[j + 1], names[j]

print(names)
print(times)


# Task 5 - the largest number
my_list = [2, 7, 3, 1, 8, 4]

# Artur
my_list.sort()
a = (len(my_list)) - 1
print(my_list[a])

# Boti
a = max(my_list)
print(a)

# Soma
list_my=[5,9,45,4,1,2,7]

for i in range(len(list_my)):
    for j in range(len(list_my) - 1):
        if list_my[j] < list_my[j + 1]:
            list_my[j], list_my[j + 1] = list_my[j + 1], list_my[j]

print(list_my[0])

# Donát
my_list = [2, 7, 3, 1, 8, 4]

largest_number = my_list[0]
for item in my_list:
    if item > largest_number:
        largest_number = item

print(largest_number)

smallest_number = 0
for item in my_list:
    smallest_number += item
for item in my_list:
    if item < smallest_number:
        smallest_number = item
print(smallest_number)

# Task 6 - The second largest number

my_list.sort()
b = my_list[-2]
print(b)

# Traner - The first and the second largest number
my_list = [2, 7, 3, 1, 8, 4]

index = 0
largest_number = my_list[0]

while index < len(my_list):
    if largest_number < my_list[index]:
        largest_number = my_list[index]
        largest_index = index
    index += 1

print(largest_index)
second_largest_number = my_list[0]
index = 0

while index <len(my_list):
    if largest_number != my_list[index] and second_largest_number < my_list[index]:
        second_largest_number = my_list[index]
    index += 1

print(my_list)
diff = largest_number - second_largest_number
largest_number -= diff
my_list[largest_index] = largest_number
my_list.insert(largest_index + 1, diff)
print(my_list)
print("The largest number was " + str(largest_number + diff) + ".\nThe second largest was " + str(second_largest_number) + ".")

# Task 7 - sorting a list
list_to_sort = [41, 4, 13, 43, 30, 22, 11,  5, 38, 92, 36, 33, 35, 26, 85, 95, 68, 56, 62, 55, 75, 73, 42, 88, 54, 64, 78]

# Donát

print('Start: ', list_to_sort)
sorted = False
while not sorted:
    for i in range(len(list_to_sort)-1):
        if list_to_sort[i] > list_to_sort[i+1]:
            temp = list_to_sort[i+1]
            list_to_sort[i+1] = list_to_sort[i]
            list_to_sort[i] = temp
        sorted = True
        for i in range(len(list_to_sort)-1):
            if list_to_sort[i] > list_to_sort[i+1]:
                sorted = False

list_to_sort = list_to_sort
print('Result:', list_to_sort)

list_to_sort = [41, 4, 13, 43, 30, 22, 11,  5, 38, 92, 36, 33, 35, 26, 85, 95, 68, 56, 62, 55, 75, 73, 42, 88, 54, 64, 78]
print(list_to_sort)
sorted = False
while not sorted:
    i = 0
    sorted = True
    while i < len(list_to_sort) - 1:
        if list_to_sort[i] > list_to_sort[i + 1]:
            temp = list_to_sort[i]
            list_to_sort[i] = list_to_sort[i + 1]
            list_to_sort[i + 1] = temp
            sorted = False
        i += 1

print(list_to_sort)


# Task 8 - Your age / day
input_date = input("Give me today's date with this format: e.g. 2021-05-15:\n")
date = input("Give me your birth date with the same format:\n")

day = 0
daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Spliting the text to list element
for i in date:
    born = date.split('-')

date_now = input_date.split('-')

# Converting the list element from string to int
for i in range(len(born)):
    born[i] = int(born[i])

for i in range(len(date_now)):
    date_now[i] = int(date_now[i])

while (not (born[1] == date_now[1] and born[0] == date_now[0] and born[2] == date_now[2])):
    if born[1] == 2 and ((born[0] % 4 == 0 and born[0] % 100 != 0) or born[0] % 400 == 0):
        if born[2] < daysOfMonths[born[1] - 1] + 1:
            born[2] += 1
        else:
            born[1] += 1
            born[2] = 1
    else:
        if born[2] < daysOfMonths[born[1] - 1]:
            born[2] += 1
        else:
            if born[1] == 12:
                born[0] += 1
                born[1] = 1
                born[2] = 1
            else:
                born[1] += 1
                born[2] = 1

    day += 1

print("You are %s days old." % day)