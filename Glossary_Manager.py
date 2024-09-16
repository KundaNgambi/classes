class Glossary:
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.glossary_type = {self.key: [self.item]}

    def food_manager(self):
        print(self.glossary_type)

    def update_food_manager(self, update):
        if self.key in self.glossary_type:
            self.glossary_type[self.key].append(update)
        else:
            self.glossary_type[self.key] = [update]

    def get_food(self):
        print("You've added " + ", ".join(self.glossary_type[self.key]) + " to " + self.key)


food_type = input("What food category would you like to add: ")
actual_food = input("Enter the food you would like to add: ")
my_glossary = Glossary(food_type, actual_food)
my_glossary.food_manager()
my_glossary.update_food_manager("Rice")
my_glossary.get_food()
