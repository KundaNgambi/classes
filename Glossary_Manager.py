class Glossary:
    #initialized with key and item as parameters
    def __init__(self, key=None, item=None):
        if key and item:
            #converted to lower case to avoid errors caused from improper case handling
            self.key = key.lower()
            self.item = item.lower()
            self.glossary_type = {self.key: [self.item]}
        else:
            self.glossary_type = {}

    # def food_manager(self):
    #     print(self.glossary_type)

    def update_food_manager(self):
        while True:
            categories = input("Enter categories separated by commas: ").lower().split(",")
            foods = input("Enter corresponding foods separated by commas (in same order).if multiple items are to be "
                          "added to same category, separate using semi colon: ").lower().split(";")

            # Ensure both inputs have the same length
            if len(categories) != len(foods):
                print("Error: Number of categories and foods must match.Please try again")
            continue

        # Add each category and corresponding food
        for category, food in zip(categories, foods):
            category = category.strip()
            food_list = [item.strip() for item in food.split(",")]

            if category in self.glossary_type:
                self.glossary_type[category].extend(food_list)
            else:
                self.glossary_type[category] = [food]

    def get_food(self):
        if self.key in self.glossary_type:
            print("You've added " + ", ".join(self.glossary_type[self.key]) + " to " + self.key)
        else:
            print("No food has been added yet.")

    # New method to check all keys and items
    def check_glossary(self):
        if self.glossary_type:
            print("Current glossary categories and items:")
            for key, items in self.glossary_type.items():
                print(f"{key.capitalize()}: {', '.join(items)}")
        else:
            print("The glossary is empty.")


# Example usage
my_glossary = Glossary()
# my_glossary.food_manager()
my_glossary.update_food_manager()  # Add multiple categories and foods
my_glossary.check_glossary()  # Check current keys and items
