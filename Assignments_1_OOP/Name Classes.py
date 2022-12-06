class Name:

    def __init__(self):
        self.fname = input("Enter First Name : ")
        self.lname = input("Enter Last Name : ")
        print("Your first Name is : ", self.fname.capitalize())
        print("Your Last Name is : ", self.lname.capitalize())

    def fullname(self):
        print("Your Fullname is : ", self.fname.capitalize() + ' ' + self.lname.capitalize())

    def initials(self):
        print("Your initial is : {}.{}".format(self.fname[0].capitalize(),self.lname[0].capitalize()))

def main():
    obj = Name()
    obj.fullname()
    obj.initials()

if __name__=="__main__":
    main()