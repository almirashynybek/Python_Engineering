row = 3
column = 3 


def greeting():
    print('Welcome to the game!')
    print('----------------------------')
    

def boarder(row):
    for line in range(row):
        print(" | ".join(line))
        print("-" * 10)
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)
              
def player_input():
    n = int(input(f'Ход игрока Х. Введите число от 1 до 9: '))

greeting()
boarder()
player_input()

def position(n):
    for i in range(row):
        for j in range(column):
            if i == n:
                print(f'   |   | {n} ')




x = [
    ['x', '', 'o'],
    ['x', '', 'o'],
    ['o', 'x', 'o']
]

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

print(print_board(x))