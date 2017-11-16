##
# Tic-Tac-Toe board program
#
import pprint

def PrintBoard(board):
    print(board['TOP-L'] + '|' + board['TOP-M'] + '|' + board['TOP-R'])
    print('-+-+-')
    print(board['MID-L'] + '|' + board['MID-M'] + '|' + board['MID-R'])
    print('-+-+-')
    print(board['BOT-L'] + '|' + board['BOT-M'] + '|' + board['BOT-R'])

def CheckWin(board):#NEEDS WORK STILL 
    win = False;
    return win
    
    
def UserMoves(board, index, usedSpots):
    print('\n[TOP-L] | [TOP-M] | [TOP-R]')
    print('------------------------')
    print('[MID-L] | [MID-M] | [MID-R]')
    print('------------------------')
    print('[BOT-L] | [BOT-M] | [BOT-R]')
    
    valid = False
    while valid == False:
        
        try:
            key = input('\nMove on which space: ')

            while key != 'TOP-L' and key != 'TOP-M' and key != 'TOP-R' and key != 'MID-L' and key != 'MID-M' and key != 'MID-R' and key != 'BOT-L' and key != 'BOT-M' and key != 'BOT-R':
                    key = input('\nInvalid selection! Move on which space: ')
            valid = True
                
        except ValueError:
            print('Value error!')
        except TypeError:
            print('Type error!')
        
    if key not in usedSpots:
        #print('ADDING TO THE BOARD. ' + 'INDEX IS: ' + str(index))
        #input()
        if index % 2 == 0:
            board[key] = 'X'

        else:
            board[key] = 'O'
            
        index += 1
    else:
        print('Space has been taken, try again!')

            
    usedSpots.append(key)
    #print('\nTHIS IS THE USED LIST')
    #print(usedSpots)
    #print('\nTHIS is the index: ' + str(index) + '\n')

    return index

    
def main():
    usedSpots = []
    index = 0
    player1 = ''
    player2 = ''
    winner = False
    
    board = {'TOP-L': ' ', 'TOP-M': ' ', 'TOP-R': ' ',
             'MID-L': ' ', 'MID-M': ' ', 'MID-R': ' ',
             'BOT-L': ' ', 'BOT-M': ' ', 'BOT-R': ' '}

    for i in range(9):
        index = UserMoves(board, index, usedSpots)
        
        print()
        PrintBoard(board)
        print()
        if i >=5:
            #print('In check win')
            winner = CheckWin(board)


main()
