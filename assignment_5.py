
# Challenge 1: Square Numbers and Return Their Sum
class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
z = int(input("Enter the value of z: "))

obj = point(x, y, z)
print(obj.sqSum()) 

#<<<<---------------------------------------------------------------------->>>>
#Challenge 2: Implement a Calculator Class
class Calculator:
    def __init__(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            raise ValueError("Cannot divide by zero.")

calculator = Calculator()

result_addition = calculator.add()
result_subtraction = calculator.subtract()
result_multiplication = calculator.multiply()
result_division = calculator.divide()

print("Addition:", result_addition)
print("Subtraction:", result_subtraction)
print("Multiplication:", result_multiplication)
print("Division:", result_division)

#<<<<-------------------------------------------------------------------------->>>>
#Challenge 3: Implement the Complete Student Class

class Student:
    def __init__(self):
        self.__name = None
        self.__roll_number = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def roll_number(self):
        return self.__roll_number

    @roll_number.setter
    def roll_number(self, value):
        self.__roll_number = value

student = Student()
name = input("Enter the student's name: ")
student.name = name
roll_number = input("Enter the student's roll number: ")
student.roll_number = roll_number
name = student.name
roll_number = student.roll_number
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")

#<<<--------------------------------------------------------------------->>>>>>>>>
#CHALLANGE - 4  IMPLEMENT A BANKING ACCOUNT

class Account:
    def _init_(self,title,balance):
        self.title = title
        self.balance = balance
class savingsaccount(Account):
    def _init_(self,title,balance,interest_rate):
        super()._init_(title,balance)
        self.interest_rate = interest_rate
title = input()
balance = int(input())
interest_rate = int(input())
account_2 = savingsaccount(title,balance,interest_rate)
print("account title:",account_2.title)
print("account balance:",account_2.balance)
print("account interest",account_2.interest_rate)


#<<<<<------------------------------------------------------------------------>>>>
#CHALLANGE - 5  HANDLING A BANK ACCOUNT

class Account:
    def _init_(self, title, balance):
        self.title = title
        self.balance = balance
        
    def withdrawal(self, amount):
        self.balance -= amount 
    
    def deposit(self, amount):
        self.balance += amount       
    
    def getBalance(self):
        return self.balance
    
class SavingsAccount(Account):
    def _init_(self, title=None, balance =0, interestRate=0):
        super()._init_(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return self.balance * self.interestRate / 100
  
demo1= SavingsAccount("Alex", 35000, 7)
print(demo1.interestAmount())