from storage import Storage
from account import Accounts
from admin import  Admin
Storage  = Storage()
data = Storage.load_accounts()



class Main :
    def __init__(self):
        pass

def login_page():
    while True:
        print("="*30)
        print("WELCOME TO PYTHON ATM")
        print("="*30)
        print("1. Insert Card (Login)")
        print("2. Admin Login")
        print("3. Exit")
        print("-"*30)
        try:
            choice = int(input("Choose an option: "))
        except:
            print("⚠️ Please enter a correct input !" )
            break
        if choice == 1:
            user_login_page()
        elif choice ==2:
            admin_login()
        elif choice == 3:
            print("Thanks for using Py banking system , visit again")
            break
        else:
            print("Invalid choice Please try again")

def user_login_page():
    while True:
        print("-"*30)
        try: 
            card_id = str(input("Enter Card Number : "))
        except:
            print("⚠️ Please enter a correct input !" )
            break
        if card_id not in data:
            print("Invalid Card Number!")
            return
        user = data[card_id]
        print("-"*30)
        if user["locked"]:
          print("Your account is locked. Contact admin.")
          return
        try:
            pin = input("Enter PIN: ")
        except:
            print("⚠️ Please enter a correct input !" )
            break  

    # Validate PIN
        if pin == user["pin"]:
            print(f"\nWelcome {user['name']}!")
            user["attempts"] = 0   # reset attempts
            Storage.save_accounts(data)
            main_menu(card_id)

        else:
            print("Incorrect PIN!")
            user["attempts"] += 1
            attempts_left = 3- user["attempts"]
            print(attempts_left , " attempts left")

            # If 3 wrong attempts → lock account
            if user["attempts"] >= 3:
                user["locked"] = True
                print("Too many wrong attempts. Account locked!")

            Storage.save_accounts(data)

def main_menu(card_id):
    account = Accounts(card_id)
    print("="*30)
    print("Python atm machine menu")
    print("="*30)
    print("1. Withdraw money")
    print("2. Deposit money")
    print("3. Check balance")
    print("4. Change pin")
    print("5. Close account")
    print("6. Transfer money")
    print("7. Exit (Logout)")
    print("-"*30)
    try:
        choice = int(input("Choose an option: "))
    except:
        print("⚠️ Please enter a correct input !")
    if choice == 1:
        account.withdraw()
    elif choice ==2:
        account.deposit()
    elif choice ==3:
        account.check_balance()
    elif choice ==4:
        account.change_pin()
    elif choice ==5:
        account.close_account()
    elif choice ==6:
        account.transfer_money()
    elif choice == 7:
        print("Thanks for using Py banking system , visit again")
    else:
        print("Invalid choice Please try again")

def admin_login_page():
    admin = Admin()
    print("=" * 30)
    print("PYTHON ATM - MAIN MENU")
    print("=" * 30)
    print("1. Add user")
    print("2. Delete user")
    print("3. Unlock user")
    print("4. Exit (Logout)")
    try:
        choice = int(input("Choose an option: "))
    except:
        print("⚠️ Please enter a correct input !")
    if choice == 1:
        admin.add_user()
    elif choice == 2:
        admin.delete_user()
    elif choice == 3:
        admin.unlock_user()
    elif choice == 4:
        print("Thanks for using Py banking system , visit again")
    else:
        print("Invalid choice Please try again")


def admin_login():
    admin_data  = Storage.load_admin()
    print("-" * 30)
    try:
        username = str(input("Enter Admin Username : "))
    except:
        print("⚠️ Please enter a correct input !")
    if admin_data["username"] != username:
        return print("⚠️ Invalid Username")
    else:
        try:
            password = str(input("Enter Admin Password : "))
        except:
            print("⚠️ Please enter a correct input !")
        if admin_data["password"] != password:
            return print("⚠️ Invalid Password")
        else:
            admin_login_page()

login_page()
