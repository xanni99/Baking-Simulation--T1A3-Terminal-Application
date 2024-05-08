from datetime import datetime, timedelta
from baker3000 import Machine
import time
from user_interface import clear

class Date:
# Will read the date from the txt file (date the machine was last accessed)
    def past_accessed_date(self):
        try:
            with open("date_last_accessed.txt") as f:
                past_date = f.read()
            return past_date
        except FileNotFoundError as error:
            print(f"An error has occurred: {str(error)}")


    # Will save current date into txt file once the machine is turned off
    def date_today(self):
        with open("date_last_accessed.txt", "a") as f:
            current_date = str(datetime.now().date())
            consume_by_date = current_date + str(timedelta(days= 3))
            f.write(f"\nThese goods were baked on {current_date} and should be consumed by {consume_by_date}")
        return current_date


    # Check if current date and past date are the same
    def check_date(self, past_date):
            if str(datetime.now().date()) not in past_date:
                if Machine().ingredients["water"] >= 100 and Machine().ingredients["soap"] >= 15:
                    clear()
                    print("Before we start baking, let's make sure everything is nice and clean!")
                    time.sleep(3)
                    Machine().clean_machine()
                    Machine().ingredients["water"] -= 100
                    Machine().ingredients["soap"] -= 15
                    Machine().save_ingredients()
                else:
                    clear()
                    print("I do not have enough soap and water for a clean before we start baking :(...\n")
                    print("I recommend adding these ingredients and cleaning the machine before baking!")
                    time.sleep(6)
            else:
                pass

    def print_log(self):
        try:
            with open("date_last_accessed.txt") as f:
                print(f.read())
                time.sleep(10)
                print("Returning to Main Menu in 3 seconds...")
        except FileNotFoundError as error:
            print(f"An error has occurred: {str(error)}")