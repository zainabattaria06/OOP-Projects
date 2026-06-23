class Car:
    def __init__(self,year,color,brand,model):
        self.year=year
        self.color=color
        self.brand=brand
        self.model=model
        self.is_running=False
    def start(self):
        if self.is_running:
            print(f"The {self.brand} is already running.")
        else:
            self.is_running=True
            print(f"The {self.brand} starts. Vroom Vroom!")
    def stop(self):
        if self.is_running:
            self.is_running=False
            print(f"The {self.brand} engine is turned off.")
        else:
            print(f"The {self.brand} is already off.")
    def drive(self,distance):
        if self.is_running:
            print(f"Driving {distance} miles.")
        else:
            print(f"The {self.brand} is off. Start the car first.")
    def __str__(self):
        return f"{self.year} {self.color} {self.brand} {self.model}"


my_car=Car("2000","White","Toyota","Corolla")
print(my_car)
my_car.start()
my_car.drive(100)
my_car.stop()
my_car.drive(50)

your_car=Car("2001","Black","Honda","City")
print(your_car)
your_car.start()
your_car.stop()
your_car.drive(50)