#!/usr/bin/python3

import sys


# Table Section
def prinline(*args):
    """
    "print in line"
    just another print without "sep" and "end"
    to make it ease shorter in other functions
    :param args: like print
    :return: like print
    """
    print(*args, end="", sep="")


def row():
    """
    :return: row of the table
    """
    for i in range(0, 3):
        prinline("*", "-" * 3)
    prinline("*")
    print("")


def col(inp1,inp2,inp3):
    """
    :param inp1: 1,4,7 = X or O
    :param inp2: 2,5,8 = X or O
    :param inp3: 3,6,9 = X or O
    :return: col of the table take there parameters
    """
    prinline("|", " ", "".join(inp1), " ")
    prinline("|", " ", "".join(inp2), " ")
    prinline("|", " ", "".join(inp3), " ")
    prinline("|")
    print("")

def init_xo_grid():
    """
    This function return a dictionary of numbers from 1 to 9
    :param: None
    :return dict of int
    """
    return {"i1": "1", "i2": "2", "i3": "3", "i4": "4", "i5": "5",
      "i6": "6", "i7": "7", "i8": "8", "i9": "9"}

def table(np):
    """
    :return: the complete table with nums of the positions
    """
    row()
    col(np["i1"], np["i2"], np["i3"])
    row()
    col(np["i4"], np["i5"], np["i6"])
    row()
    col(np["i7"], np["i8"], np["i9"])
    row()

def map_input_with_cell(cell):
    return "i" + cell

def correct_cell(mv, np):
    '''
    This function takes the cell number, and check if it is a valid
    move or not
    :param: mv -> int
    :param: np -> list
    :return: bool
    '''
    mv = map_input_with_cell(mv)
    check = False

    # iffffffffffffffffs Sections
    # for every turn check for the num of the the position and if there O or X before
    # then type player mark in it mv1 means players 1 turns
    # I will change it later to change who start the game according to the winner
    if np[mv] != "X" and np[mv] != "O":
        check = True
    return check


def is_winner(np, player_sym):
    '''
    Check if the player win or not
    :param: np -> list
    :return: bool
    '''
    if np["i1"] == np["i2"] == np["i3"] == player_sym \
                or np["i4"] == np["i5"] == np["i6"] == player_sym \
                or np["i7"] == np["i8"] == np["i9"] == player_sym \
                or np["i3"] == np["i5"] == np["i7"] == player_sym \
                or np["i1"] == np["i5"] == np["i9"] == player_sym \
                or np["i1"] == np["i4"] == np["i7"] == player_sym \
                or np["i2"] == np["i5"] == np["i8"] == player_sym \
                or np["i3"] == np["i6"] == np["i9"] == player_sym:
        return True
    return False

def is_draw(np):
    '''
    Check if the game draws
    :param: np -> list
    :return: bool
    '''
    if np["i1"] != "1" and np["i2"] != "2" and np["i3"] != "3" \
    and np["i4"] != "4" and np["i5"] != "5" and np["i6"] != "6" \
    and np["i7"] != "7" and np["i8"] != "8" and np["i9"] != "9":
        return True

    return False

def draw_procedural(player1, player2):
    print("Draw")
    print("{} score {} \n{} score {}".format(
        player1['name'], player1['score'],
        player2['name'], player2['score'])
        )

def move_calc(mv, np, player_sym):
    '''
    :param: mv -> str
    :param: np -> list
    :param: player_sym -> str
    :return: void
    '''
    while True:
        if correct_cell(mv, np):
            mv = map_input_with_cell(mv)
            np[mv] = player_sym
            table(np)
            break
        else:
            print("Please enter num between 1 and 9 if it dosen't entered before")
            table(np)
        mv = input("Enter num of position : \n")

def print_players_score(player1, player2):
    print("{} score : {}\n".format(player1['name'], player1['score']))
    print("{} score : {}\n".format(player2['name'], player2['score']))


# Game Section the worst XO
def game(player1, player2):
    """
    !! really need some hard work
    :return: table and players inputs and scores
    """
    np = init_xo_grid()
    table(np)

    while True:
        mv1 = input("{} turn \nenter num of position : \n".format(player1['name']))
        move_calc(mv1, np, "X")

        # check if player one is the winner
        if is_winner(np, "X"):
            player1['score'] += 1
            print_players_score()
            break

        # check If Draw
        elif is_draw(np):
            draw_procedural(player1, player2)
            break

        # player two turn
        mv2 = input("{} turn \nenter num of position : \n".format(player2['name']))
        move_calc(mv2, np, "O")

        # check if player two is the winner
        if is_winner(np, "O"):
            player2['score'] += 1
            print_players_score()
            break

        elif is_draw(np):
            draw_procedural(player1, player2)
            break

def main():
    # take players name and make sure they give us their names
    def init_player():
        return {"name": '', "score": 0}
    
    # Players Names Section
    player1 = init_player()
    player2 = init_player()

    while not player1['name']:
        print("Player 1".center(24))
        player1['name'] = input("please enter you name : \n")
        if not player1['name']:
            print("can't play without your name >_>\n")
            continue
        while not player2['name']:
            print("Player 2".center(24))
            player2['name'] = input("please enter you name : \n")
            if not player2['name']:
                print("can't play without your name >_>\n")

    print("\n{} will play with 'X' \n{} wil play with 'O'".format(player1['name'] ,player2['name']))

    # just break to make sure the players have known their mark
    input("\n\nPress enter to start the game >_< \n")

    # run the game
    game(player1, player2)

    while True:
        ans = input("Do you want to play again : (answer by y or n)\n")
        if ans == "y":
            game(player1, player2)
        elif ans == "n":
            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
