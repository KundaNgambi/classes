class Glossary:
    def __init__(self, key=None, item=None):
        # Only create glossary_type if key and item are provided
        if key and item:
            self.key = key.lower()
            self.item = item.lower()
            self.glossary_type = {self.key: [self.item]}
        else:
            self.glossary_type = {}

    # def food_manager(self):
    #     print(self.glossary_type)

    def update_food_manager(self):
        self.key = input("What category would you like to add? ").lower()
        self.item = input("What food would you like to add to it? ").lower()

        if self.key in self.glossary_type:
            self.glossary_type[self.key].append(self.item)
        else:
            self.glossary_type[self.key] = [self.item]

    def get_food(self):
        if self.key in self.glossary_type:
            print("You've added " + ", ".join(self.glossary_type[self.key]) + " to " + self.key)
        else:
            print("No food has been added yet.")

    def check_glossary(self):
        if self.glossary_type:
            print("Current glossary categories and items:")
            for key, items in self.glossary_type.items():
                print(f"{key.capitalize()}: {', '.join(items)}")
        else:
            print("The glossary is empty.")


# Instantiate without arguments
my_glossary = Glossary()
# my_glossary.food_manager()
my_glossary.update_food_manager()
my_glossary.get_food()
my_glossary.check_glossary()
