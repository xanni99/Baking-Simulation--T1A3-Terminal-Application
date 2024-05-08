from baker3000 import Machine
from recipes import Recipe
from date import Date
import user_interface as ui
import time

def main():
    ui.clear()
    ui.welcome_message()
    time.sleep(3)
    baker3000 = Machine()
    recipes = Recipe()
    date = Date()
    past_date = date.past_accessed_date()
    date.check_date(past_date)
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
                # baker3000.store_baked_good(choice)
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
                date.print_log()
                time.sleep(3)
            case "7":
                ui.clear()
                date.date_today()
                ui.goodbye_message()
                time.sleep(4)
                ui.clear()
                break
            case _:
                print(f"\n Sorry, {user_action} is not a valid option. I can only accept 1, 2, 3, 4, 5 or 6\n")
                time.sleep(4)
        

main()



