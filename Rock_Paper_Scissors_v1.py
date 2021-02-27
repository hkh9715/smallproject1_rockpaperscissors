#let's play rock paper scissors game
#rock wins scissors / paper wins rock / scissors wins paper 
#update1 : make draw part / make format(make simply)
#update2 : make 'play again' part
#update3 : UpperLower / random
#update4 : enter when new game starts
#update5 : make error message by 'try&except' / make sure to restart the game by 'continue' / make odds
#update6 : make odds detail / make definitions for simple code / make color for situation
#update7 : make color for windows situation 


 
import ctypes
import random

STD_INPUT_HANDLE   = -10
STD_OUTPUT_HANDLE  = -11
STD_ERROR_HANDLE   = -12
 
FOREGROUND_BLACK     = 0x00
FOREGROUND_BLUE      = 0x01 # text color contains blue.
FOREGROUND_GREEN     = 0x02 # text color contains green.
FOREGROUND_RED       = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE      = 0x10 # background color contains blue.
BACKGROUND_GREEN     = 0x20 # background color contains green.
BACKGROUND_RED       = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
Type = ['rock', 'paper', 'scissors']

def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

def error1(e1):
    if e1 not in Type:
        raise ValueError

def result_win(player, computer):
    set_color(121)
    print('You win:', 'player {0}, computer {1}'.format(player, computer))
    set_color(7)
    
def result_lose(player, computer):
    set_color(124)
    print('You lose:', 'player {0}, computer {1}'.format(player, computer))
    set_color(7)

num_win = 0
num_draw = 0
num_lose = 0
num_game = 1
odds = 0.0

while True:
    a = input('\nGame{0}\nShow your hand(rock, paper, scissors): '.format(num_game))
    player = a.lower()
    try:
        error1(player)
    except ValueError:
        print('PLEASE type one of these(rock, paper, scissors)')
        continue

    num_game += 1
    computer = random.choice(Type)
    # print(computer)

    if player == computer:
        print('Draw')
        num_draw += 1
    elif player == 'paper':
        if computer == 'rock':
            result_win(player, computer)
            num_win += 1
        else:
            result_lose(player, computer)
            num_lose += 1

    elif player == 'rock':
        if computer == 'scissors':
            result_win(player, computer)
            num_win += 1
        else:
            result_lose(player, computer)
            num_lose += 1

    elif player == 'scissors':
        if computer == 'paper':
            result_win(player, computer)
            num_win += 1
        else:
            result_lose(player, computer)
            num_lose += 1

    try:
        odds = num_win / (num_game-num_draw) * 100
        b = input('Your odds(win:draw:lose, odds): {0}:{1}:{2}, {3}% \nWant to play again? Press ENTER: '.format(num_win, num_draw, num_lose, odds))
    except:
        b = input('Your odds(win:draw:lose, odds): {0}:{1}:{2}, {3}% \nWant to play again? Press ENTER: '.format(num_win, num_draw, num_lose, odds))

    if b != "":
        print('\nSee you')
        break
    else:
        print('play again')