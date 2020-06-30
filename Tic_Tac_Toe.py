move = ['_','_','_','_','_','_','_','_','_']
first_move = "X"
draw = "_" in move
ok_moves = ["O", "X", "_"]
ok_types = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
ok_new_moves = (("1 3"), ("2 3"), ("3 3"), ("1 2"), ("2 2"), ("3 2"), ("1 1"), ("2 1"), ("3 1"))
x = move.count('X')
o = move.count('O')
win_count = 0
for _ in move:
    if _ not in ok_moves:
        entry = input(f"enter cells:")   
def win():
    if draw is False:
        print("Draw")
    else:
        print("{0} wins" .format(winner))
def print_board():
    line_1 = ("| " + (move[0]) + " " + (move[1]) + " " + (move[2]) + " |")
    line_2 = ("| " + (move[3]) + " " + (move[4]) + " " + (move[5]) + " |")
    line_3 = ("| " + (move[6]) + " " + (move[7]) + " " + (move[8]) + " |")
    print("---------")
    print(line_1.replace("_", " "))
    print(line_2.replace("_", " "))
    print(line_3.replace("_", " "))
    print("---------")
print_board()
if x - o >= 2:
    print("Impossible")
if o - x >= 2:
    print("Impossible")
win_1 = move[0] == move[1] == move[2]
win_2 = move[3] == move[4] == move[5]
win_3 = move[6] == move[7] == move[8]
win_4 = move[0] == move[3] == move[6]
win_5 = move[1] == move[4] == move[7]
win_6 = move[2] == move[5] == move[8]
win_7 = move[0] == move[4] == move[8]
win_8 = move[6] == move[4] == move[2]
if win_1 is True:
    if move[0] != "_":
        win_count = win_count + 1
        winner = move[0]
if win_2 is True:
    if move[3] != "_":
        win_count = win_count + 1
        winner = move[3]
if win_3 is True:
    if move[6] != "_":
        win_count = win_count + 1
        winner = move[6]
if win_4 is True:
    if move[0] != "_":
        win_count = win_count + 1
        winner = move[0]
if win_5 is True:
    if move[1] != "_":
        win_count = win_count + 1
        winner = move[1]
if win_6 is True:
    if move[2] != "_":
        win_count = win_count + 1
        winner = move[2]
if win_7 is True:
    if move[0] != "_":
        win_count = win_count + 1
        winner = move[0]
if win_8 is True:
    if move[6] != "_":
        win_count = win_count + 1
        winner = move[6]
while win_count == 0:
    draw = "_" in move
    if draw is True:
        new_move = input("Enter the coordinates:")
        if new_move[0] not in ok_types:
            print("You should enter numbers!")
        elif new_move[2] not in ok_types:
            print("You should enter numbers!")
        else:
            new_move == tuple(new_move)
            if new_move not in ok_new_moves:
                print("Coordinates should be from 1 to 3!")
            elif new_move in ok_new_moves:
                if new_move == ("1 1"):
                    if move[6] != "_":
                        print("This cell is occupied! Choose another one!")
                    else:
                        move[6] = first_move
                        print_board()
                        if first_move == "X":
                            first_move = "O"
                        else:
                            first_move = "X"
                elif new_move == ("1 2"):
                    if move[3] != "_":
                        print("This cell is occupied! Choose another one!")
                    else:
                        move[3] = first_move
                        print_board()
                        if first_move == "X":
                            first_move = "O"
                        else:
                            first_move = "X"
                if new_move == ("1 3"):
                    if move[0] != "_":
                        print("This cell is occupied! Choose another one!")
                    else:
                        move[0] = first_move
                        print_board()
                        if first_move == "X":
                            first_move = "O"
                        else:
                            first_move = "X"
                if new_move == ("2 1"):
                    if move[7] != "_":
                        print("This cell is occupied! Choose another one!")
                    else:
                        move[7] = first_move
                        print_board()
                        if first_move == "X":
                            first_move = "O"
                        else:
                            first_move = "X"
                if new_move == ("2 2"):
                    if move[4] != "_":
                        print("This cell is occupied! Choose another one!")
                    else:
                        move[4] = first_move
                        print_board()
                        if first_move == "X":
                            first_move = "O"
                        else:
                            first_move = "X"
                if new_move == ("2 3"):
                    if move[1] != "_":
                        print("This cell is occupied! Choose another one!")
                    else:
                        move[1] = first_move
                        print_board()
                        if first_move == "X":
                            first_move = "O"
                        else:
                            first_move = "X"
                if new_move == ("3 1"):
                    if move[8] != "_":
                        print("This cell is occupied! Choose another one!")
                    else:
                        move[8] = first_move
                        print_board()
                        if first_move == "X":
                            first_move = "O"
                        else:
                            first_move = "X"
                if new_move == ("3 2"):
                    if move[5] != "_":
                        print("This cell is occupied! Choose another one!")
                    else:
                        move[5] = first_move
                        print_board()
                        if first_move == "X":
                            first_move = "O"
                        else:
                            first_move = "X"
                if new_move == ("3 3"):
                    if move[2] != "_":
                        print("This cell is occupied! Choose another one!")
                    else:
                        move[2] = first_move
                        print_board()
                        if first_move == "X":
                            first_move = "O"
                        else:
                            first_move = "X"
                win_1 = move[0] == move[1] == move[2]
                win_2 = move[3] == move[4] == move[5]
                win_3 = move[6] == move[7] == move[8]
                win_4 = move[0] == move[3] == move[6]
                win_5 = move[1] == move[4] == move[7]
                win_6 = move[2] == move[5] == move[8]
                win_7 = move[0] == move[4] == move[8]
                win_8 = move[6] == move[4] == move[2]
                if win_1 is True:
                    if move[0] != "_":
                        win_count = win_count + 1
                        winner = move[0]
                if win_2 is True:
                    if move[3] != "_":
                        win_count = win_count + 1
                        winner = move[3]
                if win_3 is True:
                    if move[6] != "_":
                        win_count = win_count + 1
                        winner = move[6]
                if win_4 is True:
                    if move[0] != "_":
                        win_count = win_count + 1
                        winner = move[0]
                if win_5 is True:
                    if move[1] != "_":
                        win_count = win_count + 1
                        winner = move[1]
                if win_6 is True:
                    if move[2] != "_":
                        win_count = win_count + 1
                        winner = move[2]
                if win_7 is True:
                    if move[0] != "_":
                        win_count = win_count + 1
                        winner = move[0]
                if win_8 is True:
                    if move[6] != "_":
                        win_count = win_count + 1
                        winner = move[6]
    else:
        win_count = win_count + 1
if win_count > 0:
    win()
        
