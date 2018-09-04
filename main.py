# first of all take players name and make sure they give us their names

# Players Names Section
player1 = ""
player2 = ""
while not player1:
    print("Player 1".center(24))
    player1 = input("please enter you name : \n")
    if not player1:
        print("can't play without your name >_>\n")
        continue
    while not player2:
        print("Player 2".center(24))
        player2 = input("please enter you name : \n")
        if not player2:
            print("can't play without your name >_>\n")

print("\n{} will play with 'X' \n{} wil play with 'O'".format(player1,player2))

input("\n\nPress enter to start the game >_< \n")
# just break to make sure the players have known their mark

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

def set_np():
    """
    This function return a dictionary of numbers from 1 to 9
    :paran: None
    :return dict of int
    """
    return {"i1": "1", "i2": "2", "i3": "3", "i4": "4", "i5": "5",
      "i6": "6", "i7": "7", "i8": "8", "i9": "9"}

np = set_np()

def table(i1=np["i1"], i2=np["i2"], i3=np["i3"], i4=np["i4"],
          i5=np["i5"], i6=np["i6"], i7=np["i7"], i8=np["i8"], i9=np["i9"]):
    """
    :return: the complete table with nums of the positions
    """
    row()
    col(i1, i2, i3)
    row()
    col(i4, i5, i6)
    row()
    col(i7, i8, i9)
    row()


# Game Section the worst XO
def game():
    """
    !! really need some hard work
    :return: table and players inputs and scores
    """
    table()

    # dic have the nums of the positions will change with X or O later
    p1score = 0
    p2score = 0
    while True:
        mv1 = input("{} turn \nenter num of position : \n".format(player1))


        # iffffffffffffffffs Sections
        # for every turn check for the num of the the position and if there O or X before
        # then type player mark in it mv1 means players 1 turns
        # I will change it later to change who start the game according to the winner
        if mv1 == "9" and np["i9"] != "X" and np["i9"] != "O":
            np["i9"] = "X"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv1 == "8" and np["i8"] != "X" and np["i8"] != "O":
            np["i8"] = "X"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv1 == "7" and np["i7"] != "X" and np["i7"] != "O":
            np["i7"] = "X"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv1 == "6" and np["i6"] != "X" and np["i6"] != "O":
            np["i6"] = "X"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv1 == "5" and np["i5"] != "X" and np["i5"] != "O":
            np["i5"] = "X"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv1 == "4" and np["i4"] != "X" and np["i4"] != "O":
            np["i4"] = "X"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv1 == "3" and np["i3"] != "X" and np["i3"] != "O":
            np["i3"] = "X"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv1 == "2" and np["i2"] != "X" and np["i2"] != "O":
            np["i2"] = "X"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv1 == "1" and np["i1"] != "X" and np["i1"] != "O":
            np["i1"] = "X"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        else:
            print("please enter num between 1 and 9 if it dosen't entered before")
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        # check if player one is the winner
        if np["i1"] == np["i2"] == np["i3"] == "X" \
                or np["i4"] == np["i5"] == np["i6"] == "X" \
                or np["i7"] == np["i8"] == np["i9"] == "X" \
                or np["i3"] == np["i5"] == np["i7"] == "X" \
                or np["i1"] == np["i5"] == np["i9"] == "X" \
                or np["i1"] == np["i4"] == np["i7"] == "X" \
                or np["i2"] == np["i5"] == np["i8"] == "X" \
                or np["i3"] == np["i6"] == np["i9"] == "X":
            p1score += 1
            print("{} score : {}\n".format(player1, p1score))
            break

        # check If Draw
        elif np["i1"] != "1" and np["i2"] != "2" and np["i3"] != "3" and np["i4"] != "4" \
                and np["i5"] != "5" and np["i6"] != "6" and np["i7"] != "7" and np["i8"] != "8" \
                and np["i9"] != "9":
            print("Draw")
            print("{} score {} \n{} score {}".format(player1, p1score, player2, p2score))
            break

        # player two turn
        mv2 = input("{} turn \nenter num of position : \n".format(player2))

        if mv2 == "9" and np["i9"] != "X" and np["i9"] != "O":
            np["i9"] = "O"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv2 == "8" and np["i8"] != "X" and np["i8"] != "O":
            np["i8"] = "O"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv2 == "7" and np["i7"] != "X" and np["i7"] != "O":
            np["i7"] = "O"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv2 == "6" and np["i6"] != "X" and np["i6"] != "O":
            np["i6"] = "O"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv2 == "5" and np["i5"] != "X" and np["i5"] != "O":
            np["i5"] = "O"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv2 == "4" and np["i4"] != "X" and np["i4"] != "O":
            np["i4"] = "O"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv2 == "3" and np["i3"] != "X" and np["i3"] != "O":
            np["i3"] = "O"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv2 == "2" and np["i2"] != "X" and np["i2"] != "O":
            np["i2"] = "O"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        elif mv2 == "1" and np["i1"] != "X" and np["i1"] != "O":
            np["i1"] = "O"
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

        else:
            print("please enter num between 1 and 9 if it dosen't entered before")
            table(np["i1"], np["i2"], np["i3"], np["i4"],
                  np["i5"], np["i6"], np["i7"], np["i8"], np["i9"])

            # check if player two is the winner
        if np["i1"] == np["i2"] == np["i3"] == "O" \
                or np["i4"] == np["i5"] == np["i6"] == "O" \
                or np["i7"] == np["i8"] == np["i9"] == "O":
            p2score += 1
            print("{} score : {}\n".format(player2, p2score))
            break

        elif np["i1"] == np["i4"] == np["i7"] == "O" \
                or np["i2"] == np["i5"] == np["i8"] == "O" \
                or np["i3"] == np["i6"] == np["i9"] == "O":
            p2score += 1
            print("{} score : {}\n".format(player2, p2score))
            break

        elif np["i3"] == np["i5"] == np["i7"] == "O" \
                or np["i1"] == np["i5"] == np["i9"] == "O":
            p2score += 1
            print("{} score : {}\n".format(player2, p2score))
            break


game()

while True:
    ans = input("Do you want to play again : (answer by y or n)\n")
    if ans == "y":
        #reset the game's grad and restart the game
        np = set_np()
        game()
    elif ans == "n":
        break
