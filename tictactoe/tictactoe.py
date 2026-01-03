"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count = 0
    O_count = 0

    for row in board:
        for col in row:
            if col == X:
                X_count += 1
            elif col == O:
                O_count += 1
            
    if X_count == O_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    i = 0
    j = 0

    for row in board:
        for col in row:
            if col == EMPTY:
                moves.add((i,j)) 
            j += 1               
        i +=1
            
        j = 0      
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action in board != EMPTY:
        raise ValueError
    
    copy = []

    for row in board:
        copy_row = []
        for element in row:
            copy_row.append(element)
        copy.append(copy_row)
   
    turn = player(board)

    copy[action[0]][action[1]] = turn

    return copy
#mehal's version:
''''
    deep_copy=[]
    for i in range(3):
        row=[]
        for j in range(3):
            if (i,j) == action:
                row.append(player(board))
            else:
                row.append(board[i][j])
        deep_copy.append(row)
    return deep_copy'''

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # my virsion
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == O:
            return O
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        if board[i][0] == board[i][1] == board[i][2] == O:
            return O
        if board[i][0] == board[i][1] == board[i][2] == X:
            return X

    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    
    return None
 # batter virsion!! 
"""def winner(board):
    # All possible winning lines: 3 rows, 3 columns, 2 diagonals
    lines = []

    # Rows
    for i in range(3):
        lines.append([board[i][0], board[i][1], board[i][2]])

    # Columns
    for j in range(3):
        lines.append([board[0][j], board[1][j], board[2][j]])

    # Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    # Check each line for X or O
    for line in lines:
        if line == [X, X, X]:
            return X
        if line == [O, O, O]:
            return O

    return None"""

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)

    if win is not None:
        return True

    for row in board:
        for element in row:
            if element == EMPTY:
                return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        win = winner(board)

        if win == X:
            return 1
        if win == O:
            return -1
    
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current = player(board)

    if current == X:
        best_score = -math.inf
        best_move = None

        for action in actions(board):
            score = min_value(result(board,action))
            if score > best_score:
                best_score = score
                best_move = action

        return best_move
    if current == O:
        best_score = math.inf
        best_move = None

        for action in actions(board):
            score = max_value(result(board,action))
            if score < best_score:
                best_score = score
                best_move = action

        return best_move
    
def max_value(board):
        
    if terminal(board):
        return utility(board)
        
    v = -math.inf

    for action in actions(board):
        v = max(v,min_value(result(board,action)))

    return v    
    
def min_value(board):

    if terminal(board):
        return utility(board)
         
    v = math.inf

    for action in actions(board):
        v = min(v,max_value(result(board,action)))

    return v 
    
