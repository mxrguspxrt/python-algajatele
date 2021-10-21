empty_square = " "

squares = [
  empty_square, empty_square, empty_square,
  empty_square, empty_square, empty_square,
  empty_square, empty_square, empty_square
]

def print_tic_tac_toe_table():
  print(squares[0] + " | " + squares[1] + " | " + squares[2])
  print("----------")
  print(squares[3] + " | " + squares[4] + " | " + squares[5])
  print("----------")
  print(squares[6] + " | " + squares[7] + " | " + squares[8])

def ask_move_to_make(x_or_y):
  move_to_make = input("Kuhu soovid lisada " + x_or_y + "?: ")

  move_to_make_int = int(move_to_make) - 1

  if squares[move_to_make_int] != empty_square:
    print("Cant make move, because already contains: " + squares[0])
    return False
  else:
    squares[move_to_make_int] = x_or_y
    return True


while True:
  while not ask_move_to_make("X"):
    print_tic_tac_toe_table()
  print_tic_tac_toe_table()
  while not ask_move_to_make("Y"):
    print_tic_tac_toe_table()
  print_tic_tac_toe_table()

