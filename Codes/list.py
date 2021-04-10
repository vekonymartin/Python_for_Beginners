
# Task 1 - create a list with manually added items and print these elements. These elements be random names

names = ["Anna", "Elizabeth", "George", "Tom", "Adam", "Chris"]
print(names)
print(type(names))
print("")

# Task 2 - using the len() function on list
print("The length of your list is: " + str(len(names)))
print("")

# Task 3 - print out the first, last and a chosen element from the list
print(names[0])
print(names[1])
print(names[5])
print("")

# Task 4 - a loop that only ends if we add an existing index in the list
j = len(names)
print("Give an index and i'll show you that item in the list.")
while j > len(names)-1 or j < -len(names):
    j = int(input("Give me a valid index:\n"))
    if j < len(names) and j >= -len(names):
        print(names[j])
    else:
        print("There is no such item in the list.")


# Task 5 - using loop to print each element from the list
i = 0
while i < len(names):
    print(names[i])
    i += 1
print("")

# Task 6 - create a new list and fill it with the first 50 positive integers with a loop
numbers = []
i = 1
while i <= 50:
    numbers.append(i)
    i += 1
print(numbers)

# Task 7 - create a new list, which contains the first 20 odd numbers
odd_numbers = []
even_numbers = []
i = 0
while i < 20:
    if i % 2 == 1:
        odd_numbers.append(i)
    else:
        even_numbers.append(i)
    i += 1
print("Odd numbers: " + str(odd_numbers))
print("Even numbers: " + str(even_numbers))
print("")

# Task 8 - Switch two list elements each other
list_1 = [1,2,3,4,5]
list_2 = [11,23,34,45,57]
print("Before switch: %s" %list_1)
print("Before switch: %s" %list_2)

# region Zsombor and Milán
i = 0
while i < 5:
    temp = list_1[i]
    list_1[i] = list_2[i]
    list_2[i] = temp

    i += 1
    
# endregion

# region Artur and Boti
list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14, 15]
list3 = []

print(list1)
print(list2)

list3 = list1
list1 = list2
list2 = list3

print(list1)
print(list2)


lista = []
listb = []

# 3. solution

lista,listb = listb, lista
# endregion

print("After switch: %s" %list_1)
print("After switch: %s" %list_2)
print("")

# Task 9 - insert items into a list
insertList = []
insertList.insert(1,0)
insertList.insert(10,1)
insertList.insert(5,2)
print(insertList)

# Task 10 - deleting items from a list
girl_names = ["Anne", "Elizabeth", "Elon", "Sophie", "Hannah"]
boy_names = ["Thomas", "George", "Rick", "Olivia", "Noah"]
print(girl_names)
print(boy_names)
girl_names.pop(2)
boy_names.remove("Olivia")
print(girl_names)
print(boy_names)

# Task 11 - sum of items
numberList = [1,40,523,6851,0,346,321,8,1,457,123]
i = 0
sum = 0
while i < len(numberList):
    sum += numberList[i]
    i += 1
print(sum)

# Task 12 - occurencies in the list
repeatList = [1, 0, 1, 2, 0, 2, 2, 1, 0, 1, 2, 1, 1, 1, 0]
i = 0
occunences = 0
value = int(input("What value are we looking for?\n"))
while i < len(repeatList):
    if repeatList[i] == value:
        occunences += 1
    i += 1
print("The number " + str(value) + " appears " + str(occunences) + " times in the list.")
