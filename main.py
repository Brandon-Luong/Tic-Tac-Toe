import random

def board(boxes):
    """Calculate and display board
    
    boxes (list): 1-9, and converted X and O

    return (print): Print the board"""

    return print("""
            |       |      
        {}   |   {}   |   {}  
            |       |      
    -----------------------
            |       |      
        {}   |   {}   |   {}  
            |       |      
    -----------------------
            |       |      
        {}   |   {}   |   {}  
            |       |      
    """.format(*boxes))

def playerTurn(freeboxes, player_box):
    """
    Asks user where to place piece.

    freeboxes (list): A list of available boxes
    
    return (int): Chosen box number
    """
    while True:
        try:
            print(f'Where do you want to place your piece?')
            print()
            user_input = (input("Input an available box number or 'exit' to quit game: "))
            user_input_int = int(user_input)
            assert user_input_int in freeboxes
        except AssertionError:
            if not (0 < user_input_int < 10):
                print('Please enter a valid box number.')
                print()
            else:
                print('That box is not available.')
                print()
        except:
            if user_input == 'exit':
                return user_input
            else:
                print('Invalid input.')
                print()
        else:
            chosen_box = freeboxes.pop(freeboxes.index(user_input_int))
            player_box.append(chosen_box)
            player_box.sort()
            return chosen_box

def compTurn(freeboxes, comp_box):
    """
    Computer picks a random available box number.

    freeboxes (list): Available box numbers

    return (int): Chosen box number
    """
    comp_choose = random.choice(freeboxes)
    chosen_box = freeboxes.pop(freeboxes.index(comp_choose))
    comp_box.append(chosen_box)
    comp_box.sort()
    return chosen_box

def winCheck(box):
    """
    Checks box if it has connected 3.

    box (list): Used box numbers

    return (bool): True to win, otherwise False.
    """
    for number in box:
        # Diagonal checks
        if number == 1:
            if 5 in box and 9 in box:
                return True
        if number == 3:
            if 5 in box and 7 in box:
                return True
        # Row checks
        if number in range(1,8,3):
            if (number+1 in box) and (number+2 in box):
                return True
        # Column checks
        if number in range(1,4):
            if (number+3 in box) and (number+6 in box):
                return True
    return False

def playGame():
    """ Plays the game"""
    print('Welcome to Tic-Tac-Toe!')
    game_flag = True
    while game_flag:
        box_represent = [1,2,3,4,5,6,7,8,9]
        freeboxes = box_represent[:]
        player_box = []
        comp_box = []
        board(box_represent)
        while True:
            print('It is now your turn.')
            print()
            chosen_box = playerTurn(freeboxes, player_box)
            if chosen_box == 'exit':
                game_flag = False
                break
            box_represent[chosen_box - 1] = 'X'
            board(box_represent)
            if winCheck(player_box):
                print('You win!')
                print("Let's play again.")
                print()
                break
            elif freeboxes == []:
                print("It's a draw.")
                print("Let's play again.")
                break
            else:
                print("It is now the computer's turn.")
                chosen_box = compTurn(freeboxes, comp_box)
                box_represent[chosen_box - 1] = 'O'
                board(box_represent)
                if winCheck(comp_box):
                    print('Oh no, you lost.')
                    print("Let's play again.")
                    print()
                    break
    print('Bye!')

if __name__ == "__main__":
    playGame()
