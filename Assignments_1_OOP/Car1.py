class Vehicle:
    Wheels = 4

    def __init__(self):
        self.Type = input("Enter Vehicle Type : ")
        self.Color = input("Enter Vehicle Color : ")
        self.Speed = input("Enter Vehicle Speed : ")

    def DisplayVehicleInfo(self):
        print("Car Details of Vehicle is:\nType is : {}\nColor is : {}\nSpeed is : {}"
              .format(self.Type, self.Color, self.Speed))

def main():

    obj = Vehicle()
    obj.DisplayVehicleInfo()

if __name__ == "__main__":
    main()
