import json
from user_interface import clear
import time
import random

class Recipe:
    def __init__(self):
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
        print("444 Random Pick ** Surprise Me **")

    def add_recipe(self):
        print("Let's add a new recipe!\n")
        name = input("Enter the name of the recipe: \n")
        try:
            eggs = int(input("\nEnter the number of Eggs (if no Eggs are used enter 0): \n"))
            milk = int(input("Enter the amount of Milk(mls) (if no Milk is used enter 0): \n"))
            butter = int(input("Enter the amount of Butter(g) (if no Butter is used enter 0): \n"))
            flour = int(input("Enter the amount of Flour(g) (if no Flour is used enter 0): \n"))
            sugar = int(input("Enter the amount of Sugar(g) (if no Sugar is used enter 0): \n"))
            chocolate = int(input("Enter the amount of Chocolate(g) (if no Chocolate is used enter 0): \n"))
            vanilla = int(input("Enter the amount of Vanilla(mls) (if no Vanilla is used enter 0): \n"))
            bake_time = int(input("Enter the Bake time(mins) (if no bake time is used enter 0): \n"))
        except ValueError:
            print("\n -- Invalid input -- I can only accept numbers, please start again\n")
            time.sleep(5)
            clear()
            self.add_recipe()

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
        clear()
        print(f"\nYou have succsessfully added '{name}' to the list of recipes!")
        time.sleep(2)
        clear()
        print("Returning to Main Menu...")

    def recipe_selection(self):
        self.list_recipes()
        try:
            recipe_to_bake = int(input("\nEnter the number of the recipe you would like to bake\n"))
            if recipe_to_bake == 444:
                recipe_to_bake = random.choice(list(self.recipes.keys()))
                # recipe_to_bake = random.randint(1,4)
            return recipe_to_bake
        except ValueError:
            print("\n -- Invalid input -- I can only accept numbers, please start again\n")
            self.recipe_selection()
        except KeyError:
            print("\n -- Invalid input -- I can only accept numbers listed, please start again\n")
            self.recipe_selection()
        


