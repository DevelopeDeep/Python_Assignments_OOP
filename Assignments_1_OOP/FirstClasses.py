# class Employee:
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
#
#     def fullname(self):
#         return '{} {}\n{} {}'.format(self.first, self.last, self.email, self.pay)
#
# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'Employee', 60000)
# print(emp_1.fullname())
# # print(emp_1.email, emp_1.pay)
# # print(emp_1.pay)

print("____________________Restart_______________________")

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}\n{}\n{}'.format(self.first, self.last, self.email, self.pay)

emp_1 = Employee(input('first : '), input('last : '), int(input("pay : ")))
emp_2 = Employee('Test', 'Employee', 60000)
print(emp_1.fullname())
# print(emp_1.email, emp_1.pay)
# print(emp_1.pay)
