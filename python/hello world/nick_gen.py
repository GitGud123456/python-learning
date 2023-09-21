# pytrhon menu loop
loop = True
while loop:
    #python print menu
    print("\nMAIN MENU")
    print("1: Change Name")
    print("2: Display a Random Nickname")
    print("3: Display All Nicknames")
    print("4: Add a Nickname")
    print("5: Remove a Nickname")
    print("6: EXIT")

    # Get Menu Selection from User

    selection = input("Enter Selection (1-6): ")


    # Take Action Based on Menu Selection

    if selection == "1":
        print("\nOption 1")
    elif selection == "2":
        print ("\nOption 2")
    elif selection == "3":
        print("\nOption 3")
    elif selection == "4":
        print("\nOption 4")
    elif selection == "5":
        print("\nOption 5")
    elif selection == "6":
        print("\nEXIT")
        loop = False