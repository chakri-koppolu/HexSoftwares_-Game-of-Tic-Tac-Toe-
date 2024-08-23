import random

boxes = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
HUMAN = 'X'
COMPUTER = 'O'
turn = 1
winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def print_board(boxes):
    print('''
             {} | {} | {} 
            -----------
             {} | {} | {}
            -----------
             {} | {} | {} 
        '''.format(*boxes))

def take_turn(player):
    if player == COMPUTER:
        box = get_computer_move()
        boxes[box] = player
        print('Computer places its \'{}\' in box {}'.format(player, box + 1))
    else:
        while True:
            box = input('Player {}, type a number from 1-9 to select a box: '.format(player))
            try:
                box = int(box) - 1
            except ValueError:
                print("That's not a valid number, try again.\n")
                continue
            if box < 0 or box > 8:
                print('That number is out of range, try again.\n')
                continue
            if boxes[box] == ' ':
                boxes[box] = player
                break
            else:
                print('That box is already marked, try again.\n')

def get_computer_move():
    while True:
        box = random.randint(0, 8)
        if boxes[box] == ' ':
            return box

def check_for_win(player):
    for combo in winning_combos:
        score = 0
        for index in combo:
            if boxes[index] == player:
                score += 1
        if score == 3:
            return True
    return False

def play():
    current_player = HUMAN
    while True:
        print_board(boxes)
        take_turn(current_player)
        if check_for_win(current_player):
            print_board(boxes)
            print('Game over. {} wins!\n'.format(current_player))
            break
        elif ' ' not in boxes:
            print_board(boxes)
            print('Game over. It\'s a tie.\n')
            break
        current_player = COMPUTER if current_player == HUMAN else HUMAN
        global turn
        turn += 1

print('\n\nWelcome to Tic Tac Toe for human vs computer!')
print_board(range(1, 10))
play()