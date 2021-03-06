# region Arithmetic op.
#============================
#    Arithmetic operators
#============================

print("--- Arithmetic operators ---")
print(5 + 5)
print(6 - 4)
print(9 * 10)
print(9 / 3)
print(9 / 2)
print(7 % 4)
print(3 ** 3)
print(99 / 4)
print(99 // 4)
print()

# endregion

# region Assignment op.
#============================
#    Assignment operators
#============================

print("--- Assignment operators ---")
num = 8
print(num)
num += 7
print(num)
num -= 6
print(num)
num *= 5
print(num)
num /= 4
print(num)
num **= 2
print(num)
print("")

# endregion

# region Comparison op.
#============================
#    Comparison operators
#============================

print("--- Comparison operators ---")
print(5 < 4)
print(32 > 9)
print(9 == 45)
print(9 * 5 == 45)
print("")

# endregion

# region Identity op.
#============================
#    Identity operators
#============================

print("--- Identity operators ---")
print("5 is 5")
print(5 is 5)
print("8 is 9")
print(8 is 9)
print("6 is \"peach\"")
print(6 is "peach")
print("")

x1 = 5
x2 = 5
x3 = 8
y1 = "random name"
y2 = "random animal"
print(x1 is x2)
print(x1 is x3)
print(x1 is y1)
print(y1 is y1)
print(y1 is y2)
print("")

# endregion

# region Membership op.
#============================
#    Membership operators
#============================

print("--- Membership operators ---")
z1 = 'H'
z2 = 'K'
z3 = "world"
word = "Hello world"
print(z1 in word)
print(z2 in word)
print(z3 in word)

# region

# region Tasks
hyphen = "-"
print(hyphen * 10)
print("TASKS")
print(hyphen * 10)
# region OP in Statement
a1 = 4
a2 = 7
if a1 < a2:
    print(str(a1) + " is smaller than " + str(a2))
if a1 ** a2 == a2 ** a1:
     print(str(a1) + "^" + str(a2) + " equals to " + str(a2) + "^" + str(a1))
if a1 ** a2 != a2 ** a1:
     print(str(a1) + "^" + str(a2) + " not equals to " + str(a2) + "^" + str(a1))
# endregion

# region Email validity
print(hyphen * 10)
address = "manyme@logiscool.com"
if "@" in address and ( address.endswith(".com") or address.endswith(".hu")):
    print("Valid address")
else:
    print("Invalid address")
# endregion

# region Value of a number
print(hyphen * 10)
number = float(input("Enter a number!\n"))
if number >= 0:
    if number == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
# endregion

# region Greater number
print(hyphen * 10)
a = float(input("Enter the first number!\n"))
b = float(input("Enter the second number!\n"))
c = float(input("Enter the third number!\n"))
if a > b:
    if a > c:
        print(str(a) + " is the greatest number.")
    elif c > a:
        print(str(c) + " is the greatest number.")
    else:
        print("There are multiple greatest numbers here.")
elif b > a:
    if b > c:
        print(str(b) + " is the greatest number.")
    elif c > b:
        print(str(c) + " is the greatest number.")
    else:
        print("There are multiple greatest numbers here.")
else:
    print("There are multiple greatest numbers here.")
# endregion

# region Guessing game
print(hyphen * 10)
animal_leg = int(input("Has 2 or 4 legs?"))
animal_fly = input("Can fly?")
animal_swim = input("Can swim?")
if animal_leg == 2:
    if animal_fly.lower == "yes":
        if animal_swim.lower == "yes":
            print("It's an atlantic puffins")
        else:
            print("It's a pidgeon")
    elif animal_fly.lower == "no":
        if animal_swim.lower == "yes":
            print("It's a penguin")
        else:
            print("It's a kiwi")

elif animal_leg == 4:
    if animal_fly.lower == "yes":
        if animal_swim.lower == "yes":
            print("There is no such animal...(except a pegasus)")
        else:
            print("It's a butterfly")
    elif animal_fly.lower == "no":
        if animal_swim.lower == "yes":
            print("It's a horse")
        else:
            print("It's a camel")
# endregion

# endregion

