# AQA Treasure Hunt v.1.0 - Ian Richardson, 15 March 2018


def cls():
    print("\n" * 100)
    # this is a simple and quick way to get the screen to clear in between sections
    # of the program. I generally make this at the start of any project


def create_grid(width, height,contents):
    grid = []
    for x in range(height):
        grid.append([])
        for y in range(width):
            grid[x].append(contents)
    return grid


def display_grid(grid, height):
    print("-" * 32)
    for y in range(0, height):
        print("|"+"|".join(grid[y])+"|")
        print("-"*32)


def place_object(grid, object_symbol, num_object, width,height):
    from random import randint
    while num_object > 0:
        rand_x = randint(-1, width-1)
        rand_y = randint(-1, height-1)
        if grid[rand_y][rand_x] == "   ":
            grid[rand_y][rand_x] = " "+object_symbol+" "
            num_object -= 1
    return grid


def hide_objects(grid, num_chests, num_bandits,width,height):
    grid[7][0] = " * "
    grid = place_object(grid,"T",num_chests, width, height)
    grid = place_object(grid,"B",num_bandits,width,height)
    return grid

def play_standard_game():
    cls()
    width = 8
    height = 8
    hidden_grid = create_grid(width, height,"   ")
    hidden_grid = hide_objects (hidden_grid, 10, 5, width,height)
    player_grid = create_grid(width,height, "   ")
    counting_grid = create_grid(width, height, 0)
    display_grid(player_grid, height)



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
            play_standard_game()
            choice = ""
            input()
        elif choice == "2":
            print("PLAY CUSTOM GAME")
            choice = ""
            input()
    print("Exiting Program")


# don't forget that once you have defined a program, you will need to call it up in order for it to run!
menu()


