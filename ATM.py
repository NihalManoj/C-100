class Atm():
    def __init__(self, name, accNum):
        self.name = name
        self.accNum = accNum
        self.balance = 2000
    def displayDetails(self):
        print("Name- ", self.name)
        print("Account Number- ", self.accNum)
        print("Current Balance- ", str(self.balance))
    def deposit(self, money):
        self.balance = self.balance + money
    def withdrawal(self, money):
        self.balance = self.balance - money
    
Nihal = Atm("Nihal", "12345678")
Nihal.deposit(3000)
Nihal.displayDetails()
Nihal.withdrawal(4000)
Nihal.displayDetails()