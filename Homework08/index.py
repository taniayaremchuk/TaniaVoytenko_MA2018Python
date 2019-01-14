"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 70        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    
    while board.check_win() == None:
        board_empty_squares = board.get_empty_squares()
        random_square = random.choice(board_empty_squares)
        board.move(random_square[0], random_square[1], player)
        player = provided.switch_player(player)
        
def mc_update_scores(scores, board, player):
    board_dimension = range(board.get_dim())
    winner = board.check_win() 
    
    for row in board_dimension:
        for col in board_dimension:
            current_player = board.square(row, col)
            if current_player == provided.PLAYERX and winner == provided.PLAYERX:
                scores[row][col] += SCORE_CURRENT
            elif current_player == provided.PLAYERX and winner == provided.PLAYERO:
                scores[row][col] += (-1)*SCORE_OTHER
            elif current_player == provided.PLAYERO and winner == provided.PLAYERX:
                scores[row][col] += (-1)*SCORE_OTHER
            elif current_player == provided.PLAYERO and winner == provided.PLAYERO:
                scores[row][col] += SCORE_CURRENT
        
def get_best_move(board, scores):       
    max_score_list = list()
    max_comparison = None
    board_dimension = range(board.get_dim())
    board_empty_squares = board.get_empty_squares()

    for row in board_dimension:
        for col in board_dimension:
            current_position = (row, col)
            if max_comparison == None and current_position in board_empty_squares:
                max_comparison = scores[row][col]
                max_score_list = list([current_position])
            elif scores[row][col] > max_comparison and current_position in board_empty_squares:
                max_comparison = scores[row][col]
                max_score_list = list([current_position])
            elif scores[row][col] == max_comparison and current_position in board_empty_squares:
                max_score_list.append(current_position)    
    random_max_move = random.choice(max_score_list)
    return random_max_move

def mc_move(board, player, trials):
   
    scores = [[0 for _ in range(board.get_dim())] 
                          for _ in range(board.get_dim())]
    
    for _ in range(trials):
        cloned_board = board.clone()
        mc_trial(cloned_board, player)
        mc_update_scores(scores, cloned_board, player)    
    best_move = get_best_move(board, scores)    
    return best_move  

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

