import json
from user_interface import clear
import time
import random

"""This module contains the class Recipe and contains all of the methods to do with the recipes stored on the machine"""

class Recipe:
    """Creates an instance of Recipe"""
    def __init__(self):
        self.recipes = self.load_recipes()
        """establishes recipes storeed on the machine"""

    def load_recipes(self):
        """Loads recipes stored on the machine"""
        try:
            with open("stored_recipes.json", "r") as f:
                recipes = json.load(f)
        except FileNotFoundError:
            recipes = {}
        return recipes
    
    def save_recipes(self):
        """saves the recipes currently stored in the machine to an external JSON doc"""
        with open("stored_recipes.json", "w") as f:
            json.dump(self.recipes, f, indent = 4)


    def list_recipes(self):
        """Lists all of the recipes stored on the machine"""
        for key, value in self.recipes.items():
            print(key, value["name"])
        #Lists an extra option with special number that indicates random recipe
        print("444 Random Pick ** Surprise Me **")

    def add_recipe(self):
        """Allows the user to add a new recipe to the machine.
        The user is prompted to enter the name of the recipe, the amount of ingredients required, and the bake time."""

        print("Let's add a new recipe!\n")
        name = input("Enter the name of the recipe: \n")
        #Gather inputs corresponding to ingredient amounts (only accepts integers)
        try:
            eggs = int(input("\nEnter the number of Eggs (if no Eggs are used enter 0): \n"))
            milk = int(input("Enter the amount of Milk(mls) (if no Milk is used enter 0): \n"))
            butter = int(input("Enter the amount of Butter(g) (if no Butter is used enter 0): \n"))
            flour = int(input("Enter the amount of Flour(g) (if no Flour is used enter 0): \n"))
            sugar = int(input("Enter the amount of Sugar(g) (if no Sugar is used enter 0): \n"))
            chocolate = int(input("Enter the amount of Chocolate(g) (if no Chocolate is used enter 0): \n"))
            vanilla = int(input("Enter the amount of Vanilla(mls) (if no Vanilla is used enter 0): \n"))
            bake_time = int(input("Enter the Bake time(mins) (if no bake time is used enter 0): \n"))
        #Values entered should only be integers
        except ValueError:
            print("\n -- Invalid input -- I can only accept numbers, please start again\n")
            time.sleep(5)
            clear()
            self.add_recipe()

        #Creates new recipe number which is 1 higher than the latest stored recipe
        new_key = str(len(self.recipes) + 1 )

        #Adds key names and values for new recipe
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
        
        #Saves new recipe into external JSON doc so it can be used in future
        self.save_recipes()
        clear()
        print(f"\nYou have sucsessfully added '{name}' to the list of recipes!")
        print("\nPlease turn the machine on and off again before baking this recipe!")
        time.sleep(5)
        clear()
        print("Returning to Main Menu...")

    def recipe_selection(self):
        """Allows the user to select a recipe to bake.
        Calls list_recipe method so the user can see available recipes
        Returns the number corresponding to the recipe the user wants to bake"""

        #Loops until the user enters a valid recipe number
        while True:
            self.list_recipes()
            try:
                recipe_to_bake = int(input("\nEnter the number of the recipe you would like to bake:\n"))
                if recipe_to_bake == 444:
                    recipe_to_bake = random.choice(list(self.recipes.keys()))
                if str(recipe_to_bake) not in self.recipes.keys():
                    raise KeyError
                return recipe_to_bake
            except ValueError:
                print("\n -- Invalid input -- I can only accept numbers, please try again\n")
                time.sleep(2)
                clear()
            except KeyError:
                print(f"\n{recipe_to_bake} is not a valid recipe number, please try again\n")
                time.sleep(2)
                clear()
        