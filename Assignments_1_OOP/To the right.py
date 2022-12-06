class Menu:

    def __init__(self):
        self.menu = [1, 2, 3]

    def to_the_right(self):
        print("to_the _right", self.menu)

    def Display(self):
        print("Display", self.menu[0])

def main():
    obj = Menu()
    obj.to_the_right()
    obj.Display()

if __name__=="__main__":
    main()