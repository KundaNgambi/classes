from My_restaurant import Restaurant



class Ice_cream_stand(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def flavors_offered(self):
        flavors = ", ".join(self.flavors)
        print("At " + self.name + " we offer the following ice cream flavors: " + flavors)


ice_world = Ice_cream_stand("Ice World", ["Plastic cup", "Corn"], ["Vanilla", "Chocolate", "Mint"])
ice_world.flavors_offered()