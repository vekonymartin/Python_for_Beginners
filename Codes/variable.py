#========================================================
#                       VARIABLES
#========================================================
# Task 1 - creating a person
firstname = "Handsome"
lastname = "Boy"
age = 7
jobtype = "Junior programmer"
gender = "boy"
country = "Hungary"
born_in = "Budapest"
weight = 50  # calculating as kg

print(firstname)
print(lastname)
print(age)
print(jobtype)
print(weight)
#========================================================

# Task 2 - creating a pet as well
pet_1_name = "Winston"
pet_1_age = 2
pet_1_species = "dog"
pet_1_gender = "female"
pet_1_born_in = "New York"
pet_1_weight = 31.7 # calculating as kg

print(pet_1_name)
print(pet_1_age)
print(pet_1_species)
print(pet_1_weight)
#========================================================

# Task 3 - changes these variables values - change the type of the variable
pet_1_age = 3
pet_1_weight = 32.2
age = 8
jobtype = "Senior programmer"
weight = 48.4

print(pet_1_age)
print(jobtype)
print(weight)
#========================================================

x = y = z = "Orange"
print(x)
print(y)
print(z)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z = x + y
print(z)

x = 5
y = 10
print(x + y)
#========================================================

# Task 4 - print the type of a variable
print(type(jobtype))
print(type(weight))
print(type(age))
#========================================================

# Task 5 - Converting variables
# int to float
print(age)
print(float(age))

print(weight)
print(int(weight))

# string to int -> not working if we want to print the data -> print() is always return a string type
#print(int(jobtype))

#========================================================
# Tasks:
# 1. SHOW VARIABLE'S DATA
name = input('Name: ')
age = input('Age: ')
print(f'Hi, my name is {name} and I am {age} years old.')

# 2. CALCULATOR
num_1 = int(input("What is the first number?\n"))
num_2 = int(input("What is the second number?\n"))
print("The sum of numbers is: " + str(num_1+num_2))
print("The difference of numbers is: " + str(num_1-num_2))
print("The ratio of numbers is: " + str(num_1/num_2))
print("The product of numbers is: " + str(num_1*num_2))

# 3. MOUNTAIN
mountain = "/\\"
print(mountain * 8)

# 4. CIRCLE'S DISTRICT/AREA
radius = float(input("What is the radius of the circle?\n"))
print("The area of the circle is: " + str(radius**2*3.14))
print("The perimeter of the circle is: " + str(radius*2*3.14))

# 5. SUM THE VALUE
number = int(input("Add an integer:\n"))
print("The a+aa+aaa number is:\n" + str(int(number) + 11*int(number) + 111*int(number)))

number_2 = int(input("Input an integer : "))
n1 = int( "%s" % number_2 )
n2 = int( "%s%s" % (number_2,number_2) )
n3 = int( "%s%s%s" % (number_2,number_2,number_2) )
print("The a+aa+aaa number is:\n" + str(n1+n2+n3))







