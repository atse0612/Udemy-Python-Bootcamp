
# coding: utf-8

# In[1]:

# Part 1


# In[2]:

# Step 1: Printing the Board


# In[3]:

from IPython.display import clear_output
def display_board(board):
    
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# In[4]:

# Step 2: Functions for X and O


# In[5]:

def player_input():
    
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')



# In[6]:

# Step 3: Position


# In[7]:

def place_marker(board, marker, position):
    board[position] = marker


# In[8]:

# Step 4: Check to see who won:


# In[9]:

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[10]:

# Part 2:


# In[11]:

# Step 5: Random Generators to See Who Won


# In[12]:

import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[13]:

# Step 6: What is freely available


# In[14]:

def space_check(board, position):
    
    return board[position] == ' '



# In[15]:

# Step 7: Returns a boolean value


# In[16]:

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True    


# In[17]:

# Step 8: Check for free position


# In[18]:

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        
        position = input('Choose your next position: (1-9) ')
    return int(position)


# In[19]:

('1 2 3 4 5 6 7 8 9').split()


# In[20]:

# Step 9: Do you want to play again?


# In[21]:

def replay():
    
    return input('Do you want to play again? Yes or No').lower.startswith(y)


# In[22]:

my_string = 'yup'
my_string.lower().startswith('Y')


# In[ ]:

# Step 10: Use while loops to run the game!


# In[ ]:

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:




# In[ ]:



