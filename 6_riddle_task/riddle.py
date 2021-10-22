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