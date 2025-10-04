class Ferrari():
    def fuel_type(self):
        print("The fuel type in a Ferrari is Petrol")
    def max_speed(self):
        print("401 Km/h is the maximum speed of a ferrari")
    

class BMW():
    def fuel_type(self):
        print("The fuel type in a BMW is Diesel")
    def max_speed(self):
        print("307 Km/h is the maximum speed of a BMW")

ferrari=Ferrari()
bmw=BMW()

for car  in (ferrari,bmw):
    car.fuel_type()
    car.max_speed()
    