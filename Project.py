import time

class Users:
    def __init__(self):
        self.users = {}
    
    def create_user(self,username,password,email,balance=0):
        if username in self.users:
            time.sleep(2)
            print("Username already exists. Please choose a different username.")
            return False
        else:
            self.users[username]={"password": password,
                                    "balance": balance,
                                    "email": email,
                                    "transaction_history": []}
            time.sleep(2)
            print("Signed up successfully. Use these credentials to login")
            return True
        
    def login(self,username,passwd):
        if username in self.users:
            if self.users[username]["password"]==passwd:
                time.sleep(2)
                return True
            else:
                time.sleep(2)
                print("Invalid credentials")
                return False
        else: 
            time.sleep(2)
            print("Invalid credentials")
            return False


class ATM:
    def __init__(self,users):
        self.users=users

    def check_balance(self,username,passwd):
        if self.users.login(username,passwd):
            return self.users.users[username]["balance"]
        else:
            return None

    def deposit(self,username,passwd,amount):
        if self.users.login(username,passwd):
            self.users.users[username]["balance"]+=amount
            self.users.users[username]["transaction_history"].append(f"Deposited ${amount}")
            time.sleep(2)
            print("Deposit successful")
            print(f"New balance is ${self.users.users[username]['balance']}")
        
    def transfer(self,sender,passwd,recieve,amount):
        if self.users.login(sender,passwd):
            sender_balance=self.users.users[sender]["balance"]
            if sender_balance>=amount:
                if recieve in self.users.users:
                    self.users.users[sender]["balance"]-=amount
                    self.users.users[sender]["transaction_history"].append(f"Transferred ${amount} to {recieve}")
                    self.users.users[recieve]["balance"]+=amount
                    self.users.users[recieve]["transaction_history"].append(f"Received ${amount} from {sender}")
                    time.sleep(2)
                    print("Transfer successful")
                    print(f"New balance for {sender} is ${self.users.users[sender]['balance']}")
                else:
                    time.sleep(2)
                    print(f"No such username {recieve} found.")
                    print("Transaction failed")
            else:
                time.sleep(2)
                print("Insufficient balance for transfer")
                print("Transcation failed")

    def withdraw(self,username,passwd,amount):
        if self.users.login(username,passwd):
            if self.users.users[username]["balance"]>=amount:
                self.users.users[username]["balance"]-=amount
                self.users.users[username]["transaction_history"].append(f"Withdrew ${amount}")
                time.sleep(2)
                print("Withdrawal successful.")
                print(f"New balance is ${self.users.users[username]['balance']}")
            else:
                time.sleep(2)
                print("Insufficient balance")
        
    def view_transaction_history(self,username,passwd):
        if self.users.login(username,passwd):
            time.sleep(2)
            print("Transaction History:")
            for transaction in self.users.users[username]["transaction_history"]:
                print(transaction)

    def delete_user(self,username,passwd):
        if self.users.login(username,passwd):
            time.sleep(2)
            del self.users.users[username]
            time.sleep(2)
            print("Account for user",username,"closed successfully")
       

def main():
    customer = Users()
    atm = ATM(customer)

    while True:
        time.sleep(2)
        print("\n= = = = = = = = = = = = = = Banking interface = = = = = = = = = = = = = =")
        print()
        print("Welcome!")
        print("1. Signup")
        print("2. Login")
        print("3. Quit interface")
        usrsel=int(input("Select your choice [1,2,3]: "))

        if usrsel == 1:
            time.sleep(2)
            name=input("Enter your name: ")
            passwd=input("Enter your password: ")
            email=input("Enter your email: ")
            balance=float(input("Enter your opening balance (minimum of 5000): "))
            while balance<5000:
                print("Minimum balance is 5000.")
                balance=float(input("Enter your opening balance (minimum of 5000): "))
            customer.create_user(name,passwd,email,balance)
        
        elif usrsel == 2:
            time.sleep(2)
            name=input("Enter your name: ")
            passwd=input("Enter your password: ")
            if customer.login(name, passwd):
                while True:
                    print()
                    time.sleep(2)
                    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
                    print(f"Welcome {name}!")
                    print(f"Logined as {name}")
                    print(f"Email: {email}")
                    print("\nPlease choose selection")
                    print("1. Check current balance")
                    print("2. Deposit amount")
                    print("3. Withdraw amount")
                    print("4. Transaction history")
                    print("5. Transfer amount")
                    print("6. Logout")
                    print()
                    sel=int(input("Enter your selection [2,3,4,5,6]: "))

                    if sel == 1:
                        balance=atm.check_balance(name,passwd)
                        if balance is not None:
                            print("Balance:", balance)

                    elif sel == 2:
                        amount=float(input("Enter an amount to be deposited: "))
                        atm.deposit(name,passwd,amount)

                    elif sel == 3:
                        amount=float(input("Enter an amount to be withdrawn: "))
                        atm.withdraw(name,passwd,amount)

                    elif sel == 4:
                        atm.view_transaction_history(name,passwd)

                    elif sel == 5:
                        recieve=input(f"Enter the reciever's username: ")
                        amount=float(input("Enter the amount to be transfered: "))
                        atm.transfer(name,passwd,recieve,amount)

                    elif sel == 6:
                        print(f"Logging out {name}")
                        print("See you soon!")
                        break

                    else:
                        print("Invalid selection.")

        elif usrsel == 3:
            print("Exiting interface.")
            exit()

        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()

# Code by Ajith Kumar