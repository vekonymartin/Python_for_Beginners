# Task 1 - print number using for loop
for i in range(10):
    print(i)

# Task 2 - print positive number using for loop
for i in range(1,11):
    print(i)

# Task 3 - print even number using for loop
for i in range(2,100,2):
    print(i)

# Task 4 - for loop on strings
for i in "Hello World!":
    print(i)

# Task 5 - multiplication table
num = int(input("Give me a number and i'll show you its multiplication table: "))
for i in range(1,11,1):
    print(str(i) + " * " + str(num) + " = " + str(i*num))

# Task 6 - decryption with for loop
encrypted_message = "Wyh earne  eclaenp hIa nbtu?"
decrypted_message = ""
for i in range(0,len(encrypted_message)):
    if i % 2 == 0:
        decrypted_message += encrypted_message[i]
for i in range(0,len(encrypted_message)):
    if i % 2 == 1:
        decrypted_message += encrypted_message[i]
print(encrypted_message)
print(decrypted_message)

# Task 7 - encryption with for loop
new_decrypted_message = "Hello, my name is George and I am 17 years old"
print(new_decrypted_message)
first_half = new_decrypted_message[:(len(new_decrypted_message)+1)//2]
second_half = new_decrypted_message[(len(new_decrypted_message)+1)//2:]
new_encrypted_message = ""
for i in range((len(new_decrypted_message)+1)//2):
    new_encrypted_message += first_half[i]
    if i < len(second_half):
        new_encrypted_message += second_half[i]
print(new_encrypted_message)


# Task 8 - Generating numbers with for loop and add them to a list
list_1 = []
for i in range(50):
    list_1.append(i)
print(list_1)
print("")


# Task 9 - Generate numbers with for loop which start with 9 to 99
list_1 = []
for j in range(9, 99):
    list_1.append(j)
print(list_1)
print("")

# Task 10 - Generate numbers with for loop from 7 to -20
list_1 = []
for k in range(7, -20, -1):
    list_1.append(k)
print(list_1)
print("")

# Task 11 - Check that a given name is in the list with for loop
names = ["Anna", "David", "George", "Alex", "Felix", "Mike"]
chosen_name = input("Give me a name:\n")
in_the_list = False
for item in names:
    if chosen_name.lower() == item.lower():
        in_the_list = True

if in_the_list:
    print("Yes! This name is in the list!")
else:
    print("No, this name is NOT in the list...")
print("")

# Task 12 - generate multiplaction tables and print them one by one
numbers = []
for i in range(1,11):
    for j in range(1,11):
        numbers.append(i*j)
print(numbers)
j = 0
for i in range(11):
    print(numbers[i*10:(i*10)+10])
    j += 1
print("")
