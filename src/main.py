from baker3000 import Machine
from recipes import Recipe
import user_interface as ui

def main():
    ui.welcome_message()
    baker3000 = Machine()
    recipes = Recipe()
    while True:
        ui.user_menu()
        user_action = input("\n:")
        match user_action:
            case "1":
                ui.clear()
                choice = recipes.recipe_selection()
                baker3000.bake_treat(choice)
            case "2":
                ui.clear()
                baker3000.list_ingredients()
            case "3":
                ui.clear()
                baker3000.refill_ingredients()
            case "4":
                ui.clear()
                recipes.add_recipe()
            case "5":
                ui.clear()
                baker3000.clean_machine()
            case "6":
                ui.clear()
                ui.goodbye_message()
                break
            case _:
                print(f"\n Sorry, {user_action} is not a valid option. I can only accept 1, 2, 3, 4, 5 or 6\n")

main()



