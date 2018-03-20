# AQA Treasure Hunt v.1.0 - Ian Richardson, 15 March 2018


def cls():
    print("\n" * 100)
    # this is a simple and quick way to get the screen to clear in between sections
    # of the program. I generally make this at the start of any project


def create_grid(width, height, contents):
    #create a 2d array with the specified dimensions & contents
    #called 3 times to create the 3 game tables
    grid = []
    for x in range(height):
        grid.append([])
        for y in range(width):
            grid[x].append(contents)
    return grid


def display_grid(grid, height):
    #prints any array sent to it in a readable format
    cls()
    print("-" * 32)
    for y in range(0, height):
        print("|"+"|".join(grid[y])+"|")
        print("-"*32)


def place_object(grid, object_symbol, num_object, width, height):
    #place the given object symbol into the map in random empty locations
    from random import randint
    while num_object > 0:
        rand_x = randint(-1, width-1)
        rand_y = randint(-1, height-1)
        if grid[rand_y][rand_x] == "   ":
            grid[rand_y][rand_x] = " "+object_symbol+" "
            num_object -= 1
    return grid


def hide_objects(grid, num_chests, num_bandits, width, height):
    #initialises the hidden grid, by hiding the various objects in it, using the place object function
    grid[7][0] = " * "
    grid = place_object(grid, "T", num_chests, width, height)
    grid = place_object(grid, "B", num_bandits, width, height)
    return grid


def get_move():
    #take and validate the user's choice of movement directions and distances
    #returns negative value for left and up movements
    vert_direction = ""
    horz_direction = ""
    while vert_direction != "U" and vert_direction != "D":
        print("Enter U for Up, D for Down:")
        vert_direction = input().upper()
    print("Enter number of squares:")
    vert_move = int(input())
    if vert_direction == "U":
        vert_move = 0 - vert_move
    while horz_direction != "L" and horz_direction != "R":
        print("Enter L for Left, R for Right:")
        horz_direction = input().upper()
    print("Enter number of squares:")
    horz_move = int(input())
    if horz_direction == "L":
        horz_move = 0 - horz_move
    return vert_move, horz_move

def initialise_game(width, height,num_chests,num_bandits):
    player_x_pos = 0
    player_y_pos = height-1
    hidden_grid = create_grid(width, height, "   ")
    hidden_grid = hide_objects(hidden_grid, num_chests, num_bandits, width, height)
    hidden_grid[player_y_pos][player_x_pos] = " * "
    player_grid = create_grid(width, height, "   ")
    player_grid[player_y_pos][player_x_pos] = " * "
    counting_grid = create_grid(width, height, 0)
    return hidden_grid, player_grid, counting_grid, player_y_pos,player_x_pos

def select_custom_game():
    cls()
    print("SELECT A GRID SIZE")
    print("-"*32)
    print("1\t10 x 10")
    print("2\t12 x 12")
    print("3\t16 x 16")
    choice = "x"
    while choice not in "123":
        choice = input("Enter your choice of size: ")
        if choice == "1":
            height = 10
            width = 10
        if choice == "2":
            height = 12
            width = 12
        if choice == "3":
            height = 16
            width = 16
    num_chests = int(input("Enter the number of Chests: "))
    num_bandits = int(input("Enter the number of Bandits: "))
    return height, width, num_chests, num_bandits



def play_game(width, height, num_chests, num_bandits):
    cls()
    score = 0
    total_moves = 0
    hidden_grid, player_grid, counting_grid, player_y_pos, player_x_pos = initialise_game(width, height, num_chests, num_bandits)
    display_grid(player_grid, height)

    while score < 100 and num_chests > 0:
        valid_move = False
        while not valid_move:
            vert_move, horz_move = get_move()
            if player_x_pos + horz_move < 0 or player_x_pos + horz_move > width - 1 or player_y_pos + vert_move < 0 or player_y_pos + vert_move > height - 1:
                print("Invalid Move")
            else:
                total_moves += 1
                valid_move = True
        player_grid[player_y_pos][player_x_pos] = "   "
        player_x_pos += horz_move
        player_y_pos += vert_move
        player_grid[player_y_pos][player_x_pos] = " * "

        if hidden_grid[player_y_pos][player_x_pos] == " T ":
            print("You have found a treasure chest! 10 Gold coins!")
            counting_grid[player_y_pos][player_x_pos] += 1
            score += 10
        elif hidden_grid[player_y_pos][player_x_pos] == " B ":
            print("Oh dear! You have been attacked by bandits! Lose all of your gold.")
            score = 0
        if counting_grid[player_y_pos][player_x_pos] >= 2:
            hidden_grid[player_y_pos][player_x_pos] = " B "
            num_bandits += 1
            num_chests -= 1
        display_grid(player_grid, height)
        print("Score: ", score)
        print("Number of Moves: ", total_moves)
        print("Number of Chests Remaining: ", num_chests)
        print("Number of Bandits on the map: ", num_bandits)


    if score == 100:
        print("Congratulations! You have won the game!")
    else:
        print("You have lost. Feel ashamed.")




def menu():
    cls()
    choice = ""
    while choice != "0":
        print("Welcome to AQA Treasure Hunt")
        print("MAIN MENU")
        print("-" * 50)
        print("\n(1)\tPlay Standard Game")
        print("\n(2)\tPlay Custom Game")
        print("\n(0)\tExit Program")

        # keep repeating the display of the menu until the user chooses to exit
        valid_choice = False
        while not valid_choice:
            # check to see that the user has entered 1, 2 or 0
            choice = input("Please Enter Your Choice:")
            if choice not in "120":
                print("Invalid Option, please select from either 1, 2 or 0")
            else:
                valid_choice = True
        # make selections based on the input
        if choice == "1":
            play_game(8,8,10,5)
            choice = ""
            input()
        elif choice == "2":
            print("PLAY CUSTOM GAME")
            width, height, num_chests, num_bandits  = select_custom_game()
            play_game(width, height, num_chests, num_bandits)
            choice = ""
            input()
    print("Exiting Program")


# don't forget that once you have defined a program, you will need to call it up in order for it to run!
menu()
