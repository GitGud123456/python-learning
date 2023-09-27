# pytrhon menu loop
import random
loop = True
global account_list
account_list = []



def print_Account(acc_num,acc_bal):
    
    return f"Account {acc_num}: ${acc_bal}"

class Acc_make(object):
    def __init__(Acc,acc_num,acc_bal):
        Acc.num = acc_num
        Acc.bal = acc_bal

#for att in dir(Acc):
 #   print(att, getattr(Acc,num))




def make_accounts():
    for add in range(1,21,1):
        
        acc_bal = random.randint(0,5000)
        #print(print_Account(add,acc_bal))
        finished_acc = Acc_make(add-1,acc_bal)
        account_list.append(finished_acc)
        #print(finished_acc.num)
        account_list.append(finished_acc)
        print(account_list[add-1].num)

def deposit(acc_num,new_bal):
    account_list[acc_num]










while loop:
    #python print menu
    print("\nMAIN MENU")
    print("1: Print Accounts")
    print("2: Deposit")
    print("3: Withdrawal")
    print("4: Count Under $2000")
    print("5: Generous Doner")
    print("6: Hacker Attack")
    print("7: EXIT")

    # Get Menu Selection from User

    selection = input("Enter Selection #: ")



    # Take Action Based on Menu Selection

    if selection == "1":
        make_accounts()
    elif selection == "2":
        print ("\nOption 2")
    elif selection == "3":
        print("\nOption 3")
    elif selection == "4":
        print("\nOption 4")
    elif selection == "5":
        print("\nOption 5")
    elif selection == "6":
        print("\nOption 6")
    elif selection == "7":
        print("\nEXIT")
        loop = False