class Ball:
    def __init__(self, airPressure, airPressureCapacity, color, type):
        self.color = color
        self.type = type
        self.airPressure = airPressure
        self.airPressureCapacity = airPressureCapacity

    def getPressure(self):
        return self.airPressure

    def getCapacity(self):
        return self.airPressureCapacity

    def needsAir(self):
        # Return the numerical value
        return self.airPressureCapacity - self.airPressure

    def isFull(self):
        # Return a boolean
        return self.airPressure == self.airPressureCapacity

    def isFlat(self):
        # Return a boolean
        return self.airPressure < (1/2 * self.airPressureCapacity)

    def addAir(self, amount):
        if self.isFull():
            return False
        originalPressure = self.airPressure
        self.airPressure += amount
        if self.airPressure > self.airPressureCapacity:
            self.airPressure = self.airPressureCapacity
        return self.airPressure > originalPressure

    def getColor(self):
        return self.color

    def getType(self):
        return self.type

# Note: Swapped arguments to match (pressure, capacity, color, type)
b = Ball(11, 30, "RED", "BASKETBALL")

print("AIR Pressure " + str(b.getPressure()))
print("AIR Capacity " + str(b.getCapacity()))
print("BALL Color " + str(b.getColor()))
print("BALL Type " + str(b.getType()))
print("Is Ball full of AIR " + str(b.isFull()))
# FIX: Cast to str()
print("How much air is needed " + str(b.needsAir()))
print("Is Ball FLAT " + str(b.isFlat()))
print("Adding 20 to pressure " + str(b.addAir(20)))
print("Adding 20 to pressure " + str(b.addAir(20)))
print("Is Ball full of AIR " + str(b.isFull()))
print("Is Ball FLAT " + str(b.isFlat()))
