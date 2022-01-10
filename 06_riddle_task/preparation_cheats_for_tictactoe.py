tick_tac_toe_state = [
    "", "", "",
    "", "", "",
    "", "", ""
]

def game_ongoing(state):
  s = state
  if s[0] != "" and s[0] == s[3] == s[6]:
      print("X won")
      return False
  return True

def print_game_state(state):
  s = state 
  print(s[0] + " | " + s[1] + " | " + s[2])
  print("-------")
  print(s[3] + " | " + s[4] + " | " + s[5])
  print("-------")
  print(s[6] + " | " + s[7] + " | " + s[8])

next_is_x = True
while game_ongoing(tick_tac_toe_state):
  print_game_state(tick_tac_toe_state)
  next_move = int(input("Next move is?"))
  tick_tac_toe_state[next_move] = next_is_x and "X" or "O"
  next_is_x = not next_is_x
