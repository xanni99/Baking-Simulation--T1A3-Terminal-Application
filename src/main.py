from baker3000 import Machine
from recipes import Recipe
import user_interface as ui
import time

def main():
    ui.welcome_message()
    baker3000 = Machine()
    recipes = Recipe()
    while True:
        ui.user_menu()
        user_action = input("\n:")
        match user_action:
            case "1":
                choice_number = recipes.recipe_selection()
                choice = str(choice_number)
                baker3000.bake_treat(choice)
                time.sleep(10)
            case "2":
                baker3000.list_ingredients()
            case "3":
                baker3000.refill_ingredients()
            case "4":
                recipes.add_recipe()
            case "5":
                baker3000.clean_machine()
            case "6":
                ui.goodbye_message()
                break
            case _:
                print(f"\n Sorry, {user_action} is not a valid option. I can only accept 1, 2, 3, 4, 5 or 6\n")

main()



