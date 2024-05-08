import json
import pytest
from baker3000 import Machine

def test_load_existing_json_file():
    baker3000 = Machine()
    assert baker3000.load_ingredients() == {
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



class TestColourListed:
#Testing Ingredient will be listed in right colour depending on current ingredient level
    def mock_ingredients(self):
        return {
            "eggs": 5, #83% of Max Capacity
            "milk": 350, #58% of Max Capacity
            "butter": 210, #35% of Max Capacity
        }

    def max_ingredients(self):
        return {
            "eggs": 6,
            "milk": 600,
            "butter": 600,
        }

    def test_correct_colours(self, capsys):
        #If level of "eggs" currently in machine = 5 it should be printed in green (as it is above 75% full) and is enough to be used in any of the recipes) 
        #If level of "milk" currently in machine = 350 it should be printed in yellow (as it is above 55% full but below 75%) and is enough to be used in at least 1 of the recipes) 
        #If level of "butter" currently in machine = 210 it should be printed in red (as it is below 55%) and is not enough to be used in any of the recipes)
        baker3000 = Machine()
        baker3000.ingredients = self.mock_ingredients()
        baker3000.list_ingredients()
        captured = capsys.readouterr()
        full_capture = captured.out.split("\n\n")
        ingredient_capture = full_capture[-2]
        assert (
            ingredient_capture
            == "\033[32m Eggs - I currently have 5 units available\n\033[33m Milk - I currently have 350 units available\n\033[31m Butter - I currently have 210 units available"
        )
      
