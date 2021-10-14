towers = [ 
    [5, 4, 3, 2, 1],
    [],
    []
]

def solve_puzzle():
    move_from = int(input("Move from index? "))
    move_to = int(input("Move to index? "))

    if len(towers[move_from]) == 0:
        print("Can not make move, because no discs")
        return False

    if len(towers[move_to]) > 0:
        if towers[move_to][len(towers[move_to])-1] < towers[move_from][len(towers[move_from])-1]:
            print("Can not move on top of smaller")
            return False

    towers[move_to].append(towers[move_from].pop())

    print(towers)


print(towers)
while True:
    solve_puzzle()