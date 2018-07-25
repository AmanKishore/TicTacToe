# Tic Tac Toe inspired by inventwithpython
from game.methods import makeBoard, playerLet, firstTurn, restart, chooseMove, win, computerMove, fullBoard, playerMove

print('Tic Tac Toe the game!')  # This is the main tic tac toe game.
while True:
    game = [' '] * 10  # Start with a clean board.
    player, computer = playerLet()
    turn = firstTurn()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':  # Player’s turn.
            makeBoard(game)
            move = playerMove(game)
            chooseMove(game, player, move)
            if win(game, player):
                makeBoard(game)
                print('Congratulations! You won!')
                gameIsPlaying = False
            else:
                if fullBoard(game):
                    makeBoard(game)
                    print('You tied!')
                    break
                else:
                    turn = 'computer'

        else:  # Computer’s turn.
            move = computerMove(game, computer)
            chooseMove(game, computer, move)
            if win(game, computer):
                makeBoard(game)
                print('The computer won! You lose.')
                gameIsPlaying = False
            else:
                if fullBoard(game):
                    makeBoard(game)
                    print('You tied!')
                    break
                else:
                    turn = 'player'

    if not restart():
        break
