class Person:


    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def sorting(self):

        print("firstname is : ", self.firstname)
        print("lastname is : ", self.lastname)
        print("age is : ", self.age)


def main():
    p1 = Person('Michael', 'Smith', 40)
    p2 = Person('Alice', 'Waters', 21)
    p3 = Person('Zoey', 'Jones', 29)


    # p1.sorting()
    # p2.sorting()
    # p3.sorting()

if __name__=="__main__":
    main()