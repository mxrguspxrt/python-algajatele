age_of_my_dog = int(input("How old is your dog? "))

if (age_of_my_dog > 7): 
  print("Oh, already " + str(age_of_my_dog) + "? It has had an awesome long life! :)")
else:
  print("Oh, only " + str(age_of_my_dog) + "? It's still a puppy!")

def print_that_is_number(n):
  print(str(n) + " is a number")

numbers = [1, 2, 3, 4, 5, 6]
for n in numbers:
  print_that_is_number(n)
