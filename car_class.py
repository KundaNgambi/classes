class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 30

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def battery_information(self):
        print("This car has a " + str(self.battery_size) + " kWh battery.")

    def update_battery_information(self, new_size):
        self.battery_size = new_size
    def get_range(self):
        range = self.battery_size * 5
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# Instance creation
my_electric_car = ElectricCar("Tesla", "Model S", 2016)
print(my_electric_car.get_descriptive_name())

# Update battery information and display it separately
my_electric_car.battery.update_battery_information(100)  # Update battery size
my_electric_car.battery.battery_information()  # Display updated battery size
my_electric_car.battery.get_range()
