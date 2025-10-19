from Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self,num_of_wheels,num_of_gears,acpower):
        self.num_of_wheels=num_of_wheels
        self.num_of_gears=num_of_gears
        self.acpower=acpower
    def carAcService(self):
        print("car has Ac power",self.acpower)

if __name__=="__main__":
    c=Car(4,5,320)
    c.welcomeVehicleMessage()
    c.carAcService()
    # v=Vehicle(4,6)
    # v.welcomeVehicleMessage()
    # v.carAcService()

    
    
    