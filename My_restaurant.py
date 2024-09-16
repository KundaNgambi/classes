class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        cuisines = ", ".join(self.cuisine_type)
        print(self.name.title() + " serves the following cuisine types: " + cuisines + ".")

    def restaurant(self):
        print(str(self.number_served) + " customers have been served today.")

    def update_restaurant(self, served):
        self.number_served = served

    def increment_restaurant(self, servings):
        self.number_served += servings



my_restaurant = Restaurant("Foodies", ["Italian", "Chinese", "American", "Japanese", "Mexican", "Zambian", "Indian"])
# my_restaurant.describe_restaurant()
# my_restaurant.update_restaurant(10)
# my_restaurant.increment_restaurant(10)
# my_restaurant.restaurant()
