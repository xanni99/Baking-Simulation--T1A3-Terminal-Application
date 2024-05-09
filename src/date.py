from datetime import datetime, timedelta
from baker3000 import Machine
import time
from user_interface import clear

"""This module contains the class Date and contains all of the methods to do with storing the date the machine was accessed"""

class Date:
    """Creates an instance of Date"""
    def past_accessed_date(self):
        """returns the date the machine was last accessed - information stored in a JSON doc

        Returns
        -------
        str
            returns a string including the date the machine was last accessed
        """        
        try:
            with open("date_last_accessed.txt") as f:
                past_date = f.read()
            return past_date
        except FileNotFoundError as error:
            print(f"An error has occurred: {str(error)}")

    def date_today(self):
        """stores the date today (day that machine is currently being accessed) in an external JSON doc

        Returns
        -------
        str 
            Adds current date and date in 3 days time (date that any goods baked today should be consumed by) to JSON doc.
            Returns a string representing the date today
        """

        with open("date_last_accessed.txt", "a") as f:
            current_date = str(datetime.now().date())
            consume_by_date = current_date + str(timedelta(days= 3))
            f.write(f"\nThese goods were baked on {current_date} and should be consumed by {consume_by_date}")
        return current_date

    def check_date(self, past_date):
            """Checks if the current date is in the JSON doc.
            If the current date is not in the JSON doc (meaning the machine has not been used today), the machine is cleaned.
            If there are not enough ingredients (soap and water) for the machine to be cleaned, this step is skipped an a recommendation message is displayed instead.
            """
            if str(datetime.now().date()) not in past_date:
                #Check enough ingredients to clean machine
                if Machine().ingredients["water"] >= 100 and Machine().ingredients["soap"] >= 15:
                    clear()
                    print("Before we start baking, let's make sure everything is nice and clean!")
                    time.sleep(3)
                    Machine().clean_machine()
                    Machine().ingredients["water"] -= 100
                    Machine().ingredients["soap"] -= 15
                    Machine().save_ingredients()
                #If not enough ingredients to clean machine, recommendation message displayed instead
                else:
                    clear()
                    print("I do not have enough soap and water for a clean before we start baking :(...\n")
                    print("I recommend adding these ingredients and cleaning the machine before baking!")
                    time.sleep(6)
            else:
                pass

    def print_log(self):
        """Prints a log of the dates the machine was last accessed, along with any goods baked on that day"""
        try:
            with open("date_last_accessed.txt") as f:
                print(f.read())
                time.sleep(10)
                print("Returning to Main Menu in 3 seconds...")
        except FileNotFoundError as error:
            print(f"An error has occurred: {str(error)}")