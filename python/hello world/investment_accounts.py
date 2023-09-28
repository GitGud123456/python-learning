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
        finished_acc = Acc_make(add,acc_bal)
        account_list.append(finished_acc)
        #print(print_Account(account_list[add-1].num,account_list[add-1].bal))

def print_all_acc():
    for account in range(len(account_list)):
        print_Account(account_list[account].num,account_list[account].bal)

def deposit(acc_num,new_bal):
    updated_info = edit_Account(int(acc_num)-1,int(new_bal),"deposit")
    return updated_info



def edit_Account(acc_num,new_bal,edit_type):
    if acc_num <= len(account_list):
        previous_bal = account_list[acc_num].bal
        if edit_type == "deposit":
            account_list[acc_num].bal += new_bal
            updated_bal = account_list[acc_num].bal
        elif edit_type == "withdrawal":
            account_list[acc_num].bal -= new_bal
            updated_bal = account_list[acc_num].bal  
    return  previous_bal,updated_bal,acc_num+1






if account_list == []:
        make_accounts()

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
        print_all_acc()
        input("Press ENTER to return to main menu")
    elif selection == "2":
        New_info = deposit(input("Enter Account #: "),input("Enter Deposit Amount: "))
        print(f'Account {New_info[2]} Previous Balance: ${New_info[0]}\nAccount {New_info[2]} New Balance: ${New_info[1]}')
        input("Press ENTER to return to main menu")
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