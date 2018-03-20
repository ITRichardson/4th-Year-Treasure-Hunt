# AQA Treasure Hunt v.1.0 - Ian Richardson, 15 March 2018

def cls():
    print("\n" * 100)
    # this is a simple and quick way to get the screen to clear in between sections
    # of the program. I generally make this at the start of any project


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
            print("PLAY GAME")
            choice = ""
            input()
        elif choice == "2":
            print("PLAY CUSTOM GAME")
            choice = ""
            input()
    print("Exiting Program")


# don't forget that once you have defined a program, you will need to call it up in order for it to run!
menu()


