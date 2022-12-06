class Employee:

    def __init__(self):
        self.fullname = input("Enter FullName : ")
        self.email = (self.fullname.replace(" ",".").lower())
        self.firstname = self.fullname.split()[0]

    def EmployeeDetails(self):
        print("Employee First Name is : ", self.firstname)
        print("Employee fullName is : ", self.fullname)
        print("Employee fullname is : {}, and his/her mail id is - {}@gmail.com".format(self.fullname,self.email))

def main():
    obj = Employee()
    obj.EmployeeDetails()

if __name__=="__main__":
    main()