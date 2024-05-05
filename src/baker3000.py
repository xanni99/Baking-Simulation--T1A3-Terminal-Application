import json

class Machine:
    def __init__(self):
        self.ingredients = self.load_ingredients()

    def load_ingredients(self):
        try:
            with open("stored_ingredients.json", "r") as f:
                ingredients = json.load(f)
        except FileNotFoundError:
            ingredients = {}
        return ingredients
    
    def save_ingredients(self):
        with open("stored_ingredients.json", "w") as f:
            json.dump(self.ingredients, f, indent = 4)

    def list_ingredients(self):
        for key, value in self.ingredients.items():
            print(f'{key} - I currently have {value} available')   

    def select_ingredient(self):
        try:
            ingredient_name = input("\nPlease enter the name of the ingredient you would like to refill: ")
            selected_ingredient = self.ingredients[ingredient_name.capitalize()]
            return selected_ingredient
        except ValueError:
            if ingredient_name.capitalized() not in self.ingredients:
                print("\n -- Invalid input -- Please enter an ingredient listed \n")
                self.select_ingredient()
        except KeyError:
            print("\n -- Invalid input -- I only accept names of ingredients listed \n")
            self.select_ingredient()


    # def refill_ingredients(self):

test = Machine()

test.list_ingredients ()
test.select_ingredient ()