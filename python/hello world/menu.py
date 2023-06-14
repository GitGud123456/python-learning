# pytrhon menu loop
loop = True
while loop:
    #python print menu
    print("\nMAIN MENU")
    print("1: Option 1")
    print("2: Option 2")
    print("3: Option 3")
    print("4: EXIT")

    # Get Menu Selection from User

    selection = input("Enter Selection (1-4): ")


    # Take Action Based on Menu Selection

    if selection == "1":
        print("\nOption 1")
    elif selection == "2":
        print ("\nOption 2")
    elif selection == "3":
        print("\nOption 3")
    elif selection == "4":
        print("\nEXIT")
        loop = False