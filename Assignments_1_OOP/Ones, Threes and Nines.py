class Math:

    def __init__(self):
        lst = []
        size = int(input("Enter length of list : "))
        for i in range(0, size):
            num = int (input(" Enter number : "))
            lst.append(num)
        print(lst)

        self.ones = lst.count(1)
        self.threes = lst.count(3)
        self.nines = lst.count(9)

    def one_threes_nines(self):
        print("ones are : ", self.ones)
        print("Threes are : ", self.threes)
        print("Nines are : ", self.nines)

def main():

    obj = Math()
    obj.one_threes_nines()

if __name__=="__main__":
    main()

