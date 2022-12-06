class Employee:

    def __init__(self,firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def from_string(self):

        print("Emp first name : ", self.firstname)
        print("Emp lastname : ", self.lastname)
        print("Emp salary is : ", self.salary)


def main():

    emp1 = Employee("Mary", "Sue", 60000)
    emp2 = Employee.from_string("John-Smith-55000")

if __name__=="__main__":
    main()
