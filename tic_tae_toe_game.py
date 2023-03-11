import random

print("WELCOME TO THE TIC-TAC-TOE GAME\n")
print("DO YOU WANT TO PLAY AGAINST AI OR MULTIPLAYER?\n")
mode_input = input(
    "TYPE 'M' IF YOU WANT TO PLAY MULTIPLAYER. TYPE 'A' IF YOU WANT TO PLAY AGAINST AI.: ")

x = "_1_|_2_|_3_"
y = "_4_|_5_|_6_"
z = " 7 | 8 | 9 "
wrong_input = False


def print_game():

    print(x)
    print(y)
    print(z)


def out_user_1_input():

    global x, y, z, wrong_input

    user_1_input = input(
        "USER 1, Type in the number you want to place your cross in: ")

    if user_1_input == "1":

        if x[1] == "❌" or x[1] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_1_input()
        else:
            x = x.replace(user_1_input, "❌", 1)
            print_game()

    elif user_1_input == "2":

        if x[5] == "❌" or x[5] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_1_input()
        else:
            x = x.replace(user_1_input, "❌", 1)
            print_game()

    elif user_1_input == "3":

        if x[9] == "❌" or x[9] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_1_input()
        else:
            x = x.replace(user_1_input, "❌", 1)
            print_game()

    elif user_1_input == "4":

        if y[1] == "❌" or y[1] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_1_input()
        else:
            y = y.replace(user_1_input, "❌", 1)
            print_game()

    elif user_1_input == "5":

        if y[5] == "❌" or y[5] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_1_input()
        else:
            y = y.replace(user_1_input, "❌", 1)
            print_game()

    elif user_1_input == "6":

        if y[9] == "❌" or y[9] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_1_input()
        else:
            y = y.replace(user_1_input, "❌", 1)
            print_game()

    elif user_1_input == "7":

        if z[1] == "❌" or z[1] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_1_input()
        else:
            z = z.replace(user_1_input, "❌", 1)
            print_game()

    elif user_1_input == "8":

        if z[5] == "❌" or z[5] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_1_input()
        else:
            z = z.replace(user_1_input, "❌", 1)
            print_game()

    elif user_1_input == "9":

        if z[9] == "❌" or z[9] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_1_input()
        else:
            z = z.replace(user_1_input, "❌", 1)
            print_game()

    else:
        print("Wrong entry. Enter any number that's available in the tic-tae-toe posiiton above.\n")
        out_user_1_input()


def AI_output():

    global x, y, z

    user_2_input = str(random.randint(1, 10))

    if user_2_input == "1":

        if x[1] == "❌" or x[1] == "🟣":
            # print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            AI_output()
        else:
            x = x.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "2":

        if x[5] == "❌" or x[5] == "🟣":
            # print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            AI_output()
        else:
            x = x.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "3":

        if x[9] == "❌" or x[9] == "🟣":
            # print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            AI_output()
        else:
            x = x.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "4":

        if y[1] == "❌" or y[1] == "🟣":
            # print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            AI_output()
        else:
            y = y.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "5":

        if y[5] == "❌" or y[5] == "🟣":
            # print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            AI_output()
        else:
            y = y.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "6":

        if y[9] == "❌" or y[9] == "🟣":
            # print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            AI_output()
        else:
            y = y.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "7":

        if z[1] == "❌" or z[1] == "🟣":
            # print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            AI_output()
        else:
            z = z.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "8":

        if z[5] == "❌" or z[5] == "🟣":
            # print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            AI_output()
        else:
            z = z.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "9":

        if z[9] == "❌" or z[9] == "🟣":
            # print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            AI_output()
        else:
            z = z.replace(user_2_input, "🟣", 1)
            print_game()

    else:
        # print("Wrong entry. Enter any number that's available in the tic-tae-toe posiiton above.\n")
        AI_output()

    # print_game()


def out_user_2_input():

    global x, y, z

    user_2_input = input(
        "USER 2, Type in the number you want to place your circle in: ")

    if user_2_input == "1":

        if x[1] == "❌" or x[1] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_2_input()
        else:
            x = x.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "2":

        if x[5] == "❌" or x[5] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_2_input()
        else:
            x = x.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "3":

        if x[9] == "❌" or x[9] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_2_input()
        else:
            x = x.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "4":

        if y[1] == "❌" or y[1] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_2_input()
        else:
            y = y.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "5":

        if y[5] == "❌" or y[5] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_2_input()
        else:
            y = y.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "6":

        if y[9] == "❌" or y[9] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_2_input()
        else:
            y = y.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "7":

        if z[1] == "❌" or z[1] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_2_input()
        else:
            z = z.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "8":

        if z[5] == "❌" or z[5] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_2_input()
        else:
            z = z.replace(user_2_input, "🟣", 1)
            print_game()

    elif user_2_input == "9":

        if z[9] == "❌" or z[9] == "🟣":
            print("INVALID INPUT. THIS POSITION IS ALREADY FILLED.TRY ANOTHER ONE.\n")
            out_user_2_input()
        else:
            z = z.replace(user_2_input, "🟣", 1)
            print_game()

    else:
        print("Wrong entry. Enter any number that's available in the tic-tae-toe posiiton above.\n")
        out_user_2_input()


def check_user_1_won():
    global x, y, z

    if x[1] == "❌" and x[5] == "❌" and x[9] == "❌":
        return True
    elif y[1] == "❌" and y[5] == "❌" and y[9] == "❌":
        return True
    elif z[1] == "❌" and z[5] == "❌" and z[9] == "❌":
        return True
    elif x[1] == "❌" and y[1] == "❌" and z[1] == "❌":
        return True
    elif x[5] == "❌" and y[5] == "❌" and z[5] == "❌":
        return True
    elif x[9] == "❌" and y[9] == "❌" and z[9] == "❌":
        return True
    elif x[1] == "❌" and y[5] == "❌" and z[9] == "❌":
        return True
    elif x[9] == "❌" and y[5] == "❌" and z[1] == "❌":
        return True


def check_user_2_won():
    global x, y, z

    if x[1] == "🟣" and x[5] == "🟣" and x[9] == "🟣":
        return True
    elif y[1] == "🟣" and y[5] == "🟣" and y[9] == "🟣":
        return True
    elif z[1] == "🟣" and z[5] == "🟣" and z[9] == "🟣":
        return True
    elif x[1] == "🟣" and y[1] == "🟣" and z[1] == "🟣":
        return True
    elif x[5] == "🟣" and y[5] == "🟣" and z[5] == "🟣":
        return True
    elif x[9] == "🟣" and y[9] == "🟣" and z[9] == "🟣":
        return True
    elif x[1] == "🟣" and y[5] == "🟣" and z[9] == "🟣":
        return True
    elif x[9] == "🟣" and y[5] == "🟣" and z[1] == "🟣":
        return True


winner = ""
move_counter = 0

print_game()

while True:

    print("\n")

    print("\n")

    out_user_1_input()

    check_user_1_won()

    if check_user_1_won():
        if mode_input == "M":

            winner = "User 1 has"
        else:
            winner = "YOU have"
        break

    print("\n")

    move_counter += 1
    print("\n")

    if move_counter >= 9:
        winner = "THE GAME IS A DRAW!"
        break

    if mode_input == "M":

        out_user_2_input()

    else:
        AI_output()

    check_user_2_won()

    if check_user_2_won():
        if mode_input == "M":

            winner = "User 2 has"
        else:
            winner = "THE AI has"

        break

    move_counter += 1

print("\n")
print("\n")

if winner == "THE GAME IS A DRAW!":
    print(winner)
else:
    print(f"{winner} won!!")
