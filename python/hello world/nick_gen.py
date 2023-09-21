# pytrhon menu loop
import re
import random

name_list = []
nick_list = ['Crusher','the Scientist','Twinkle-toes','the Coder','the Jester','the Sloth','Quick-Silver']
decode_name_str = r'\w+'

def add_nick(New_n):
    nick_list.append(New_n)
    return "added New Nickname:" + New_n
def name(n):
    [first,last] = re.findall(decode_name_str,n)
    return [first,last]
     
def rand_nick(r):
    num = random.randint(0,len(nick_list))
    return r[0] + " \"" + nick_list[num] + "\" " + r[1]

def show_all_nick():
    num= 1
    for name in nick_list:

        print(name)

def remove_nick():
    nick_list.index()
global split_Name
split_Name = name(input("Enter Name:"))
print(split_Name[0] + " " + split_Name[1])

loop = True
while loop:
    
    #python print menu
    print("\nMAIN MENU")
    print("1: Enter Name/Change Name")
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
        
        split_Name = name(input("Enter New Name:"))
        print ("Name changed to:" + split_Name[0] +" "+ split_Name[1])
    elif selection == "2":
        print ("\nOption 2")
        print(rand_nick(split_Name))
    elif selection == "3":
        show_all_nick()
    elif selection == "4":
        add_nick(input("New Nickname:"))
    elif selection == "5":
        print("\nOption 5")
    elif selection == "6":
        print("\nEXIT")
        loop = False
