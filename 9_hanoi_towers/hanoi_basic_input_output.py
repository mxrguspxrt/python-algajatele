towers = [ 
    [5, 4, 3, 2, 1],
    [],
    []
]

def solve_puzzle():
    move_from = int(input("Move from index? "))
    move_to = int(input("Move to index? "))
    towers[move_to].append(towers[move_from].pop())

    print(towers)


print(towers)
while True:
    solve_puzzle()