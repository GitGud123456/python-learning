# pytrhon menu loop
loop = True
global ranking_List
ranking_List = []



print_Ranks = lambda rank,data: print(f"{rank}: {data}")

def printList():
    if len(ranking_List) > 0:
        ranking_List.sort(key=lambda obj : obj.rank)
        for item in ranking_List:
            print_Ranks(item.rank,item.data)
    else: print("\nNo Items in the Rank List")

#Create Accounts
class item_make(object):
    def __init__(item,rank,data):
        item.rank = rank
        item.data = data

def add_to_End(data):
        placement = len(ranking_List) + 1
        finished_object = item_make(placement,data)
        ranking_List.append(finished_object)

def Remove_last():
    removed = ranking_List.pop()
    return f"{removed.data} removed from end of list."

def insert_item(num,data):
    finished_object = item_make(num,data)
    for item in ranking_List:
        print(item.rank,item.data)
        if item.rank >= num:
            item.rank +=1
    ranking_List.insert(num-1,finished_object)

def remove_atPosition(num):
    print(f"{ranking_List[num-1]} Removed from position {num}")
    ranking_List.pop(num-1)
    for item in ranking_List:
        if item.rank >= num:
            item.rank -=1

def move_to_position(oldL,newL):
    # print(f"move Item form: {oldL}\nMove Item to: {newL}")
    data = ranking_List[oldL-1].data
    remove_atPosition(oldL)
    insert_item(newL,data)

def edit_item(num,new_data):
    ranking_List[num-1].data = new_data

while loop:
    #python print menu
    print("\nMAIN MENU")
    print("1: Print List")
    print("2:  Add item to End")
    print("3: Remove Last Item")
    print("4: Insert at Position")
    print("5: Remove at Position")
    print("6: Move to Position")
    print("7: Edit Item")
    print("8: EXIT")

    # Get Menu Selection from User

    selection = input("Enter Selection (1-8): ")
    # Take Action Based on Menu Selection

    if selection == "1":
        printList()
        input("Press ENTER to Return to Main Menu")
    elif selection == "2":
        add_to_End(input("ADD ITEM TO END\nEnter item: "))
    elif selection == "3":
        print(Remove_last())
    elif selection == "4":
        insert_item(int(input("Insert Position: ")),input("Item to Insert: "))
    elif selection == "5":
        remove_atPosition(int(input("Reomve Position: ")))
    elif selection == "6":
        move_to_position(int(input("move Item form: ")),int(input("Move Item to: ")))
    elif selection == "7":
      edit_item(int(input("Enter Position: ")),input("Replace with: "))
    elif selection == "8":
        print("\nEXIT")
        loop = False