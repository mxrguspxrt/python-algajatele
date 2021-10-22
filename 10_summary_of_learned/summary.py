alfabet = ["a", "b", "c", "d", "e", "f", "g", "x", "y"]

def character_that_is_not(to_the_left, to_the_right):
  print("To the left is", to_the_left)
  print("To the right is", to_the_right)
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
      to_the_left = string_as_array[i-1]
      to_the_right = string_as_array[i+1]
      new_char = character_that_is_not(to_the_left, to_the_right)
      new_string.append(new_char)
    i = i + 1
  
  return "".join(new_string)

print(solve_riddle("abc?abc"))