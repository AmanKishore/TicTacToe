from random import randint, choice


def makeBoard(game):  # This function prints out the 2D board that is passed in.
    print('   |   |')
    print(' ' + game[7] + ' | ' + game[8] + ' | ' + game[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + game[4] + ' | ' + game[5] + ' | ' + game[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + game[1] + ' | ' + game[2] + ' | ' + game[3])
    print('   |   |')


def playerLet():  # This function allows the player to choose their letter and returns a list.
    char = ''
    while not (char == 'X' or char == 'O'):
        print('Do you want to be X or O?')
        char = input().upper()
    # First Element is player's letter and second is computer's.
    if char == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def firstTurn():  # This function randomly chooses who goes first.
    if randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def restart():  # This function returns True if yes is entered, otherwise it returns False.
    print('Would you like to play again? (yes or no)')
    return input().lower().startswith('y')


def chooseMove(game, let, space):  # This function assigns where the computer/player wants to move.
    game[space] = let


def win(game, let):  # This function checks if the last move entered results in a victory for that player.
    return ((game[7] == let and game[8] == let and game[9] == let) or  # across the top
            (game[4] == let and game[5] == let and game[6] == let) or  # across the middle
            (game[1] == let and game[2] == let and game[3] == let) or  # across the bottom
            (game[7] == let and game[4] == let and game[1] == let) or  # down the left side
            (game[8] == let and game[5] == let and game[2] == let) or  # down the middle
            (game[9] == let and game[6] == let and game[3] == let) or  # down the right side
            (game[7] == let and game[5] == let and game[3] == let) or  # diagonal
            (game[9] == let and game[5] == let and game[1] == let))    # diagonal


def copyBoard(game):  # This function makes a copy of the tic tac toe board.
    copy = []
    for i in game:
        copy.append(i)
    return copy


def freeSpace(game, space):  # This function checks if the space is empty.
    return game[space] == ' '


def playerMove(game):  # This function allows the player to move.
    space = ' '
    while space not in '1 2 3 4 5 6 7 8 9'.split() or not freeSpace(game, int(space)):
        print('What is your next move? (1-9)')
        space = input()
    return int(space)


def randMove(game, moves):  # This function reandomly chooses a move for the computer.
    possible = []
    for i in moves:
        if freeSpace(game, i):
            possible.append(i)
    if len(possible) != 0:
        return choice(possible)
    else:
        return None


def computerMove(game, computerLet):  # This function is the main computer logic for making a move.
    if computerLet == 'X':
        playerLet = 'O'
    else:
        playerLet = 'X'

    # First, check if there is a move that results in a victory.
    for i in range(1, 10):
        copy = copyBoard(game)
        if freeSpace(copy, i):
            chooseMove(copy, computerLet, i)
            if win(copy, computerLet):
                return i

    # Then, check if the player can win, and try to counteract that.
    for i in range(1, 10):
        copy = copyBoard(game)
        if freeSpace(copy, i):
            chooseMove(copy, playerLet, i)
            if win(copy, playerLet):
                return i

    # Then go for any of the corners.
    move = randMove(game, [1, 3, 7, 9])
    if not move:
        return move

    # If a corner is not free, go in the center.
    if freeSpace(game, 5):
        return 5

    # Otherwise, move on one of the sides
    return randMove(game, [2, 4, 6, 8])


def fullBoard(game):  # This function checks if the board is full.
    for i in range(1, 10):
        if freeSpace(game, i):
            return False
    return True