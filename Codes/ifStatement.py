# ==========================================
my_name = "xy"

print("My name is " + my_name)
print("")
# ==========================================
my_age = 34

print("I'm " + str(my_age) + "years old!")
print()
# ==========================================

pet_name = "Mr.Lion"
pet_age = 3
pet_species = "Lion"

print("My first pet called: " + pet_name + " and he is " + str(pet_age) + " years old. He is a " + pet_species)

pet_name = "Mrs.Otter"
pet_age = 9
pet_species = "Otter"

print("My second pet called: " + pet_name + " and he is " + str(pet_age) + "years old. He is a " + pet_species)
print("")
# ==========================================

print("My name is %s"%my_name)
print()

print("Hello! My name is %s and I am %d years old"%(my_name, my_age))
print()
# ==========================================

thing_1 = input("Give me a thing:\n") # card
thing_2 = input("Give me another thing:\n") # desk
adjective = input("Give me an adjective:\n") # beautiful
song_title = input("Give me a song title:\n") # Thinderstruck
celebrity = input("Give me a celebraty name:\n") # Tom Holland
feeling = input("Give me an emotion:\n") # sad
verb = input("Give me a verb:\n") # cook
place = input("Give me a place:\n") # home
food = input("Give me a food:\n") # burger
person = input("Give me a person/name:\n") # Anna


print("""
U just got back from a pizza party with %s.
Can you believe we got to eat %s pizza in %s?!
Everyone got to choose their own toppings.
I made '%s and %s' pizza, which is my favorite!
They even stuffed the crust with %s. How %s!
if That wasn't good enough already, %s was there singing %s.
I was so inspired by the music, I had to get up out of my seat and %s.

""" %(person,adjective,place, food, thing_1, thing_2, feeling, celebrity, song_title, verb))


print("I just got back from a pizza party with " + person +". Can you believe we got to eat " + adjective +
      "\npizza in " + place + "?! Everyone got to choose their own toppings. I made '" + food + " and " + thing_1 +
      "'\npizza, which is my favorite! They even stuffed the crust with " + thing_2 + ". How " + feeling +
      "!\nIf that wasn't good enough already, " + celebrity + " was there singing " + song_title +
      ".\nI was so inspired by the music, I had to get up out of my seat and " + verb + ".")

# ==========================================
#                 STATEMENT
# ==========================================

num = 5
word = "cat"
is_boy = True
is_animal = False

# ==========================================

if num:
    print("It's a number")
if word:
    print("It's a word")
if is_boy:  # is_boy == True
    print("It's a boy")
if is_animal: is_animal: # is_animal == True
    print("It's an animal")
else:
    print("It's not an animal")
print("")

b = 4
a = 5
c = 0
value = b if a > 10 else c
print(value)

b = 11
a = 12
c = 1
value = [c, b][a > 10]
print(value)

# ==========================================
#   region 'region name here'
#   WRITE YOUR CODE.
#   endregion
# ==========================================

# Logic >> AND , OR , NOT, EQUAL
#               &&    ||    !    ==     other language  === -> equal and type

a1 = int(input("Give me a number:\n"))
b1 = int(input("Give me another number:\n"))
if a1 == b1:
    print("They are equal!")
elif a1 > b1:
    print("The first number is bigger.")
else:
    print("The second number is bigger.")
print("")

# ==========================================

point = input("Give me a point:\n")
if int(point) >= 90:
    print("You got an A")
elif int(point) >= 75:
    print("You got an B")
elif int(point) >= 60:
    print("You got an C")
elif int(point) >= 45:
    print("You got an D")
else:
    print("You got an E")

print("")
