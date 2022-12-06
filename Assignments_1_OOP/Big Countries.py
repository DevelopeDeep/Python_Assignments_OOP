# class Country:
#
#     def __init__(self):
#         self.country = input("Enter Country : ")
#         self.population = int(input("Enter Population : "))
#         self.area = int(input("Enter Area : "))
#
#     def is_big(self):
#         if self.population > 250000000:
#             print("{}.is_big : {}".format(self.country, True))
#         elif self.area > 3000000:
#             print("{}.is_big : {}".format(self.country, True))
#
#         else:
#             print("{}.is_big : {}".format(self.country, False))
#
#     def Compare(self,contry, othrcomntry):
#         smaller = "smaller"
#         larger = "larger"
#         if self.population / self.area:
#             print(f'"{contry} has a {smaller} population density than {othrcomntry}"')
#         else:
#             print(f'"{contry} has a {larger} population density than {othrcomntry}"')
#
# def main():
#
#     Aus = Country()
#     Andora = Country()
#
#     Aus.is_big()
#     Andora.is_big()
#     Aus.Compare(Aus,Andora)
#
# if __name__=="__main__":
#     main()

# Enter Country1 : india
# Enter Population : 1300000000
# Enter Area : 3287263
# Enter Country1 : pakistan
# Enter Population : 230000000
# Enter Area : 796095



# Class as Country
# Instance Variables as population, area
# Instance Methods as is_big

class Country:
    def __init__(self):
        self.Name = input("Enter Country Name : ")
        self.Population = int(input("Enter Population : "))
        self.Area = int(input("Enter Area : "))

    def is_big(self):
        if self.Name == self.Population > 25000000 or self.Area > 3000000:
            print("True")
        else:
            print("False")

    def compares(self, country, othercountry):
        smaller = "smaller"
        larger = "larger"
        if self.Population < 25000000:
            print(f'{country} has a {smaller} population density than {othercountry}')
        else:
            print(f'{country} has a {larger} population density than {othercountry}')

def main():
    User1 = Country()
    User2 = Country()

    User1.is_big()
    User2.is_big()

    User2.compares(User2.Name, User1.Name)

if __name__ == "__main__":
    main()


# class Country:
# 	def __init__(self, Name, Population, Area):
# 		self.Name = Name
# 		self.Population = Population
# 		self.Area = Area
#
# 	def is_big(self):
# 		if self.Name == self.Population > 25000000 or self.Area > 3000000:
# 			print("True")
# 		else:
# 			print("False")
#
# 	def compares(self, Country, Other_Country):
# 		smaller = "smaller"
# 		larger = "larger"
# 		if self.Population < 25000000:
# 			print(f'{Country} has a {smaller} population density than {Other_Country}')
# 		else:
# 			print(f'{Country} has a {larger} population density than {Other_Country}')
#
# def main():
# 	Australia = Country("Australia", 43545500, 7692024)
# 	Andorra = Country("Andorra", 76098, 468)
#
# 	Australia.is_big()
# 	Andorra.is_big()
#
# 	Australia.compares("Australia", "Andorra")
#
#
# if __name__ == "__main__":
# 	main()