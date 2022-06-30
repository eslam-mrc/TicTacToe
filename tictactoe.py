#Simple TicTacToe game using python
from IPython.display import clear_output
import os

def printBoard(board):
    print("|"+chr(8254)*5+"|"+chr(8254)*5+"|"+chr(8254)*5+"|")
    print("|  "+board[1]+"  |  "+board[2]+"  |  "+board[3]+"  |")
    print("|"+"     "+"|"+"     "+"|"+"     "+"|")
    print("|"+chr(8254)*5+"|"+chr(8254)*5+"|"+chr(8254)*5+"|")
    print("|  "+board[4]+"  |  "+board[5]+"  |  "+board[6]+"  |")
    print("|"+"     "+"|"+"     "+"|"+"     "+"|")
    print("|"+chr(8254)*5+"|"+chr(8254)*5+"|"+chr(8254)*5+"|")
    print("|  "+board[7]+"  |  "+board[8]+"  |  "+board[9]+"  |")
    print("|"+"_____"+"|"+"_____"+"|"+"_____"+"|")
    
def clear():
    os.system( 'cls' )

def playTicTacToe():
    board = list()
    board = [0,' ',' ',' ',' ',' ',' ',' ',' ',' ']
    counter = 1
    exitFlag = True
    while exitFlag:
    
        while counter <= 9:
            #playerInput()
            letter = ""
            while not (letter.upper() == "X" or letter.upper() == "O"):
                letter = input("Are you an X or an O").upper()
            position = 0
            while not position > 0 and position <= 9:
                try:
                    position = int(input("Pick a place from 1 to 9"))
                except:
                    print("You didn't enter a number, did you?")
            board[position] = letter
            clear()
            printBoard(board)

            if (
            (board[4]==board[5]==board[6]=="X") or
           (board[3]==board[6]==board[9]=="X") or
           (board[1]==board[2]==board[3]=="X") or
           (board[1]==board[4]==board[7]=="X") or
           (board[1]==board[5]==board[9]=="X") or
           (board[2]==board[5]==board[8]=="X") or
           (board[3]==board[5]==board[7]=="X") or
           (board[7]==board[8]==board[9]=="X")):
                print("Congrats X! You Won!")
                break
            elif ((board[4]==board[5]==board[6]=="O") or
           (board[3]==board[6]==board[9]=="O") or
           (board[1]==board[2]==board[3]=="O") or
           (board[1]==board[4]==board[7]=="O") or
           (board[1]==board[5]==board[9]=="O") or
           (board[2]==board[5]==board[8]=="O") or
           (board[3]==board[5]==board[7]=="O") or
           (board[7]==board[8]==board[9]=="O")):
                print("Congrats O! You won!")
                break
            elif (board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " "
                  and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " "
                  and board[9] != " " and
                (board[4] != board[5] or board[4] != board[6] or board[5] != board[6]) and
                 (board[3] != board[6] or board[3] != board[9] or board[6] != board[9]) and
                 (board[1] != board[2] or board[1] != board[3] or board[2] != board[3]) and
                 (board[1] != board[4] or board[1] != board[7] or board[4] != board[7]) and
                 (board[1] != board[5] or board[1] != board[9] or board[5] != board[9]) and
                 (board[2] != board[5] or board[2] != board[8] or board[5] != board[8]) and
                 (board[3] != board[5] or board[3] != board[7] or board[5] != board[7]) and
                 (board[7] != board[8] or board[7] != board[9] or board[8] != board[9])):
                print("It's a draw")
                break
            else:
                continue
            counter+=1
        exitGame = ""
        while not (exitGame.upper() == "Y" or exitGame.upper() == "N"):
            exitGame = input("Do you wanna play again? Y/N").upper()
        if exitGame == "N":
            clear()
            exitFlag = False
        else:
            clear()
            board = [0,' ',' ',' ',' ',' ',' ',' ',' ',' ']
            counter = 1

playTicTacToe()            
