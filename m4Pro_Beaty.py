#
#Tristan Beaty
#10-7-24

import funcs as fun


def main():

    restart = 0
    while restart != 1:
        userMenu = fun.menu()
        valid = userMenu
        if valid < 1 or valid > 5:
            print()
            print("ERROR, Invalid input. Please enter the number of a menu option.")
            print()
    
        if userMenu == 1:
            print()
            fun.totalDisplay()
            restart = fun.exit()
    
        elif userMenu == 2:
            print()
            fun.authorLookup()
            restart = fun.exit()

        elif userMenu == 3:
            print()
            fun.bookLook()
            restart = fun.exit()

        elif userMenu == 4:
            print()
            fun.priceRange()
            restart = fun.exit()

        elif userMenu == 5:
            print()
            restart = fun.exit()
    
    print("Terminating Program...")
    input("Press enter/return to close")


if __name__ == "__main__":
    main()