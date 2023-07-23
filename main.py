# Python Tic Tac Toe Game 
# Created by Kyran Zhanat
# Date 17.11.21

'''

Python Tic Tac Toe for 2 players

0) Let the first player to pick his symbol ('X' or 'O' only)
1) The second player will automatically get the left symbol
1) Visual Representation
2) Let players pick a position 
3) They will play in turn 
4) gameon_choice for continuation
5) game_logic for logic of the game_logic
6) placing_symbol for placing your symbol on the board
7) if_won function takes into consideration all the victory cases

'''

def display_board(board):

    print(board[7] +'|'+ board[8] +'|'+ board[9])
    print(board[4] +'|'+ board[5] +'|'+ board[6])
    print(board[1] +'|'+ board[2] +'|'+ board[3])
    

def picking_symbol(name1, name2):
    
    player1 = 'Wrong'
    
    while player1 != 'X' and player1 != 'O':
    
        player1 = input(f"\n{name1}, choose your symbol from these 'X' or 'O'. It's case sensitive: ")
        
    if player1 == 'X':
        player2 = 'O'
        print(f"\n{name1}'s symbol is X")
        print(f"{name2}'s symbol is O")
    else:
        player2 = 'X'
        print(f"\n{name1}'s symbol is O")
        print(f"{name2}'s symbol is X")
    
    print('\nThe game has just started! Good luck!')
    return (player1, player2)
    
    

def pick_position(name):
    
    within_range = False
    position = 'Wrong'
    
    while position.isdigit() == False or within_range == False:
    
        position = input(f'{name}, pick a position at which you wanna place your symbol (1-9): ')
    
        if position.isdigit():
            if int(position) in range(1,10):
                within_range = True
            else:
                print('The number you entered is our of range, please enter 1-9.')
        else:
            print("It's not a digit(+). Enter numbers between 1-9: ")
    
    return int(position)



def placing_symbol(board,pick_position,marker):
    
    board[pick_position] = marker
    
    return board


def gameon_choice():
    
    choice = 'Wrong'
    
    while choice != 'Y' and choice != 'N':
        
        choice = input('\nDo you want to keep playing? "Y" for YES or "N" for No: ')
        
        if choice not in ['Y', 'N']:
            print("Invalid input, type either Y or N!")
            
    
    if choice == 'Y':
        return True
    elif choice == 'N':
        return False


def if_won(board, marker):
    
    if board[7] == board[8] == board[9] == marker:
        return True
    elif board[1] == board[2] == board[3] == marker:
        return True
    elif board[4] == board[5] == board[6] == marker:
        return True
    elif board[1] == board[4] == board[7] == marker:
        return True
    elif board[2] == board[5] == board[8] == marker:
        return True
    elif board[3] == board[6] == board[9] == marker:
        return True
    elif board[3] == board[5] == board[7] == marker:
        return True
    elif board[1] == board[5] == board[9] == marker:
        return True
    else:
        return False
    

def game_logic(board, picking_symbol, pick_position, display_board, name, player):
    
    position = pick_position(name)
    while board[position] != ' ':
        print(f"It's already taken {name}, pick another position!\n")
        position = pick_position(name)
    board = placing_symbol(board, position, player)
    display_board(board)
    
    return board

# Game logic

game_on = True

while game_on:
    
    won = False
    tie = False
    turn = True
    
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    name1 = input("\nWhat's your name Player 1? ")
    name2 = input("\nWhat's your name Player 2? ")
    
    player1, player2 = picking_symbol(name1, name2)
    display_board(board)
    
    while won == False and tie == False:
        
        if turn:
            board = game_logic(board, picking_symbol, pick_position, display_board, name1, player1)
            won = if_won(board, player1)
            if won:
                print(f'\n{name1} has won the game!')
                break
            turn = False
        else:
            board = game_logic(board, picking_symbol, pick_position, display_board, name2, player2)
            won = if_won(board, player2)
            if won:
                print(f'\n{name2} has won the game!')
                break
            turn = True
        
        # Checking
        
        if ' ' in board:
            tie = False
        else: 
            tie = True
            print("\nIt's draw!")

    game_on = gameon_choice()

    
    
                
                
    






















    
        
        
    

