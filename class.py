class Robot:
    def __init__(self, givenName, givenColor,givenWeight):
        self.name = givenName
        self.color = givenColor
        self.weight = givenWeight

    def introduce_self(self):
        print("Name is: " + self.name)
        print("Color: " + self.color)
        print("Weight: " + str(self.weight))

#r1 = Robot()
#r1.name = "Manu"
#r1.color = "green"
#r1.weight = 135

#r1.introduce_self()

#r2 = Robot()
#r2.name = "Jerry"
#r2.color = "blue"
#r2.weight = 120


#r2 = Robot()
#r2.name = "Jerry"
#r2.color = "blue"
#r2.weight = 120

#r2.introduce_self()

r1 = Robot("Manu", "Green", 135)
r2 = Robot("Jerry", "Blue", 120)

r1.introduce_self()
r2.introduce_self()


