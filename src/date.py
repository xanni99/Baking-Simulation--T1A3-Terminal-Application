import json
import time
from datetime import datetime

def store_completion_info(func_name, completion_time, outcome):
    try:
        with open('baked_treats.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Add completion time and outcome for the function
    data[func_name] = {'completion_time': completion_time.strftime('%Y-%m-%d %H:%M:%S'), 'outcome': outcome}

    # Write data back to JSON file
    with open('baked_treats.json', 'w') as file:
        json.dump(data, file, indent=4)

# Modify the bake_treat function to return a status indicating success or failure
def bake_treat(self, choice):
    try:
        for ingredient, required_amount in self.recipes.recipes[choice].items():
            if ingredient in ['name', 'bake time']:
                continue
            if self.ingredients[ingredient] < required_amount:
                print(f"I do not have enough {ingredient} for {self.recipes.recipes[choice]['name'].capitalize()}. This recipe requires {required_amount} and I currently have {self.ingredients[ingredient]}, please refill this.")
                return False  # Return False indicating failure
        print(f"Baking {self.recipes.recipes[choice]['name'].capitalize()}... Please Wait...")
        time.sleep(5)
        clear()
        print(f'*****{self.recipes.recipes[choice]["bake time"]} minutes later*****')
        time.sleep(2)
        clear()
        print(f"Here are your {self.recipes.recipes[choice]['name']}")
        self.display_treat(choice)
        time.sleep(8)
        # Reduce ingredient amounts
        for ingredient, required_amount in self.recipes.recipes[choice].items():
            if ingredient in ['name', 'bake time']:
                continue
            self.ingredients[ingredient] -= required_amount
        self.save_ingredients()
        return True  # Return True indicating success
    except KeyError:
        print(f"\n{choice} is not a valid recipe, returning to Main Menu...")
        time.sleep(2)
        return False  # Return False indicating failure

# Example usage:
completion_time = datetime.now()
outcome = bake_treat(baker3000, "Chocolate_Cake")  # Replace self_instance with your instance of the class
store_completion_info("bake_treat", completion_time, outcome)
