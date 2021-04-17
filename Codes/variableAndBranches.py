# Task 1 - hangman game

puzzle = "computer science"
my_solution = "******** *******"
life = 10
correct_letters = []
incorrect_letters = []
while life > 0 and puzzle != my_solution:
    print(my_solution)
    tip = input("Tip a new letter:\n")
    if len(tip) == len(puzzle):
        temp = my_solution
        my_solution = tip
        print("You try to guess the solution...and your guess is...")
        if my_solution == puzzle:
            print("Correct.")
        else:
            print("Not correct.")
            life -= 1
            print("This isn't in the puzzle. " + str(life) + " lives left.")
            my_solution = temp
    else:
        found_something = False
        for i in range(len(puzzle)):
            if puzzle[i] == tip:
                my_solution_list = list(my_solution)
                my_solution_list[i] = tip
                my_solution = "".join(my_solution_list)
                found_something = True
        if not found_something:
            incorrect_letters.append(tip)
            life -= 1
            print("This isn't in the puzzle. " + str(life) + " lives left.")
        else:
            correct_letters.append(tip)
        print("List of correct letters: " + str(correct_letters))
        print("List of incorrect letters: " + str(incorrect_letters))
if life > 0:
    print("Congratulations!")
else:
    print("Maybe next time..\n")

# Task 2 - find quadrant based on coordinates
x_pos = int(input("What is the x position?\n"))
y_pos = int(input("What is the y position?\n"))
if x_pos >=0:
    if y_pos >=0:
        print("The coordinate point is in the first quadrant.")
    else:
        print("The coordinate point is in the fourth quadrant.")
else:
    if y_pos >=0:
        print("The coordinate point is in the second quadrant.")
    else:
        print("The coordinate point is in the third quadrant.")

# Task 3 - greatest common divisor
number_1 = int(input("What is the first number?\n"))
number_2 = int(input("What is the second number?\n"))
gcd = 1
for i in range(1,number_1+1):
    if number_1 % i == 0 and number_2 % i == 0:
        gcd = i
print("The greatest common divisor of " + str(number_1) + " and " + str(number_2) + " is " + str(gcd) + ".")

# Task 4 - prime factors of a number
number = int(input("Give me a number:\n"))
i = 2
prime_factors = []
while number > 1:
    while number % i == 0:
        number /= i
        prime_factors.append(i)
    i += 1
print(prime_factors)

# Task 5 - least common multiple - without finding all the prime factors
num_1 = int(input("What is the first number?\n"))
num_2 = int(input("What is the second number?\n"))
if num_1 > num_2:
    lcm = num_1
else:
    lcm = num_2
while not (lcm % num_1 == 0 and lcm % num_2 == 0):
    lcm += 1
print("The least common miltiple of " + str(num_1) + " and " + str(num_2) + " is " + str(lcm) + ".")

# Task 6 - binary numbers
bin(42)
type(bin(42))
bin(42)[2:]
int(bin(42)[2:])

# Task 7 - solving equations with quadratic formula - ax^2+bx+c
print("You have the following equation: ax^2+bx+c = 0\n "
      "Tell me the a,b,c, parameters and i'll tell you the possible x values.")
a = int(input("What is the value of a?\n"))
b = int(input("What is the value of b?\n"))
c = int(input("What is the value of c?\n"))
if b**2-4*a*c > 0:
    x_1 = (-b + (b ** 2 - 4 * a * c) ** 1 / 2) / (2 * a)
    x_2 = (-b - (b ** 2 - 4 * a * c) ** 1 / 2) / (2 * a)
    print("The roots of the equation are: " + str(x_1) + " and " + str(x_2) + ".")
elif b**2-4*a*c < 0:
    print("The equation has no real roots.")
else:
    x_1 = (-b + (b ** 2 - 4 * a * c) ** 1 / 2) / (2 * a)
    print("There is only one root which is: " + str(x_1) + ".")
