import chess
import numpy as np
from numpy import save
import numpy


def boardToArray(board: chess.Board):
    myboard = []
    pieceListWhite = [0]*6
    pieceListBlack = [0]*6
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        
        if piece != None:
            if piece.piece_type == 1:
                if piece.color == True:
                    myboard.append(1)
                    pieceListWhite[0] += 1
                else:
                    myboard.append(-1)
                    pieceListBlack[0] += 1
                    
            if piece.piece_type == 2:
                if piece.color == True:
                    myboard.append(2)
                    pieceListWhite[1] += 1
                else:
                    myboard.append(-2)
                    pieceListBlack[1] += 1
                    
            if piece.piece_type == 3:
                if piece.color == True:
                    myboard.append(3)
                    pieceListWhite[2] += 1
                else:
                    myboard.append(-3)
                    pieceListBlack[2] += 1
                    
            if piece.piece_type == 4:
                if piece.color == True:
                    myboard.append(4)
                    pieceListWhite[3] += 1
                else:
                    myboard.append(-4)
                    pieceListBlack[3] += 1
            
            if piece.piece_type == 5:
                if piece.color == True:
                    myboard.append(5)
                    pieceListWhite[4] += 1
                else:
                    myboard.append(-5)
                    pieceListBlack[4] += 1

            if piece.piece_type == 6:
                if piece.color == True:
                    myboard.append(6)
                    pieceListWhite[5] += 1
                else:
                    myboard.append(-6)
                    pieceListBlack[5] += 1
        else:
            myboard.append(0)
    inputArray = np.array(myboard + pieceListWhite + pieceListBlack)
    return inputArray

def boardToArrayResultTurn(board: chess.Board):
    myboard = []
    pieceListWhite = [0]*6
    pieceListBlack = [0]*6
    turn = []
    if(board.turn):
        turn.append(1)
    else:
        turn.append(0)
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        
        if piece != None:
            if piece.piece_type == 1:
                if piece.color == True:
                    myboard.append(1)
                    pieceListWhite[0] += 1
                else:
                    myboard.append(-1)
                    pieceListBlack[0] += 1
                    
            if piece.piece_type == 2:
                if piece.color == True:
                    myboard.append(2)
                    pieceListWhite[1] += 1
                else:
                    myboard.append(-2)
                    pieceListBlack[1] += 1
                    
            if piece.piece_type == 3:
                if piece.color == True:
                    myboard.append(3)
                    pieceListWhite[2] += 1
                else:
                    myboard.append(-3)
                    pieceListBlack[2] += 1
                    
            if piece.piece_type == 4:
                if piece.color == True:
                    myboard.append(4)
                    pieceListWhite[3] += 1
                else:
                    myboard.append(-4)
                    pieceListBlack[3] += 1
            
            if piece.piece_type == 5:
                if piece.color == True:
                    myboard.append(5)
                    pieceListWhite[4] += 1
                else:
                    myboard.append(-5)
                    pieceListBlack[4] += 1

            if piece.piece_type == 6:
                if piece.color == True:
                    myboard.append(6)
                    pieceListWhite[5] += 1
                else:
                    myboard.append(-6)
                    pieceListBlack[5] += 1
        else:
            myboard.append(0)
    inputArray = np.array(myboard + pieceListWhite + pieceListBlack + turn)
    return inputArray


def format(path, idx, games):
    board = chess.Board()

    x = []
    y = []

    with open('datasets/all_with_filtered_anotations_since1998.txt', 'r') as f:
        for i in range(5):
            f.readline()

        for i in range(idx):
            f.readline()

        for i in range(games):
            line = str(f.readline())
            arrLine = line.split()

            winner = 0
            if(arrLine[2] == '1-0'):
                winner = 1
            if(arrLine[2] == '1/2-1/2'):
                continue
                winner = 0.5
            if(arrLine[2] == '0-1'):
                winner = 0

            for m in arrLine[17:]:
                # print(board,i, arrLine)
                try:
                    board.push_san(m.split(".")[1:][0])
                except:
                    break

                x.append(boardToArray(board))
                y.append(winner)

            board.reset()
            
    x = np.array(x)
    y = np.array(y)
    print(x.shape)
    print(y.shape)

    save(path + "_x.npy", x)
    save(path + "_y.npy", y)


