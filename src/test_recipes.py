import json
import pytest
from recipes import Recipe

def test_load_existing_json_file():
    recipe = Recipe()
    assert recipe.load_recipes() == {
    "1": {
        "name": "Chocolate Chip Cookies",
        "eggs": 2,
        "milk": 0,
        "butter": 170,
        "flour": 280,
        "sugar": 100,
        "chocolate": 200,
        "vanilla": 15,
        "bake time": 15
    },
    "2": {
        "name": "Vanilla Cupcakes",
        "eggs": 2,
        "milk": 250,
        "butter": 60,
        "flour": 250,
        "sugar": 180,
        "chocolate": 0,
        "vanilla": 30,
        "bake time": 25
    },
    "3": {
        "name": "Brownies",
        "eggs": 2,
        "milk": 0,
        "butter": 125,
        "flour": 115,
        "sugar": 330,
        "chocolate": 125,
        "vanilla": 15,
        "bake time": 30
    },
    "4": {
        "name": "Chocolate Muffins",
        "eggs": 1,
        "milk": 200,
        "butter": 70,
        "flour": 300,
        "sugar": 250,
        "chocolate": 180,
        "vanilla": 0,
        "bake time": 25
    }
}
    
def test_list_recipes(capsys):
    recipe = Recipe()
    recipe.list_recipes()
    captured = capsys.readouterr()
    assert captured.out == "1 Chocolate Chip Cookies\n2 Vanilla Cupcakes\n3 Brownies\n4 Chocolate Muffins\n444 Random Pick ** Surprise Me **\n"
    

# def test_add_recipe(monkeypatch, capsys):
#     user_inputs = iter([
#         "Test Recipe", # Recipe Name
#         "2", # Eggs
#         "250", #Milk
#         "150", #Butter
#         "200", #Flour
#         "250", #Sugar
#         "0", #Chocolate
#         "15", #Vanilla
#         "45", #Bake Time
#     ])
#     monkeypatch.setattr('builtins.input', lambda _: next(user_inputs))
#     recipe = Recipe()
#     recipe.recipes = {}
#     recipe.add_recipe()
#     captured = capsys.readouterr()
#     assert captured.out == "You have succsessfully added 'Test Recipe' to the list of recipes!\nReturning to Main Menu...\n"
#     assert recipe.recipes == {
#         "1": {
#             "name": "Test Recipe",
#             "eggs": 2,
#             "milk": 250,
#             "butter": 150,
#             "flour": 200,
#             "sugar": 250,
#             "chocolate": 0,
#             "vanilla": 15,
#             "bake time": 45
#         }
#     }

