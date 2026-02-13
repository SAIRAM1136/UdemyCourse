#Calculator program using Class and methods

class BasicCalculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

obj = BasicCalculator(10,5)
print("Addition : ",obj.add())
print("Subtraction : ",obj.sub())
print("Multiplication: ",obj.mul())
print("Division: ",obj.div())



def GreetUser(username):
    print("Hello " + username + "Welcome to the Python course.")

GreetUser("John !")

def CalculateAverage(num1, num2,num3):
    print("The average of 10,20,30 : ",num1+num2+num3 / 3)

CalculateAverage(10,20,30)





