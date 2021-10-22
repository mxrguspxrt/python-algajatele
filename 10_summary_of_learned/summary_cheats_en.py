a = int(input("Please type first number: "))
b = int(input("Please type second number: "))
print(a + b)


print("Please choose your calculator: ")
print("a. normal calculator")
print("b. tax calculator")
calculator_choice = input()





# + - * /
if calculator_choice == "a":
  a = int(input("Please type first number: "))
  b = int(input("Please type second number: "))
  operation = input("What operations you want to do (+ - * /): ")

  if operation == "+":
    print(a + b)

  if operation == "-":
    print(a - b)

  if operation == "*":
    print(a * b)

  if operation == "/":
    print(a / b)

if calculator_choice == "b":
  salary = int(input("Please input salary: "))
  profit_tax = 0.2
  for_goverment = salary * profit_tax
  to_bank_for_employee  = salary - for_goverment
  print("Tax is: ", profit_tax)
  print("To goverement: ", for_goverment)
  print("To bank for employee: ", to_bank_for_employee)


def normal_calculator():
  a = int(input("Please type first number: "))
  b = int(input("Please type second number: "))
  operation = input("What operations you want to do (+ - * /): ")

  if operation == "+":
    print(a + b)

  if operation == "-":
    print(a - b)

  if operation == "*":
    print(a * b)

  if operation == "/":
    print(a / b)

def tax_calculator():
  salary = int(input("Please input salary: "))
  profit_tax = 0.2
  for_goverment = salary * profit_tax
  to_bank_for_employee  = salary - for_goverment
  print("Tax is: ", profit_tax)
  print("To goverement: ", for_goverment)
  print("To bank for employee: ", to_bank_for_employee)


while True:
  # + - * /
  print("\n\nPlease choose your calculator: ")
  print("a. normal calculator")
  print("b. tax calculator")
  calculator_choice = input()

  if calculator_choice == "a":
    normal_calculator()

  if calculator_choice == "b":
    tax_calculator()







    square1 = " "
square2 = " "
square3 = " "
square4 = " "
square5 = " "
square6 = " "
square7 = " "
square8 = " "
square9 = " "

def print_tic_tac_toe_table():
  print(square1 + " | " +  square2 + " | " + square3)
  print("----------")
  print(square4 + " | " + square5 + " | " + square6)
  print("----------")
  print(square7 + " | " + square8 + " | " + square9)

def get_x_position():
  where_to_add_x = input("Where to add X: ")
  if where_to_add_x == "1":
    square1 = "X"
  if where_to_add_x == "2":
    square2 = "X"
  if where_to_add_x == "3":
    square3 = "X"
  if where_to_add_x == "4":
    square4 = "X"
  if where_to_add_x == "5":
    square5 = "X"
  if where_to_add_x == "6":
    square6 = "X"
  if where_to_add_x == "7":
    square7 = "X"
  if where_to_add_x == "8":
    square8 = "X"
  if where_to_add_x == "9":
    square9 = "X"

def get_y_position():
  where_to_add_y = input("Where to add Y: ")
  if where_to_add_y == "1":
    square1 = "Y"
  if where_to_add_y == "2":
    square2 = "Y"
  if where_to_add_y == "3":
    square3 = "Y"
  if where_to_add_y == "4":
    square4 = "Y"
  if where_to_add_y == "5":
    square5 = "Y"
  if where_to_add_y == "6":
    square6 = "Y"
  if where_to_add_y == "7":
    square7 = "Y"
  if where_to_add_y == "8":
    square8 = "Y"
  if where_to_add_y == "9":
    square9 = "Y"

while True:
  get_x_position()

  print_tic_tac_toe_table()

  get_y_position()

  print_tic_tac_toe_table()





squares = [ 
  " ", " ", " ",
  " ", " ", " ",
  " ", " ", " "
]

def check_game_is_finished():
  if squares[0] != " " and squares[0] == squares[1] == squares[2]:
    print("Game over and person won: ", squares[0])
    return True

def print_tic_tac_toe_table():
  print(squares[0] + " | " +  squares[1] + " | " + squares[2])
  print("----------")
  print(squares[3] + " | " + squares[4] + " | " + squares[5])
  print("----------")
  print(squares[6] + " | " + squares[7] + " | " + squares[8])

def get_position(x_or_y):
  print_tic_tac_toe_table()
  where_to_add_x_or_y = int(input("Where to add "+x_or_y+": "))
  
  if squares[where_to_add_x_or_y-1] == " ":
    squares[where_to_add_x_or_y-1] = x_or_y
  else: 
    print("Cant do this move")
    get_position(x_or_y)


while True:
  get_position("X")
  if check_game_is_finished():
    break
  get_position("Y")
  if check_game_is_finished():
    break







pet_names = ["Tupsu", "Milli", "Nessi", "Trish"]
pet_types = ["dog", "dog", "dog", "cat"]
pet_ages = [10, 15, 6, 2]

pet_ages[0] = 11

# How many cats we have in our animal clinic?
we_have_cats_count = 0
for pet_type in pet_types: 
  if pet_type == "cat":
    we_have_cats_count = we_have_cats_count + 1

print("We have N cats in our clinic: ", we_have_cats_count)
print("and its of our customers", (we_have_cats_count/len(pet_types))*100, "%")










pets = [ 
  {"name": "Tupsu", "type": "dog", "age": 10},
  {"name": "Milli", "type": "dog", "age": 15},
  {"name": "Nessi", "type": "dog", "age": 6},
  {"name": "Trish", "type": "dog", "age": 2}
]


pets[0]["age"] = 11

print("Our all customers are:")
print("Name \tType \tAge")

for pet in pets:
  print(pet["name"], " \t", pet["type"], " \t", pet["age"])





string = "abx?def"

string_as_array = list(string)

for char in string_as_array:
  if char != "?":
    print(char)
  else: 
    print("x")



# This task is to introduce arrays/strings/conditions in Python. Also some logical thinking.

# Each of the ? must be replaced with a char, that is unique (so can't be same as on left or right).

alfabet = ["a", "b", "c", "d", "e", "f", "g", "x", "y"]

def character_that_is_not(to_the_left, to_the_right):
  for char in alfabet:
    if char != to_the_left and char != to_the_right:
      return char

def solve_riddle(string):
  string_as_array = list(string)
  new_string = []

  i = 0
  for char in string_as_array:
    if char != "?":
      new_string.append(char)
    else: 
      to_the_left = get_to_left_char(new_string, i)
      to_the_right = get_to_right_char(string_as_array, i)
      new_char = character_that_is_not(to_the_left, to_the_right)
      new_string.append(new_char)
    i = i + 1
  
  return "".join(new_string)

def get_to_left_char(string_as_array, i):
  if i == 0:
    return None 
  else: 
    return string_as_array[i-1]

def get_to_right_char(string_as_array, i):
  if i == len(string_as_array) - 1:
    return None 
  else: 
    return string_as_array[i+1]

def run_tests():
  is_correct_solution(solve_riddle("abc?def"))
  is_correct_solution(solve_riddle("abc?de?????"))
  is_correct_solution(solve_riddle("??????"))

def is_correct_solution(solved_str):
  print("Checking solution: ", solved_str)
  if "?" in solved_str:
    raise RuntimeError("Solution can't contain ?, but was '" + solved_str + "'")
  
  for i in range(len(solved_str)-1):
    if solved_str[i] == solved_str[i+1]:
      raise RuntimeError("Solution can't contain 2 same chars next to eachother, but was '" + solved_str + "'")

run_tests()      