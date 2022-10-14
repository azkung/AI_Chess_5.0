import chess
import math



# for i in range(1,7):
#     for j in board.pieces(i,chess.COLORS[0]):
#         print(j, i)
        
def scoreCalcBasic(board: chess.Board):
    currentScore = 0

    for i in range(1,7):
        if i == 1:
            currentScore += len(board.pieces(i, chess.COLORS[0]))
        if i == 2:
            currentScore += 3*len(board.pieces(i, chess.COLORS[0]))
        if i == 3:
            currentScore += 3*len(board.pieces(i, chess.COLORS[0]))
        if i == 4:
            currentScore += 5*len(board.pieces(i, chess.COLORS[0]))
        if i == 5:
            currentScore += 9*len(board.pieces(i, chess.COLORS[0]))
            
    for i in range(1,7):
        if i == 1:
            currentScore -= len(board.pieces(i, chess.COLORS[1]))
        if i == 2:
            currentScore -= 3*len(board.pieces(i, chess.COLORS[1]))
        if i == 3:
            currentScore -= 3*len(board.pieces(i, chess.COLORS[1]))
        if i == 4:
            currentScore -= 5*len(board.pieces(i, chess.COLORS[1]))
        if i == 5:
            currentScore -= 9*len(board.pieces(i, chess.COLORS[1]))
    
    return currentScore

def scoreCalcMiddleRush(board: chess.Board):
    currentScore = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        
        if piece != None:
            c = square%8
            r = math.floor(square/8)
            distanceFromCenter = math.sqrt(((c-4.5)**2) + ((r-4.5)**2))
            
            if piece.piece_type == 1:
                if piece.color == True:
                    currentScore += (4 +  ((6-round(distanceFromCenter))/30))
                else:
                    currentScore -= (4 +  ((6-round(distanceFromCenter))/30))
                    
            if piece.piece_type == 2:
                if piece.color == True:
                    currentScore += (12 +  ((6-round(distanceFromCenter))/30))
                else:
                    currentScore -= (12 +  ((6-round(distanceFromCenter))/30))
                    
            if piece.piece_type == 3:
                if piece.color == True:
                    currentScore += (12 +  ((6-round(distanceFromCenter))/30))
                else:
                    currentScore -= (12 +  ((6-round(distanceFromCenter))/30))
                    
            if piece.piece_type == 4:
                if piece.color == True:
                    currentScore += (20 +  ((6-round(distanceFromCenter))/30))
                else:
                    currentScore -= (20 +  ((6-round(distanceFromCenter))/30))
            
            if piece.piece_type == 5:
                if piece.color == True:
                    currentScore += (32 +  ((6-round(distanceFromCenter))/30))
                else:
                    currentScore -= (32 +  ((6-round(distanceFromCenter))/30))
                    
    return currentScore


def scoreCalcAttack(board: chess.Board):
    currentScore = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        
        if piece != None:
            
            if piece.piece_type == 1:
                if piece.color == True:
                    currentScore += (4 + len(board.attacks(square)))
                else:
                    currentScore -= (4 + len(board.attacks(square)))
                    
            if piece.piece_type == 2:
                if piece.color == True:
                    currentScore += (12 + len(board.attacks(square)))
                else:
                    currentScore -= (12 + len(board.attacks(square)))
                    
            if piece.piece_type == 3:
                if piece.color == True:
                    currentScore += (12 + len(board.attacks(square)))
                else:
                    currentScore -= (12 + len(board.attacks(square)))
                    
            if piece.piece_type == 4:
                if piece.color == True:
                    currentScore += (20 + len(board.attacks(square)))
                else:
                    currentScore -= (20 + len(board.attacks(square)))
            
            if piece.piece_type == 5:
                if piece.color == True:
                    currentScore += (32 + len(board.attacks(square)))
                else:
                    currentScore -= (32 + len(board.attacks(square)))
                    
    return currentScore


def scoreCalcBoard(board):
    return scoreCalcMiddleRush(board)


def AI(board : chess.Board, depth, alpha, beta):
    #Minimax AI that beats you
    #White maximizing, Black minimizing
    
    if board.is_checkmate():
        if board.turn == True:
            return float('-inf'), None
        else:
            return float('inf'), None
    
    if board.is_stalemate():
        return 0, None
    
    if board.is_game_over():
        return 0, None
        

    if depth == 0:
        return scoreCalcBoard(board), None

    if board.turn == True:
        #Maximizing White
        maxScore = float('-inf')
        maxMove = None
        
        for move in board.legal_moves:
            board.push(move)
            score = AI(board, depth-1, alpha, beta)[0]
            board.pop()
            
            previousMaxScore = maxScore
            maxScore = max(score, maxScore)

            if maxScore != previousMaxScore:
                maxMove = move
                
            alpha = max(alpha, score)
            if beta <= alpha:
                break

        return maxScore, maxMove

    else:
        #Minimizing Black
        minScore = float('inf')
        
        minMove = None
        
        for move in board.legal_moves:
            board.push(move)
            score = AI(board, depth-1, alpha, beta)[0]
            board.pop()
            
            previousMinScore = minScore
            minScore = min(score, minScore)

            if minScore != previousMinScore:
                minMove = move 
            
            beta = min(beta, score)

            if beta <= alpha:
                break

        return minScore, minMove
    

def bestMove(board: chess.Board):
    score, bestMove = AI(board, 3, float('-inf'), float('inf'))
    if bestMove == None:
        for move in board.legal_moves:
            return move
    return bestMove