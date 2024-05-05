class Recipe:
    def __init__(self):
        self.recipes = {
            int("1"): {"name": "Chocolate Chip Cookies", "eggs": 2, "milk": 0, "butter": 170, "flour": 280, "sugar": 100, "chocolate": 200, "vanilla": 15},
            int("2"): {"name": "Vanilla Cupcakes", "eggs": 2, "milk": 250, "butter": 60, "flour": 250, "sugar": 180, "chocolate": 0, "vanilla": 30},
            int("3"): {"name": "Brownies", "eggs": 2, "milk": 0, "butter": 125, "flour": 115, "sugar": 330, "chocolate": 125, "vanilla": 15},
            int("4"): {"name": "Chocolate Muffins", "eggs": 1, "milk": 200, "butter": 70, "flour": 300, "sugar": 250, "chocolate": 180, "vanilla": 0},
        }

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


test = Recipe()


test.select_recipe ()