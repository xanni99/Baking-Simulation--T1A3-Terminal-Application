import json

from recipes import Recipe

class Machine:
    def __init__(self):
        self.ingredients = self.load_ingredients()
        self.max_quantities = {
            "Eggs": 6,
            "Milk": 500,
            "Butter": 500,
            "Flour": 500,
            "Sugar": 500,
            "Chocolate": 300,
            "Vanilla": 50,
            "Water": 250,
            "Soap": 50
        }

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

    def refill_ingredients(self):
        try:
            ingredient_to_refill = input("\nPlease enter the name of the ingredient you would like to refill\n").capitalize()
            max_quantity = self.max_quantities.get(ingredient_to_refill)
            if max_quantity is not None:
                current_quantity = self.ingredients.get(ingredient_to_refill)
                refill_amount = int(input(f"How much/many {ingredient_to_refill} would you like to refill? I currently have {self.ingredients[ingredient_to_refill]} out of {self.max_quantities.get(ingredient_to_refill)}\n"))
                if refill_amount > 0:
                    if current_quantity + refill_amount <= max_quantity:
                        self.ingredients[ingredient_to_refill] += refill_amount
                        print(f"I now have {self.ingredients.get(ingredient_to_refill)} {ingredient_to_refill}")
                    else:
                        print(f"I cannot store more than {max_quantity} units of {ingredient_to_refill}")
                else:
                    print("Please enter a positive number greater than 0")
                    self.refill_ingredients()
            else:
                print(f"{ingredient_to_refill} is not a valid ingredient")
                self.refill_ingredients()
        except ValueError:
            print("\n -- Invalid input -- I can only accept numbers\n")
            self.refill_ingredients()
        finally:
            self.save_ingredients()

    # def bake_treat(self,choice):

    



    # def clean_machine(self):

# test = Machine()


