import json
class Storage:
    def __init__(self , data = None ):
        self.data = data or {}

    def load_accounts(self):
        try:
            with open("accounts.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print("File not found! ")
        
    def save_accounts(self , data):
        with open("accounts.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_admin(self):
        try:
            with open("admin.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print("File not found! ")

    def save_admin(self, data):
        with open("admin.json", "w") as f:
            json.dump(data, f, indent=4)