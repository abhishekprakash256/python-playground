"""
testing the encaplusation in python

use the "__" in the variable to hide and make private 
"""





class BankAccount():

    def __init__(self,account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self,amount):

        if amount < 0 :

            return False

        self.__balance += amount

    
    def withdraw(self,amount) :

        if amount > self.__balance:
            
            print("Not sufficent Funds")
            
            return False

        self.__balance -= amount

        print(f"Balance remain {self.__balance__}" )

        return True
    
    def get_balance(self):

        return self.__balance
    
    def get_account_number(self):

        return self.__account_number
    




#test the code

account = BankAccount(123435345 , 5000)



print(account.get_account_number())

print(account.get_balance())

#the data is not printed 
print(account.__balance)