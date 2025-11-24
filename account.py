from storage import Storage
data = Storage()
Storage  = Storage()

user_data = data.load_accounts()

class Accounts:
    def __init__(self , card_id=0 , pin=0 , balance=0):
        self.card_id = card_id
        self.pin = pin
        self.balance = balance
        
    def withdraw(self):
        card_id = self.card_id
        balance = user_data[card_id]["balance"]
        while True:
            print("-"*30)
            print("WITHDRAW MONEY")
            print("-"*30)
            try:
                amount= int(input("Enter Amount (multiples of 100): "))
            except:
                print("⚠️ Please enter a correct input !" )
                break 

            if(amount%100!=0):
                print("⚠️ Please enter amount muliple of 100.")
            else:
                if(amount>balance):
                    print("❌ Insufficient funds. ")
                else:
                    print(f"✅ Transaction successful. New balance: {balance - amount}")

                    user_data[card_id]["balance"] = balance - amount
                    Storage.save_accounts(user_data)
                    break

    def deposit(self):
        card_id = self.card_id
        balance = user_data[card_id]["balance"]
        while True:
            print("-"*30)
            print("DEPOSIT MONEY")
            print("-"*30)
            amount= int(input("Enter Amount (multiples of 100): "))
            if(amount%100!=0):
                print("⚠️ Please enter amount muliple of 100.")
            else:
                print(f"✅ Transaction successful.")
                user_data[card_id]["balance"] = balance + amount
                Storage.save_accounts(user_data)
                break
    def check_balance(self):
        card_id = self.card_id
        balance = user_data[card_id]["balance"]
        print(f"💰  {balance}$")

    def change_pin(self):
        card_id = self.card_id        
        while True:
            print("-"*30)
            print("Change Pin")
            print("-"*30)
            try:
                new_pin= (input("Enter new pin : "))
            except:
                print("⚠️ Please enter a correct input !" )
                break 
            print("-"*30)
            try:
                conirm_pin = (input("Confirm new pin : "))
            except:
                print("⚠️ Please enter a correct input !" )
                break 
            if(new_pin != conirm_pin):
                print("new pin not match with confirm pin")
                break
            else:
                user_data[card_id]["pin"] = new_pin
                Storage.save_accounts(user_data)
                print("✅ Pin updated ")
                break

    def close_account(self):
        card_id = self.card_id
        user_data.pop(card_id)
        Storage.save_accounts(user_data)
        print("✅ done")

    def transfer_money(self):
        card_id = self.card_id
        balance = user_data[card_id]["balance"]
        while True:
            print("-" * 30)
            print("💰 Transfer money")
            print("-" * 30)
            try:
                amount = int(input("Enter Amount (multiples of 100): "))
            except:
                print("⚠️ Please enter a correct input !")
                break
            if (amount % 100 != 0):
                print("⚠️ Please enter amount muliple of 100.")
            else:
                if (amount > balance):
                    print("❌ Insufficient funds. ")
                else:
                    print("-" * 30)
                    try:
                        account_id = (input("Enter atm number of other bank account:"))
                    except:
                        print("⚠️ Please enter a correct input !")
                        break
                    if account_id == card_id:
                        print("⚠️ Please enter others account")
                    else:
                        if account_id not in user_data:
                            print("Invalid Card Number!")
                            return
                        user = user_data[account_id]

                        user["balance"] = user["balance"] + amount
                        user_data[card_id]["balance"] = user_data[card_id]["balance"] - amount
                        print("Transation done ✅")
                        Storage.save_accounts(user_data)
                        break
