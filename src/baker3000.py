import time
import json
import colorama
from colorama import Fore
colorama.init(autoreset=True)
from recipes import Recipe
from user_interface import clear

"""
This module contains the class Machine for the baking simulation.
 """

      
class Machine:
    """Implements the Machine(Baker3000) and has multiple methods relating to what the machine itself can do, in addition to the ingredients it holds.
    """

    def __init__(self):
        """Creates an instance of the Machine
        """        
        self.recipes = Recipe()
        """creates an instance of the class Recipe() so that it can access methods relating to the recipes the machine stores """      
        self.ingredients = self.load_ingredients()
        """establishes ingredients currently stored in the machine from an external JSON doc"""
        self.max_quantities = {
            "eggs": 6,
            "milk": 600,
            "butter": 600,
            "flour": 600,
            "sugar": 600,
            "chocolate": 600,
            "vanilla": 100,
            "water": 300,
            "soap": 50
        }
        """establishes the maximum quantity of ingredients the machine can store"""

    def load_ingredients(self):
        """loads the ingredients currently stored in the machine from an external JSON doc"""
        try:
            with open("stored_ingredients.json", "r") as f:
                ingredients = json.load(f)
        except FileNotFoundError:
            ingredients = {}
        return ingredients

    def save_ingredients(self):
        """saves the ingredients currently stored in the machine to an external JSON doc"""
        with open("stored_ingredients.json", "w") as f:
            json.dump(self.ingredients, f, indent=4)

    def list_ingredients(self):
        """lists the current levels of ingredients stored in the machine and colours them in green, yellow, or red based on % of max quantity """
        for key, value in self.ingredients.items():
            max_quantity = self.max_quantities.get(key)
            if value >= 0.75 * max_quantity:
                print(f"{Fore.GREEN} {key.capitalize()} - I currently have {value} units available")
            if value >= 0.55 * max_quantity and value < 0.75 * max_quantity:
                print(f"{Fore.YELLOW} {key.capitalize()} - I currently have {value} units available")
            if value >= 0 and value < 0.55 * max_quantity:
                print(f"{Fore.RED} {key.capitalize()} - I currently have {value} units available")
        #Colour Key 
        print(f"\n{Fore.GREEN} Green ={Fore.RESET} Enough of ingredient to be used in ALL recipes - NO NEED TO REFILL")
        print(f"{Fore.YELLOW} Yellow ={Fore.RESET} Enough of ingredient to be used in AT LEAST 1 recipe - MAY NEED TO REFILL")
        print(f"{Fore.RED} Red ={Fore.RESET} Not enough of ingredient to be used in ANY recipes - NEED TO REFILL")

    def refill_ingredients(self):
        """allows the user to refill the ingredients currently stored in the machine"""
        #While loop allows user to refill multiple ingredients before returning to main menu
        while True:
            self.list_ingredients()
            print("\nWhat would you like to do?")
            print("\n[1] Refill ingredient")
            print("[2] Return to Main Menu")
            decision = input("\nEnter the number of your choice: ")
            #User chose to refill ingredient
            if decision == '1':
                clear()
                self.list_ingredients()
                try:
                    ingredient_to_refill = input("\nPlease enter the name of the ingredient you would like to refill\n").lower()
                    #Retreiving the max quantity of the ingredient the user chose to refill
                    max_quantity = self.max_quantities.get(ingredient_to_refill)
                    clear()
                    #Checking if the ingredient the user chose to refill is a valid ingredient
                    if max_quantity is not None:
                        current_quantity = self.ingredients.get(ingredient_to_refill)
                        refill_amount = int(input(f"\nHow much/many {ingredient_to_refill.capitalize()} would you like to refill? I currently have {self.ingredients[ingredient_to_refill]} out of {self.max_quantities.get(ingredient_to_refill)}\n"))
                        #Will only refill positive quantity
                        if refill_amount >= 0:
                            #Ensuring user does not overfill ingredient above maximum capacity
                            if current_quantity + refill_amount <= max_quantity:
                                #Adjusting new ingredient levels
                                self.ingredients[ingredient_to_refill] += refill_amount
                                clear()
                                print("Refilling... Please Wait...")
                                time.sleep(3)
                                clear()
                                print(f"I now have {self.ingredients.get(ingredient_to_refill)} units of {ingredient_to_refill.capitalize()}\n")
                                time.sleep(3)
                                clear()
                            else:
                                print(f"I cannot store more than {max_quantity} units of {ingredient_to_refill.capitalize()}, please try again\n")
                                time.sleep(2)
                                clear()
                                self.refill_ingredients()
                        else:
                            print("Please enter a positive number greater than 0")
                            time.sleep(2)
                            clear()
                            self.refill_ingredients()
                    else:
                        print(f"\n{ingredient_to_refill} is not a valid ingredient, please try again")
                        time.sleep(2)
                        clear()
                        self.refill_ingredients()
                except ValueError:
                    print("\n -- Invalid input -- I can only accept numbers, please try again\n")
                    time.sleep(2)
                    clear()
                    self.refill_ingredients()
            #User chose to return to main menu
            elif decision == '2':
                clear()
                print("Returning to Main Menu...")
                break
            else:
                print("\n -- Invalid input -- Please enter either '1' or '2'\n")
                time.sleep(2)
                clear()
        #Saves new ingredient level to external JSON doc
        self.save_ingredients()
        

    def display_treat(self,choice):
        """displays an ASCII representation of the chosen baked good, stored in an external txt file

        Parameters
        ----------
        choice : str
            The number that corresponds to the baked good the user wants to bake - retrieved from main
        """        
        if choice == '1':
            with open("cookie.txt", "r") as f:
                print(f.read())
        if choice == '2':
            with open("cupcake.txt", "r") as f:
                print(f.read())
        if choice == '3':
            with open("brownie.txt", "r") as f:
                print(f.read())
        if choice == '4':
            with open("muffin.txt", "r") as f:
                print(f.read())
        #if a user adds a new recipe and bakes that, there will be no corresponding text file so an empty space will be shown
        else:
            print("\n")
        print(f"Enjoy your {self.recipes.recipes[choice]['name'].capitalize()}\n \nReturning to Main Menu in 10 seconds...")


    def bake_treat(self, choice):
        """Uses user input (choice) to 'bake' the chosen baked good. 
        Involves checking there are enough stored ingredients to make the selected recipe.
        Calls display_treat function to display the ACII representation of baked good.
        Stores date that baked good was made on external JSON doc.
        Saves new ingredient values (reduces ingredients used to bake selected good).

        Parameters
        ----------
        choice : str
            The number that corresponds to the baked good the user wants to bake - retrieved from main
        """     
        #Gathers all ingredient amounts needed for chosen recipe  
        for ingredient, required_amount in self.recipes.recipes[choice].items():
            #Skips keys 'name' and 'bake' as these are not ingredient values
            if ingredient in ['name', 'bake time']:
                continue
            #Ensures user has enough of ingredient to bake selected recipe
            if self.ingredients[ingredient] < required_amount:
                print(f"I do not have enough {ingredient} for {self.recipes.recipes[choice]['name'].capitalize()}. This recipe requires {required_amount} and I currently have {self.ingredients[ingredient]}, please refill this.")
                return
        print(f"Baking {self.recipes.recipes[choice]['name'].capitalize()}... Please Wait...")
        time.sleep(5)
        clear()
        print(f'*****{self.recipes.recipes[choice]['bake time']} minutes later*****')
        time.sleep(2)
        clear()
        print(f"Here are your {self.recipes.recipes[choice]['name']}")
        #display ASCII image of baked good
        self.display_treat(choice)
        #Stores date that baked good was made on external JSON doc
        with open("date_last_accessed.txt", "a") as f:
            baked_good = str({self.recipes.recipes[choice]['name']})
            f.write(f"\n{baked_good},")
        time.sleep(5)
         # Reduce ingredient amounts
        for ingredient, required_amount in self.recipes.recipes[choice].items():
            if ingredient in ['name', 'bake time']:
                continue
            self.ingredients[ingredient] -= required_amount
        self.save_ingredients()

    
    def clean_machine(self):
        """When called, the machine undergoes a cleaning cycle.
        The machine is cleaned with soap and water.
        Soap and Water levels are adjusted accordingly and saved to external JSON doc
        """        
        clear()
        #Check there is enough soap and water
        if self.ingredients["water"] >= 100 and self.ingredients["soap"] >= 15:
            self.ingredients["water"] -= 100
            self.ingredients["soap"] -= 15
            print("Cleaning Machine with Soap and Water... Please wait...")
            time.sleep(5)
            clear()
            print("Cleaning Successful - I am now Spick and Span!")
            time.sleep(3)
            clear()
            self.save_ingredients()
            print("Returning to Main Menu...")
        #Error occurs if there is not enough ingredients
        else:
            print("Unable to Clean Machine :(\n")
            print("I do not have enough Water and Soap, please refill these")


