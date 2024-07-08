
from customer_account import CustomerAccount
from admin import Admin


accounts_list = []
admins_list = []

class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()
        
    
    def load_bank_data(self):
        
        # Added value for account_type, interest_rate and overdraft.
        account_no = 1234
        customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00, "Saving_account", 0.06, 1000.00)
        self.accounts_list.append(customer_1)
        
        account_no+=1
        customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no, 3200.00, "Current_account", 0.03, 500.00)    
        self.accounts_list.append(customer_2)

        account_no+=1
        customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no, 18000.00, "Saving_account", 0.05, 1600.00)
        self.accounts_list.append(customer_3)

        account_no+=1
        customer_4 = CustomerAccount("Ali", "Abdallah",["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], account_no, 40.00, "Current_account", 0.02, 400.00)
        self.accounts_list.append(customer_4)
                
        # create admins
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
        self.admins_list.append(admin_1)

        admin_2 = Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
        self.admins_list.append(admin_2)


    def search_admins_by_name(self, admin_username):
        
        #fixed search admin by name
        found_admin = None
        for a in self.admins_list:
            username = a.get_username()
            if username == admin_username:
                found_admin = a
                break
        if found_admin == None:
            print("\n The Admin %s does not exist! Try again...\n" %admin_username)
        return found_admin         
    
        
        
    def search_customers_by_name(self, customer_lname):
        
        #Fixed Search customer by name.
        found_customer = None
        for customer in self.accounts_list:
            if customer.lname == customer_lname:
                return customer
                break
        if found_customer is None:
            print("Please enter a proper name")
        else:
            return      
    
        
        
    def search_customers_by_account_no(self, account_no):
        
        #added new method for delete account no.
        found_customer = None
        for customer in self.accounts_list:
            if customer.account_no == account_no:
                found_customer = customer
                break
        return found_customer
    
    def get_customer_account(self,account_number):
        for customer_account in self.accounts_list:
            if customer_account.get_account_no() == account_number:
                return customer_account
            else:
                return
    
    def admin_management_report(self):
        
        #created new admin management report.
        No_of_customers = len(self.accounts_list)
        total_amount_in_accounts = sum(customers.balance for customers in self.accounts_list)
        total_interest_rate = sum(customer.balance * customer.interest_rate for customer in self.accounts_list)
        total_overdraft = sum(customer.overdraft_limit for customer in self.accounts_list if customer.account_type == "Current_account")
        
        print ("--------------------")
        print ("Management Report")
        print ("-------------------")
        print (f"a) Total no of customers list: {No_of_customers}")
        print (f"b) Total amount in customers accounts: {total_amount_in_accounts}")
        print (f"c) Total interest_rate payable to all accounts for one year: {total_interest_rate}")
        print (f"D) Total amount of overdrafts currently taken by all customers: {total_overdraft}")
        print (" ")
        

    def main_menu(self):
        
        #Added error handling for main menu.
        try:
            print()
            print()
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("Welcome to the Python Bank System")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("1) Admin login")
            print ("2) Quit Python Bank System")
            print (" ")
            option = int(input ("Choose your option: "))
            
            if option != 1 and option != 2:
                raise ValueError               
            return option
        except ValueError:
            print("Invalid option. Please enter option (1 OR 2)")
            
    
        
    def run_main_options(self):
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        print ("\n Thank-You for stopping by the bank!")


    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, sender_account_no, amount):
        
        #Fixed trnsfer money issue.
        sender = self.search_customers_by_name(sender_lname)
        receiver = self.search_customers_by_name(receiver_lname)
        
        if sender is None:
            print("sender is not found")
        elif receiver is None:
            print("Receiver is not found")
        elif sender.balance < amount:
                print("Insufficient balance")
        elif sender.account_no != sender_account_no:
            print("Please enter valid sender account" , sender_account_no, "Expected: ", sender.account_no)  
        elif receiver.account_no != receiver_account_no:
            print("Please enter valid receiver account no" , receiver_account_no, "Expected: ", receiver.account_no)
        else:
            sender.withdraw(amount)
            receiver.deposit(amount)
            print("Your transaction was successful.")
        
    

                
    def admin_login(self, username, password):
        
        #Fixed admin login
        found_admin = self.search_admins_by_name(username)
        msg = "\n Login failed"
        if found_admin != None:
            if found_admin.get_password() == password and found_admin.get_username() == username:
                msg = "\n Login successful"
                return msg, found_admin
        return msg, None
    

    def admin_menu(self, admin_obj):
        
        #added error handling to prevent output errors.
        try:
    
            print (" ")
            print ("Welcome Admin %s %s : Avilable options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("1) Transfer money")
            print ("2) Customer account operations & profile settings")
            print ("3) Delete customer")
            print ("4) Print all customers detail")
            print ("5) update admin name: %s %s" %(admin_obj.get_first_name(), admin_obj.get_last_name()))   #created admin name update
            print ("6) update admin address %s" %(admin_obj.get_address()))  #created admin address update
            print ("7) Management report")
            print ("8) Sign out")
            print (" ")
            option = int(input ("Choose your option: "))
            return option
            if len(option) > 9:
                raise ValueError
        except ValueError:
            print("Invalid option, Please try again.")


    def run_admin_options(self, admin_obj):                                
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            
            #added error handling here for sender,receiver,account_no
            if choice == 1:
                try:
                    sender_lname = input("\n Please input sender surname: ")
                    receiver_lname = input("\n Please input receiver surname: ")
                    sender_account_no = int(input("\n Please input sender account number: "))  
                    receiver_account_no = int(input("\n Please input receiver account number: ")) 
                except ValueError:
                    print("Please enter the valid names and account no.")
                    
                #added error handling for amount.
                try:
                    amount = float(input("\n Please input the amount to be transferred: "))
                except ValueError:
                    print("Invalid amount. Please enter a valid amount.")    #fixed value error.
                    continue
                self.transferMoney(sender_lname, receiver_lname, receiver_account_no, sender_account_no, amount)  
                                  
            elif choice == 2:
                
                #fixed to print customer options.
                customer_lname = input("\n please enter customer surname here: ")
                customer = self.search_customers_by_name(customer_lname)
                if customer is not None:
                    customer.run_account_options()
                else:
                    print("Customer not found.")
            
            
            elif choice == 3:
                
                #Created delete option for the customer account.
                account_no = int(input("Enter the account number of the customer to delete: "))
                found_customer = self.search_customers_by_account_no(account_no)
                if found_customer is not None:
                    self.accounts_list.remove(found_customer)
                    print("Customer account removed successfully.")
                else:
                    print("Enter a valid account no.")
            
            
            elif choice == 4:
                
                #added option to print all accounts details.
                app.print_all_accounts_details()
            
            
            elif choice == 5:
                
                # created option for admin name update.
                admin_fname = input("Enter new admin first name: ")
                admin_obj.update_first_name(admin_fname)
                admin_lname = input("Enter new admin last name: ")
                admin_obj.update_last_name(admin_lname)
                print("\n Name updated successfully")
            
            
            elif choice == 6:
                
                #created option for admin address update.
                admin_address = input("Enter new admin address (comma-separated): ").split(",")
                admin_obj.update_address(admin_address)
                print(admin_address, "\n admin address updated successfully")
            
            
            elif choice == 7:
                
                #added option for admin management report.
                app.admin_management_report()
            
            elif choice == 8:
                loop = 0
            print ("\n Exit account operations")


    def print_all_accounts_details(self):
            i = 0
            for c in self.accounts_list:
                i+=1
                print('\n %d. ' %i, end = ' ')
                c.print_details()
                print("------------------------")



app = BankSystem()
app.run_main_options()
