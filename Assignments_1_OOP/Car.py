
class Car(object):

        def __init__(self, fuelEfficiency=0, fuelCapacity=0, fuelLevel=0, odometer=0):
            self.setCar(fuelEfficiency, fuelCapacity, fuelLevel, odometer)

        def setFuelEfficiency(self, newFuelEfficiency):
            self.setCar(fuelEfficiency=newFuelEfficiency)

        def setFuelCapacity(self, newFuelCapacity):
            self.setCar(fuelCapactity=newFuelCapacity)

        def setFuelLevel(self, newFuelLevel):
            self.setCar(fuelLevel=newFuelLevel)

        def setOdometer(self, newOdometer):
            self.setCar(odometer=newOdometer)

        def setCar(self, fuelEfficiency=None, fuelCapacity=None, fuelLevel=None, odometer=None):
            if fuelEfficiency == None:
                fuelEfficiency = self.getFuelEfficiency

            if fuelCapacity == None:
                fuelCapacity = self.getFuelCapacity

            if fuelLevel == None:
                fuelLevel = self.getFuelLevel

            if odometer == None:
                odometer = self.getOdometer

            self.fuelEfficiency = fuelEfficiency
            self.fuelCapacity = fuelCapacity
            self.fuelLevel = fuelLevel
            self.odometer = odometer

        def drive(self, miles):
            if miles < 0:
                return ("The car is not driven")

            one_gallon = miles / self.fuelEfficiency

            if one_gallon < self.fuelLevel:
                print("The car drove {} miles".format(miles))
            elif self.fuelLevel == 0:
                print("The car drove 0 miles")
            # else:
            # newMiles = milesDriven * miles
            # print("The car drove {} miles".format(newMiles))

            self.fuelLevel -= one_gallon
            self.odometer += miles

        def getCar(self):
            # Returns a tuple that has (FE,FC,FL,OD)
            return (self.fuelEfficiency, self.fuelCapacity, self.fuelLevel, self.odometer)

        def addFuel(self, num):
            if type(num) == str:
                return self.fuelLevel
            if num < 0:
                print("Sorry, you need to enter a postive number.")
                return self.fuelLevel

            if (self.fuelLevel + num) > self.fuelCapacity:
                return self.getFuelLevel
            if (self.fuelLevel + num) == self.fuelCapacity:
                self.fuelLevel += num
                return self.getFuelLevel
            if (self.fuelLevel + num) < self.fuelCapacity:
                self.fuelLevel += num
                return self.getFuelLevel

        def getFuelEfficiency(self):
            return self.getCar()[0]

        def getFuelCapacity(self):
            return self.getCar()[1]

        def getFuelLevel(self):
            return self.getCar()[2]

        def getOdometer(self):
            return self.getCar()[3]

        def tripRange(self):
            numOfMiles = self.fuelEfficiency * self.fuelLevel
            return numOfMiles

        def __str__(self):
            FE = self.getFuelEfficiency()
            FC = self.getFuelCapacity()
            FL = self.getFuelLevel()
            OD = self.getOdometer()

            string = '{}:{}:{}:{}'.format(FE, FC, FL, OD)
            return string


    # And
    # here
    # 's the tester program that goes hand in hand with testing if the class works properly. If everything is fixed, the output will be "No Errors Found"

from car import *
def main():
        c = Car(25, 15)
        checkNum(c.tripRange(), 0, 'Test 1')

        expected = (25, 15, 0, 0)
        checkCar(c, expected, 'Test 2')

        c.addFuel(-1)
        checkCar(c, expected, 'Test 3')

        c.addFuel(1000)
        checkCar(c, expected, 'Test 4')

        c.addFuel('doctor')
        checkCar(c, expected, 'Test 5')

        c.addFuel(0)
        checkCar(c, expected, 'Test 6')

        c.addFuel(15)
        expected = (25, 15, 15, 0)
        checkCar(c, expected, 'Test 7')

        c.drive(50)
        expected = (25, 15, 13, 50)
        checkCar(c, expected, 'Test 8')

        c.drive(100000)
        expected = (25, 15, 0, 375)
        checkCar(c, expected, 'Test 9')

        c.drive(5)
        expected = (25, 15, 0, 375)
        checkCar(c, expected, 'Test 10')

        c.addFuel(10)
        expected = (25, 15, 10, 375)
        checkCar(c, expected, 'Test 11')

        c.drive(-1)
        expected = (25, 15, 10, 375)
        checkCar(c, expected, 'Test 12')

        c.drive(0)
        expected = (25, 15, 10, 375)
        checkCar(c, expected, 'Test 13')

        checkNum(c.tripRange(), 250, 'Test 14')

    if not errorsFound:
        print('No Errors Found')

    def checkCar(car, expected, message):
        global errorsFound
        mpg, cap, level, odo = expected
        if car.getFuelEfficiency() != mpg:
            errorsFound = True
            print(message + ': Error efficiency. Expected ' + str(mpg))
            print('\tCar:', car)
        if car.getFuelCapacity() != cap:
            errorsFound = True
            print(message + ': Error capacity. Expected ' + str(cap))
            print('\tCar:', car)
        if car.getFuelLevel() != level:
            errorsFound = True
            print(message + ': Error level. Expected ' + str(level))
            print('\tCar:', car)
        if car.getOdometer() != odo:
            errorsFound = True
            print(message + ': Error odometer. Expected ' + str(odo))
            print('\tCar:', car)

    def checkNum(value, expected, message):
        global errorsFound
        if value != expected:
            errorsFound = True
            print(message + ': Error value. Expected {}. Got {}'.format(expected, value))

    errorsFound = False
    main()