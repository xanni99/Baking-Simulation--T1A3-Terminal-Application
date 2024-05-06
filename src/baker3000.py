import json

import time

from recipes import Recipe


class Machine:
    def __init__(self):
        self.recipes = Recipe()
        self.ingredients = self.load_ingredients()
        self.max_quantities = {
            "eggs": 6,
            "milk": 500,
            "butter": 500,
            "flour": 500,
            "sugar": 500,
            "chocolate": 300,
            "vanilla": 50,
            "water": 300,
            "soap": 50,
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
            json.dump(self.ingredients, f, indent=4)

    def list_ingredients(self):
        for key, value in self.ingredients.items():
            print(f"{key} - I currently have {value} available")

    def refill_ingredients(self):
        self.list_ingredients()
        try:
            ingredient_to_refill = input(
                "\nPlease enter the name of the ingredient you would like to refill\n"
            ).lower()
            max_quantity = self.max_quantities.get(ingredient_to_refill)
            if max_quantity is not None:
                current_quantity = self.ingredients.get(ingredient_to_refill)
                refill_amount = int(
                    input(
                        f"How much/many {ingredient_to_refill} would you like to refill? I currently have {self.ingredients[ingredient_to_refill]} out of {self.max_quantities.get(ingredient_to_refill)}\n"
                    )
                )
                if refill_amount > 0:
                    if current_quantity + refill_amount <= max_quantity:
                        self.ingredients[ingredient_to_refill] += refill_amount
                        print(
                            f"I now have {self.ingredients.get(ingredient_to_refill)} {ingredient_to_refill}"
                        )
                    else:
                        print(
                            f"I cannot store more than {max_quantity} units of {ingredient_to_refill}"
                        )
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

    def bake_treat(self, choice):
        for ingredient, required_amount in self.recipes.recipes[choice].items():
            if ingredient in ['name', 'bake time']:
                continue
            if self.ingredients[ingredient] < required_amount:
                print(f"I do not have enough {ingredient}. This recipe requires {required_amount} and I currently have {self.ingredients[ingredient]}")
                return
        print(f"Baking {self.recipes.recipes[choice]['name']}")
        # Reduce ingredient amounts
        for ingredient, required_amount in self.recipes.recipes[choice].items():
            if ingredient in ['name', 'bake time']:
                continue
            self.ingredients[ingredient] -= required_amount
        self.save_ingredients()

    def clean_machine(self):
        if self.ingredients["water"] >= 100 and self.ingredients["soap"] >= 15:
            self.ingredients["water"] -= 100
            self.ingredients["soap"] -= 15
            print("Cleaning Successful - I am now Spick and Span!")
            self.save_ingredients()
        else:
            print("Unable to clean machine :(\n")
            print("I do not have enough water and soap, please refill these")



test = Machine()
# # test.list_ingredients()
test.bake_treat('1')
# print(test.recipes.recipes['1'].items())

# print(test.ingredients["Eggs"])
# print(test.recipes.recipes['1']["eggs"])
