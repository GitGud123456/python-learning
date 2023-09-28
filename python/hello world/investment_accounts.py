# PYTHON INVESTMENT ACCOUNTS ASSIGNMENT
import random
loop = True
global account_list
account_list = []

#Create Accounts
class Acc_make(object):
    def __init__(Acc,num,bal):
        Acc.num = num
        Acc.bal = bal

def make_accounts():
    for add in range(1,21,1):
        acc_bal = random.randint(0,5000)
        finished_acc = Acc_make(add,acc_bal)
        account_list.append(finished_acc)

def Account_Syntax(acc_num,acc_bal):
    return f"Account {acc_num}: ${acc_bal}"

#Print Accounts
def print_all_acc():
    print(" ")
    for account in range(0,len(account_list),1):
        print(Account_Syntax(account_list[account].num,account_list[account].bal))

#Edit Account(s)
def edit_Account(acc_num,new_bal,edit_type):
    if edit_type == "deposit" or edit_type == "withdrawal" and acc_num <= len(account_list):
        previous_bal = account_list[acc_num].bal
        if edit_type == "deposit":
            account_list[acc_num].bal += new_bal
            updated_bal = account_list[acc_num].bal
        elif edit_type == "withdrawal":
            if account_list[acc_num].bal < new_bal:
                return "\nSorry, insufficient funds.\n"
            account_list[acc_num].bal -= new_bal
            updated_bal = account_list[acc_num].bal
        return  previous_bal,updated_bal,acc_num+1
    elif edit_type == "CountUnder2000":
        num_less_than_2000 = []
        for acc in range(0,len(account_list),1):
            if account_list[acc].bal < 2000:
                num_less_than_2000.append(account_list[acc])
        return num_less_than_2000
    elif edit_type == "HackerAttack":
        stolen_amount = 0
        for acc in range(0,len(account_list),1):
            stolen_amount += account_list[acc].bal * .05
            account_list[acc].bal *= .95
        return stolen_amount
    
#Edit Options
def deposit(acc_num,new_bal):
    updated_info = edit_Account(int(acc_num)-1,int(new_bal),"deposit")
    print(f'\nAccount {updated_info[2]}\n Previous Balance: ${updated_info[0]}\n New Balance: ${updated_info[1]}\n')

def withdrawal(acc_num,new_bal):
    updated_info = edit_Account(int(acc_num)-1,int(new_bal),"withdrawal")
    if updated_info == "\nSorry, insufficient funds.\n":
        print(updated_info)
    else:
        print(f'\nAccount {updated_info[2]}\n Previous Balance: ${updated_info[0]}\n New Balance: ${updated_info[1]}\n')

def under2000():
    print("COUNT UNDER 2000\n")
    list_under2000 = edit_Account(0,0,"CountUnder2000")
    for under2000 in range(0,len(list_under2000),1):
        print(Account_Syntax(list_under2000[under2000].num,list_under2000[under2000].bal))
    print("Accounts with less than $2000: "+ str(len(list_under2000)))

def Generous_Donor():
    list_under2000 = edit_Account(0,0,"CountUnder2000")
    for under2000 in range(0,len(list_under2000),1):
        list_under2000[under2000].bal += 500
        #print(f'Account {list_under2000[under2000].num} Previous Balance: ${list_under2000[under2000].bal-500}\nAccount {list_under2000[under2000].num} New Balance: ${list_under2000[under2000].bal}\n')
        print(f'Account {list_under2000[under2000].num}:\n  Previous Balance: ${list_under2000[under2000].bal-500}\n  New Balance: ${list_under2000[under2000].bal}\n')

def Hacker_Attack():
    amount_stolen = edit_Account(0,0,"HackerAttack")
    print(f"HACKER ATTACK\nTotal Amount Stolen is ${amount_stolen}")

#initialize list
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

    selection = input("Enter Option #: ")

    if selection == "1":
        print_all_acc()
        input("Press ENTER to return to main menu")
    elif selection == "2":
        deposit(input("Enter Account #: "),input("Enter Deposit Amount: $"))
        input("Press ENTER to return to main menu")
    elif selection == "3":
        withdrawal(input("Enter Account #: "),input("Enter Withdrawal Amount: $"))
        input("Press ENTER to return to main menu")
    elif selection == "4":
        under2000()
        input("Press ENTER to return to main menu")
    elif selection == "5":
        Generous_Donor()
        input("Press ENTER to return to main menu")
    elif selection == "6":
        Hacker_Attack()
        input("Press ENTER to return to main menu")
    elif selection == "7":
        print("\nEXIT")
        loop = False