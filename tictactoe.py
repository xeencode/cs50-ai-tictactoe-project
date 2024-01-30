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
    counts_of_x = sum(l.count('X') for l in board)
    counts_of_o = sum(l.count('O') for l in board)
    if counts_of_x == 0 and counts_of_o == 0:
        return "X"
    elif counts_of_x > counts_of_o:
        return "O"
    else:
        return "X"

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
            else:
                pass
    return possible_actions

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    players = ["X", "O"]
    for player in players:
        if board[0][0] == board[0][1] == board[0][2] == player:
            return player
        elif board[1][0] == board[1][1] == board[1][2] == player:
            return player
        elif board[2][0] == board[2][1] == board[2][2] == player:
            return player
        elif board[0][0] == board[1][0] == board[2][0] == player:
            return player
        elif board[0][1] == board[1][1] == board[2][1] == player:
            return player
        elif board[0][2] == board[1][2] == board[2][2] == player:
            return player
        elif board[0][0] == board[1][1] == board[2][2] == player:
            return player     
        elif board[0][2] == board[1][1] == board[2][0] == player:
            return player
    return None

    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    board_filled = sum(l.count(None) for l in board)
    if board_filled == 0:
        return True
    else:
        if winner(board) == None:
            return False
        else:
            return True
        
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    status = winner(board)
    if status == "X":
        return 1
    elif status == "O":
        return -1
    else:
        return 0

    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
