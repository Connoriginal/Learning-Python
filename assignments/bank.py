#Bank Account

class BankAccount:

    __no_of_accounts = 0

    def __init__(self,name,balance=0):
        self.__name = name
        self.__balance = balance
        BankAccount.__no_of_accounts += 1
        print("A bank account for",self.__name,"is open.")
        print("Your current balance is",self.__balance,"won.")


    def __str__(self):
        return self.__name + "\'s BankAccount object"

    def show_balance(self):
        print(self.__name,"\'s balance is",self.__balance,"won.")

    def deposit(self,amount):
        amount = int(amount)
        if (amount >= 0):
            self.__balance += amount
            print(amount,"won has been succesfully deposited.")
            print(self.__name,"\'s balace is",self.__balance,"won.")
        else:
            print("Deoposit failed.")
            print(self.__name,"\'s balance is",self.__balance,'won.')

    def withdraw(self,amount):
        amount = int(amount)
        if not(amount < 0) and not(amount > self.__balance):
            self.__balance -= amount
            print(amount,"won has been successfully withdrawn.")
            print(self.__name,"\'s balance is",self.__balance,"won.")
        else:
            print("Withdrawn failed")
            print(self.__name,"\'s balance is",self.__balance,'won.a')

    @staticmethod
    def count_accounts():
        return BankAccount.__no_of_accounts
