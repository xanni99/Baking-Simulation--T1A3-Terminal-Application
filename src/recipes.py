import json

class Recipe:
    def __init__(self):
        # self.recipes = {
        #     int("1"): {"name": "Chocolate Chip Cookies", "eggs": 2, "milk": 0, "butter": 170, "flour": 280, "sugar": 100, "chocolate": 200, "vanilla": 15, "bake time": 15},
        #     int("2"): {"name": "Vanilla Cupcakes", "eggs": 2, "milk": 250, "butter": 60, "flour": 250, "sugar": 180, "chocolate": 0, "vanilla": 30, "bake time": 25},
        #     int("3"): {"name": "Brownies", "eggs": 2, "milk": 0, "butter": 125, "flour": 115, "sugar": 330, "chocolate": 125, "vanilla": 15, "bake time": 30},
        #     int("4"): {"name": "Chocolate Muffins", "eggs": 1, "milk": 200, "butter": 70, "flour": 300, "sugar": 250, "chocolate": 180, "vanilla": 0, "bake time": 25},
        # }
        self.recipes = self.load_recipes()

    def load_recipes(self):
        try:
            with open("stored_recipes.json", "r") as f:
                recipes = json.load(f)
        except FileNotFoundError:
            recipes = {}
        return recipes
    
    def save_recipes(self):
        with open("stored_recipes.json", "w") as f:
            json.dump(self.recipes, f, indent = 4)


    def list_recipes(self):
        for key, value in self.recipes.items():
            print(key, value["name"])


    def select_recipe(self):
        try:
            recipe_number = int(input("\nPlease enter the number of the recipe you would like to make: "))
            selected_recipe = self.recipes[recipe_number]
            return selected_recipe
        except ValueError:
            print("\n -- Invalid input -- I can only accept numbers\n")
            self.select_recipe()
        except KeyError:
            print("\n -- Invalid input -- Please enter a number listed \n")
            self.select_recipe()

    def add_recipe(self):
        print("Let's add a new recipe!")
        name = input("Enter the name of the recipe: ")
        eggs = int(input("Enter the number of eggs (if no eggs are used enter 0): "))
        milk = int(input("Enter the amount of milk(mls) (if no milk is used enter 0): "))
        butter = int(input("Enter the amount of butter(g) (if no butter is used enter 0): "))
        flour = int(input("Enter the amount of flour(g) (if no flour is used enter 0): "))
        sugar = int(input("Enter the amount of sugar(g) (if no sugar is used enter 0): "))
        chocolate = int(input("Enter the amount of chocolate(g) (if no chocolate is used enter 0): "))
        vanilla = int(input("Enter the amount of vanilla(mls) (if no vanilla is used enter 0): "))
        bake_time = int(input("Enter the bake time(min) (if no bake time is used enter 0): "))

        new_key = str(len(self.recipes) + 1 )

        self.recipes[new_key] = {
            "name": name,
            "eggs": eggs,
            "milk": milk, 
            "butter": butter, 
            "flour": flour, 
            "sugar": sugar, 
            "chocolate": chocolate, 
            "vanilla": vanilla, 
            "bake time": bake_time}
        
        self.save_recipes()


test = Recipe()


test.add_recipe ()