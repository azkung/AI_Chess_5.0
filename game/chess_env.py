import chess
import math
import bot_custom as bot_custom
import bot_inference as bot_inference
import bot_random as bot_random

board = chess.Board()


# while True:
#     print(board)
#     print()
#     score, bestMove = AI(board, 5, float('-inf'), float('inf'))
#     print(bestMove)
#     board.push(bestMove)
#     print(board)
    
#     print(board.legal_moves)
#     myMove = input("Enter Move: ")
#     board.push_san(myMove)
    
    
print(board)
print()
moves = 0
while board.is_game_over() == False:
    print(board.turn)
    bestMove = bot_inference.bestMove(board)
    board.push(bestMove)
    print(board)
    print()

    if(board.is_game_over()):
        break

    print(board.turn)
    bestMove = bot_custom.bestMove(board)
    board.push(bestMove)
    print(board)
    print()

    moves += 1

    
print(board)
print(moves)
if(board.turn):
    print("Black Wins")
else:
    print("White Wins")