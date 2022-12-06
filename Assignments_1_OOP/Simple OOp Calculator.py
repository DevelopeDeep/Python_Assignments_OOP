class Calculator:

    def __init__(self):
        self.number1 = float(input("Enter Number1 : "))
        self.number2 = float(input("Enter Number2 : "))

    def add(self):
        print("Addition of {} and {} is : ".format(self.number1, self.number2),self.number1 + self.number2)

    def subtract(self):
        Subtraction = self.number1 - self.number2
        print("Subtraction of {} and {} is : ", Subtraction)

    def multiply(self):
        Multiplication = self.number1 * self.number2
        print("Multiplication of {} and {} is: ", Multiplication)

    def divide(self):
        Division = self.number1 / self.number2
        print("Division of {} and {} is : ", Division)

def main():

    obj = Calculator()
    obj.add()
    obj.subtract()
    obj.multiply()
    obj.divide()

if __name__=="__main__":
    main()