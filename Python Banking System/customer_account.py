
class CustomerAccount:
    def __init__(self, fname, lname, address, account_no, balance, account_type, Interest_rate, Overdraft_limit):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)
        self.account_type = account_type
        self.interest_rate = Interest_rate
        self.overdraft_limit = Overdraft_limit
    
    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address = addr
        
    def get_address(self):
        return self.address
    
    def deposit(self, amount):
        self.balance+=amount
        print("\n Amount successfuly deposited: %.2f" %self.balance)
        
    def withdraw(self, amount):
        
        #fixed withdraw option.
        if self.balance >= amount:
            self.balance -= amount
            print("\nWithdrawal successful. Remaining balance: %.2f" % self.balance)
        else:
            print("Insufficient Balance.")        
    
        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def get_account_type(self):
        self.account_type = account_type
    
    def get_interest_rate(self):
        self.interest_rate = interest_rate
        
    def get_Overdraft_limit(self):
        self.Overdraft_limit = Overdraft_limit
    
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    def print_details(self):
        
        #Fixed print details.
        print("--Customer Details--")
        print("fname: ",self.fname)
        print("lname: ", self.lname)
        print("Address: " , ", ".join(self.address))
        print("Account No: ", self.account_no)
        print("Balance: %.2f" %self.balance)
    
   
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                
                #Fixed deposit options
                try:
                    amount = float(input("\nEnter the amount to deposit: "))
                    self.deposit(amount)
                    self.print_balance()
                except ValueError:
                    print("Please enter a valid amount to deposit")
            
            
            elif choice == 2:
                
                #Fixed amount withdraw.
                try:
                    amount = float(input("Enter the amount to withdraw: "))
                    self.withdraw(amount)
                    self.print_balance()
                except ValueError:
                    print("Please enter a valid amount to withdraw.")
            
            
            elif choice == 3:
                
                #Fixed to print balance.
                self.print_balance()
            
            
            elif choice == 4:
                
                 #Fixed the customer name update. 
                fname=input("\n Enter new customer first name: ")
                self.update_first_name(fname)
                sname = input("\nEnter new customer last name: ")
                self.update_last_name(sname)
                print("\nName updated successfully.")
           
            
            elif choice == 5:
                
                #Fixed address update. 
                new_address = input("Enter the new address (comma-separated): ").split(",")
                self.update_address(new_address)
                print("\nAddress updated successfully.")
            
            
            elif choice == 6:
                self.print_details()
            elif choice == 7:
                loop = 0
        print ("\n Exit account operations")