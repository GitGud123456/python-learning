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
     
def rand_nick(n):
    num = random.randint(0,len(nick_list))
    return n[0] + " \"" + nick_list[num-1] + "\" " + n[1]

def show_all_nick(n):
    num = 1
    print(" ")
    for nick in nick_list:
        nick = str(num) + ": "+ str(n[0]) +" "+ str(nick) +" "+ str(n[1])
        print(nick)
        num += 1

def remove_nick(nick_num):
    if int(nick_num) <= len(nick_list):
        show_all_nick(split_Name)
        print("\nremoved: "+ nick_list[int(nick_num)-1] + "\n\nUpdated list: ")
        nick_list.remove(nick_list[int(nick_num)-1])
        show_all_nick(split_Name)
    else: print("Number entered greater than length of Nick List. Max acceptable Number:" + str(len(nick_list)))
    

global split_Name
split_Name = name(input("Enter Name:"))
print(split_Name[0] + " " + split_Name[1])

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
        split_Name = name(input("Enter New Name:"))
        print ("Name changed to:" + split_Name[0] +" "+ split_Name[1])
    elif selection == "2":
        print ("\nOption 2")
        print(rand_nick(split_Name))
    elif selection == "3":
        show_all_nick(split_Name)
        input("press ENTER to return to Main menu")
    elif selection == "4":
        add_nick(input("New Nickname:"))
    elif selection == "5":
        show_all_nick(split_Name)
        remove_nick(input("Enter the number of the nick you want to remove: "))
        input("press ENTER to return to Main menu")
    elif selection == "6":
        print("\nEXIT")
        loop = False
