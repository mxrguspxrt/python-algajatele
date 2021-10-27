# Create variable x that has value 3
x = 3

# Create variable y that has value 5
... 

# Create a function plus(a, b) that returns sum of 2 numbers
...

# Create variable z that has return value for plus(x, y)
...

# Make a conditional output - if z is greater than 1000 output "Hello", if smaller output "There"
...

# Make a array of 4 elements: x, y, 1000, z
array_of_4_elements = ...

# Sort numbers in array
sorted_array_of_4_elements = ...

# Make a array of 3 dictonaries - your friends, pets or someone that has: age and name.
characters = [ 
  {"name": "Homer Simpson", "age": 39},
  {"name": "Bart Simpson", "age": 10},
  {"name": "Marge Simpson", "age": 36}
]

# Create a function that returns oldest person from the array of dictionaries
def get_oldest(array_of_dictionaries):
  # Check https://docs.python.org/3/howto/sorting.html (check sorted function with key parameter)
  ...

print("Oldest is:")
print(get_oldest(characters))

# Use append to add yourself to the characters
# https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
me = {"name": "...", "age": 0}
...

# Sort characters by age. Output name of the character who is first in the directionary.
...

# Sort characters by name. Output name of the character who is first in the directionary.
...

# Create a tic-tac-toe game. 1-dimensional or 2-dimensional game map + loop to ask input and redraw map

tick_tac_toe_state = [...]

def game_ongoing(state):
  ...

def print_game_state(state):
  ...

while game_ongoing(tick_tac_toe_state):
  print_game_state(tick_tac_toe_state)
  next_move = int(input("Next move is?"))
