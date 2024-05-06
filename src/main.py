from baker3000 import Machine
from recipes import Recipe
import user_interface as ui
import time

def main():
    ui.clear()
    ui.welcome_message()
    time.sleep(3)
    baker3000 = Machine()
    recipes = Recipe()
    while True:
        ui.user_menu()
        user_action = input("\n:")
        match user_action:
            case "1":
                ui.clear()
                choice_number = recipes.recipe_selection()
                choice = str(choice_number)
                ui.clear()
                baker3000.bake_treat(choice)
                time.sleep(6)
            case "2":
                ui.clear()
                baker3000.list_ingredients()
                time.sleep(12)
                print("\nReturning to Main Menu in 3 seconds...")
                time.sleep(3)
            case "3":
                ui.clear()
                baker3000.refill_ingredients()
                time.sleep(3)
            case "4":
                ui.clear()
                recipes.add_recipe()
                time.sleep(3)
            case "5":
                baker3000.clean_machine()
                time.sleep(3)
            case "6":
                ui.clear()
                ui.goodbye_message()
                time.sleep(4)
                ui.clear()
                break
            case _:
                print(f"\n Sorry, {user_action} is not a valid option. I can only accept 1, 2, 3, 4, 5 or 6\n")
                time.sleep(4)
        

main()



