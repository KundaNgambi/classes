class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        cuisines = ", ".join(self.cuisine_type)
        print(self.name.title() + " serves the following cuisine types: " + cuisines + ".")


my_restaurant = Restaurant("Foodies", ["Italian", "Chinese", "American", "Japanese", "Mexican", "Zambian", "Indian"])
my_restaurant.describe_restaurant()
