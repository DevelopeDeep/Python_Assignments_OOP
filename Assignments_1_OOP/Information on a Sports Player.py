class SportsPlayer:

    def __init__(self):
        self.name = input("Enter Name : ")
        self.age = int(input("Enter Age : "))
        self.height = int(input("Enter Height : "))
        self.weight = int(input("Enter Weight : "))

    def get_age(self):
        print("Player 1 : Name - {}, age is {} years ".format(self.name, self.age))

    def get_height(self):
        print("Player 1 : Name - {}, height is {}cm".format(self.name, self.height))

    def get_weight(self):
        print("Player 1 : Name - {}, weight is {}kg".format(self.name, self.weight))

def main():
    obj = SportsPlayer()

    obj.get_age()
    obj.get_height()
    obj.get_weight()

if __name__=="__main__":
    main()