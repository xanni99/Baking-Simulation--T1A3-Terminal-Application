class RecipeSelection:
    def __init__(self):
        self.recipes = {
            "1": {"name": "Chocolate Chip Cookies", "eggs": 2, "milk": 0, "butter": 170, "flour": 280, "sugar": 100, "chocolate": 200, "vanilla": 15},
            "2": {"name": "Vanilla Cupcakes", "eggs": 2, "milk": 250, "butter": 60, "flour": 250, "sugar": 180, "chocolate": 0, "vanilla": 30},
            "3": {"name": "Brownies", "eggs": 2, "milk": 0, "butter": 125, "flour": 115, "sugar": 330, "chocolate": 125, "vanilla": 15},
            "4": {"name": "Chocolate Muffins", "eggs": 1, "milk": 200, "butter": 70, "flour": 300, "sugar": 250, "chocolate": 180, "vanilla": 0},
        }

    def list_recipes(self):
        for key, value in self.recipes.items():
            print(key, value["name"])


test = RecipeSelection()


test.list_recipes ()