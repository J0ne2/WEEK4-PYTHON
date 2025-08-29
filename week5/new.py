# Base class: Plane
class Plane:
    def move(self):
        pass  # general method for polymorphism

# Child classes
class PassengerPlane(Plane):
    def move(self):
        print("Passenger plane is flying with passengers 🛫")

class CargoPlane(Plane):
    def move(self):
        print("Cargo plane is flying with cargo 📦")

class FighterJet(Plane):
    def move(self):
        print("Fighter jet is flying at supersonic speed ✈💨")

# Testing polymorphism
planes = [PassengerPlane(), CargoPlane(), FighterJet()]
for plane in planes:
    plane.move()