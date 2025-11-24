from account import user_data
from storage import  Storage
import random
storage = Storage()
user_data = storage.load_accounts()

def generate_random():
    random_no = random.randint(1000, 9999)
    return random_no

class Admin:
    def __init__(self):
        pass

    def add_user(self):
        print("-" * 30)
        print("Add user")
        print("-" * 30)
        try:
            name = (input("Enter your name :"))
            balance = int(input("Enter Amount to deposite first time (multiples of 100): "))
            pin = int(input("Enter 4 digit pin :"))
        except:
            print("⚠️ Please enter a correct input !")
        card_no = generate_random()

        new_user_details={
            "name": name,
            "pin": pin,
            "balance": balance,
            "locked": False,
            "attempts": 0
        }
        user_data[card_no] = new_user_details
        storage.save_accounts(user_data)

        print("User added successfully ✅  card number => " , card_no)
    def delete_user(self):
        try:
            card_id = str(input("Enter Card Number : "))
        except:
            print("⚠️ Please enter a correct input !")
        if card_id not in user_data:
            print("Invalid Card Number!")
            return
        print("⚠️ Please enter a correct input !")
        user_data.pop(card_id)
        storage.save_accounts(user_data)
        print("✅ done")

    def unlock_user(self):
        try:
            card_id = str(input("Enter Card Number : "))
        except:
            print("⚠️ Please enter a correct input !")
        if card_id not in user_data:
            print("Invalid Card Number!")
            return
        user_data[card_id]["locked"] = True
        user_data[card_id]["attempts"] = 0
        storage.save_accounts(user_data)
        print("Done ✅")