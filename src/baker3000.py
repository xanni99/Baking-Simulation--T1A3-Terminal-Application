import json

import time

from recipes import Recipe


class Machine:
    def __init__(self):
        self.recipes = Recipe()
        self.ingredients = self.load_ingredients()
        self.max_quantities = {
            "Eggs": 6,
            "Milk": 500,
            "Butter": 500,
            "Flour": 500,
            "Sugar": 500,
            "Chocolate": 300,
            "Vanilla": 50,
            "Water": 300,
            "Soap": 50,
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
            ).capitalize()
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
        if self.ingredients["Eggs"] >= self.recipes.recipes[choice]["eggs"]:
            if self.ingredients["Milk"] >= self.recipes.recipes[choice]["milk"]:
                if self.ingredients["Butter"] >= self.recipes.recipes[choice]["butter"]:
                    if self.ingredients["Flour"] >= self.recipes.recipes[choice]["flour"]:
                        if self.ingredients["Sugar"] >= self.recipes.recipes[choice]["sugar"]:
                            if self.ingredients["Chocolate"] >= self.recipes.recipes[choice]["chocolate"]:
                                if self.ingredients["Vanilla"] >= self.recipes.recipes[choice]["vanilla"]:
                                    print(f"Baking {self.recipes.recipes[choice]["name"]}")
                                    self.ingredients["Eggs"] -= self.recipes.recipes[choice]["eggs"]
                                    self.ingredients["Milk"] -= self.recipes.recipes[choice]["milk"]
                                    self.ingredients["Butter"] -= self.recipes.recipes[choice]["butter"]
                                    self.ingredients["Flour"] -= self.recipes.recipes[choice]["flour"]
                                    self.ingredients["Sugar"] -= self.recipes.recipes[choice]["sugar"]
                                    self.ingredients["Chocolate"] -= self.recipes.recipes[choice]["chocolate"]
                                    self.ingredients["Vanilla"] -= self.recipes.recipes[choice]["vanilla"]
                                else:
                                    print(
                                        f"I do not have enough Vanilla. This recipe requires {self.recipes.recipes[choice]['vanilla']} and I currently have {self.ingredients['Vanilla']}"
                                    )
                            else:
                                print(
                                    f"I do not have enough Chocolate. This recipe requires {self.recipes.recipes[choice]['chocolate']} and I currently have {self.ingredients['Chocolate']}"
                                )
                        else:
                            print(
                                f"I do not have enough Sugar. This recipe requires {self.recipes.recipes[choice]['sugar']} and I currently have {self.ingredients['Sugar']}"
                            )
                    else:
                        print(
                            f"I do not have enough Flour. This recipe requires {self.recipes.recipes[choice]['flour']} and I currently have {self.ingredients['Flour']}"
                        )
                else:
                    print(
                        f"I do not have enough Butter. This recipe requires {self.recipes.recipes[choice]['butter']} and I currently have {self.ingredients['Butter']}"
                    )
            else:
                print(
                    f"I do not have enough Milk. This recipe requires {self.recipes.recipes[choice]['milk']} and I currently have {self.ingredients['Milk']}"
                )
        else:
            print(
                f"I do not have enough Eggs. This recipe requires {self.recipes.recipes[choice]['eggs']} and I currently have {self.ingredients['Eggs']}"
            )

    def clean_machine(self):
        if self.ingredients["Water"] >= 100 and self.ingredients["Soap"] >= 15:
            self.ingredients["Water"] -= 100
            self.ingredients["Soap"] -= 15
            print("Cleaning Successful - I am now Spick and Span!")
            self.save_ingredients()
        else:
            print("Unable to clean machine :(\n")
            print("I do not have enough water and soap, please refill these")


# test = Machine()
# test.bake_treat(1)
