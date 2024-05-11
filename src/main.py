""" This module contains the main function for the baker3000 Simulation."""
from baker3000 import Machine
from recipes import Recipe
from date import Date
import user_interface as ui
import time


def main():
    """The main function for the baker3000 simulation"""
    ui.clear()
    ui.welcome_message()
    time.sleep(3)
    baker3000 = Machine()
    recipes = Recipe()
    date = Date() 
    past_date = date.past_accessed_date() 
    date.check_date(past_date) 
    date.date_today()
    while True:   # Main menu loop
        ui.user_menu()
        user_action = input("\n:")
        match user_action:
            case "1":   # User selects 'Bake a Treat'
                ui.clear()
                choice_number = recipes.recipe_selection()
                choice = str(choice_number)
                ui.clear()
                baker3000.bake_treat(choice)
                time.sleep(3)
            case "2":   # User selects 'View Supply Levels'
                ui.clear()
                baker3000.list_ingredients()
                print
                print("\nReturning to Main Menu in 10 seconds...")
                time.sleep(12)
            case "3":   # User selects 'Refill Ingredients'
                ui.clear()
                baker3000.refill_ingredients()
                time.sleep(3)
            case "4":   # User selects 'Add a Recipe'
                ui.clear()
                recipes.add_recipe()
                time.sleep(3)
            case "5":   # User selects 'Clean Machine'
                baker3000.clean_machine()
                time.sleep(3)
            case "6":   # User selects 'View Baking Log'
                ui.clear()
                date.print_log()
                time.sleep(3)
            case "7":   # User selects 'Turn Off'
                ui.clear()
                ui.goodbye_message()
                time.sleep(4)
                ui.clear()
                break
            case _:   # User enters invalid input
                print(f"\n Sorry, {user_action} is not a valid option. "
                      f" I can only accept 1, 2, 3, 4, 5, 6 or 7\n")
                time.sleep(4)
        

main()
