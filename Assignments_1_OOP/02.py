# Class = Laptop
# instance variable = brand, model, price
import select


class Laptop:
    Discount = 10.5

    def __init__(self):
        self.brand = input("Enter Brand :")
        self.model = input("Enter Model :")
        self.price = int(input("Enter Price :"))

    def Desplayinfo(self):
        print("Laptop Brand is : ", self.brand)
        print("Laptop model is : ", self.model)
        print("Laptop Price Rs : ", self.price)

    def DisplayDiscount(self):
        self.Discount = self.price * self.Discount / 100
        self.price = self.price - self.Discount

        print("Save Discount Rs : ", self.Discount)
        print("Laptop Price After Discount is : ", self.price)

def main():

    User1 = Laptop()

    User1.Desplayinfo()

    User1.DisplayDiscount()


if __name__=="__main__":
    main()
