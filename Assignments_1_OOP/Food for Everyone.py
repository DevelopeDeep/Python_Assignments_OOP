class Person:

    def __init__(self):
        self.Name = input("Enter Name : ")
        self.food = input("Enter Food : ")

    def taste(self):
        if self.food in ["apple", "mango", "banana"]:
            print("{} Eat the {} and loves it!".format(self.Name, self.food))

        elif self.food in ["Carrot", "bringal", "strabbery"]:
            print("{} Eat the {} and hate it!".format(self.Name, self.food))

        else:
            print("{} Eat the {}!".format(self.Name, self.food))

def main():

    obj = Person()
    obj.taste()

if __name__=="__main__":
    main()