# Hybrid inheritance is a combination of more than one type of inheritance.



class Vehicle:
    def move(self):
        print("vehicle can move")

# single inheritance 
class Car(Vehicle):
    def drive(self):
        print("car drives")

class Boat(Vehicle):
    def sail(self):
        print("boat can sail")



# multiple inheritance 
class AmphibiousVehicle(Car,Boat):
    def amphibious_vehicle(self):
        print("Amphibious Vehicle can drive and sail")


av = AmphibiousVehicle()
av.amphibious_vehicle() 
av.move()
av.sail() 
av.drive()                              