def format_given_result(path, idx, whiteWins, blackWins, ties):
    board = chess.Board()

    x = []
    y = []

    with open('datasets/all_with_filtered_anotations_since1998.txt', 'r') as f:
        for i in range(5):
            f.readline()

        for i in range(idx):
            f.readline()

        currentWhiteWins = 0
        currentBlackWins = 0
        currentTies = 0


        while (currentWhiteWins < whiteWins or currentBlackWins < blackWins or currentTies < ties):

            line = str(f.readline())
            arrLine = line.split()

            winner = 0
            if(arrLine[2] == '1-0'):
                winner = 1
                if(currentWhiteWins >= whiteWins):
                    continue
            if(arrLine[2] == '1/2-1/2'):
                winner = 0.5
                if(currentTies >= ties):
                    continue
            if(arrLine[2] == '0-1'):
                winner = 0
                if(currentBlackWins >= blackWins):
                    continue

            for m in arrLine[17:]:
                # print(board,i, arrLine)

                try:
                    board.push_san(m.split(".")[1:][0])
                except:
                    break

                if(arrLine[2] == '1-0'):
                    if(currentWhiteWins >= whiteWins):
                        break
                    currentWhiteWins += 1
                if(arrLine[2] == '1/2-1/2'):
                    if(currentTies >= ties):
                        break
                    currentTies += 1
                if(arrLine[2] == '0-1'):
                    if(currentBlackWins >= blackWins):
                        break
                    currentBlackWins += 1

                x.append(boardToArray(board))
                y.append(winner)

            board.reset()

    x = np.array(x)
    y = np.array(y)
    print(x.shape)
    print(y.shape)

    save(path + "_x.npy", x)
    save(path + "_y.npy", y)


def format_given_result_turn(path, idx, whiteWins, blackWins, ties):
    board = chess.Board()

    x = []
    y = []

    with open('datasets/all_with_filtered_anotations_since1998.txt', 'r') as f:
        for i in range(5):
            f.readline()

        for i in range(idx):
            f.readline()

        currentWhiteWins = 0
        currentBlackWins = 0
        currentTies = 0


        while (currentWhiteWins < whiteWins or currentBlackWins < blackWins or currentTies < ties):

            line = str(f.readline())
            arrLine = line.split()

            winner = 0
            if(arrLine[2] == '1-0'):
                winner = 1
                if(currentWhiteWins >= whiteWins):
                    continue
            if(arrLine[2] == '1/2-1/2'):
                winner = 0.5
                if(currentTies >= ties):
                    continue
            if(arrLine[2] == '0-1'):
                winner = 0
                if(currentBlackWins >= blackWins):
                    continue

            for m in arrLine[17:]:
                # print(board,i, arrLine)

                try:
                    board.push_san(m.split(".")[1:][0])
                except:
                    break

                if(arrLine[2] == '1-0'):
                    if(currentWhiteWins >= whiteWins):
                        break
                    currentWhiteWins += 1
                if(arrLine[2] == '1/2-1/2'):
                    if(currentTies >= ties):
                        break
                    currentTies += 1
                if(arrLine[2] == '0-1'):
                    if(currentBlackWins >= blackWins):
                        break
                    currentBlackWins += 1

                x.append(boardToArrayResultTurn(board))
                y.append(winner)

            board.reset()

    x = np.array(x)
    y = np.array(y)
    print(x.shape)
    print(y.shape)

    save(path + "_x.npy", x)
    save(path + "_y.npy", y)
