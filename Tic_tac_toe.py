# -*- coding: utf-8 -*-
"""
Tic Tac Toe Game
By- Sujay Rittikar
"""

from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('|' + board[7] + '|' + board[8] + '|' + board[9]+ '|')
    print(' '+'-' + ' ' + '-' + ' '+ '-')
    print('|' + board[4] + '|' + board[5] + '|' + board[6] + '|')
    print(' '+'-' + ' ' + '-' + ' '+ '-')
    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|')
    

def player_input():
    
    marker = ''
    
    while(marker!='O' and marker!='X'):
        marker = input("First player, enter your choice: ").upper()
    
    if marker=='X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    
def place_marker(board, marker, position):
    board[position] = marker
    
    
import random

def choose_first():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'
    
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(1, 10):
        if space_check(board, i):
            return False
        
    return True

def player_choice(board):
    y = 0
    
    y = int(input("Enter the next position: "))
    
    if space_check(board, y) and y in range(1, 10):
        return y

def win_check(board, mark):
    return (board[1]==mark and board[2]==mark and board[3]==mark) or (board[4]==mark and board[5]==mark and board[6]==mark) or (board[7]==mark and board[8]==mark and board[9]==mark) or (board[1]==mark and board[5]==mark and board[9]==mark) or (board[3]==mark and board[5]==mark and board[7]==mark) or (board[1]==mark and board[4]==mark and board[7]==mark) or (board[2]==mark and board[5]==mark and board[8]==mark) or (board[3]==mark and board[6]==mark and board[9]==mark)


print('WELCOME TO TIC TAC TOE!')
print(' ')
print('Author: Sujay Rittikar')

Board = [' ']*10
player1, player2 = player_input()
turn = choose_first()
print(turn + ' will go first')

print(' ')
play_game = input("Ready to play?(Yes/No)")

if play_game.lower()[0] == 'y':
    game = True
else:
    game = False
    
    
while game:
    if turn == 'Player 1':
        display_board(Board)
        pos = player_choice(Board)
        place_marker(Board, player1, pos)
        
        if win_check(Board, player1):
            display_board(Board)
            print("Congrats! Player 1 won the game.")
            game = False
        
        else:
            if full_board_check(Board):
                display_board(Board)
                print("Game is drawn!")
                break
            else:
                turn = 'Player 2'
    else:
        display_board(Board)
        pos = player_choice(Board)
        place_marker(Board, player2, pos)
        
        if win_check(Board, player2):
            display_board(Board)
            print("Congrats! Player 2 won the game.")
            game = False
        
        else:
            if full_board_check(Board):
                display_board(Board)
                print("Game is drawn!")
                break
            else:
                turn = 'Player 1'
        