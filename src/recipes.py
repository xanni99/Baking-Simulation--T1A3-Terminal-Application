import json

class Recipe:
    def __init__(self):
        self.recipes = self.load_recipes()

    def load_recipes(self):
        try:
            with open("stored_recipes.json", "r") as f:
                recipes = json.load(f)
        except FileNotFoundError:
            recipes = {}
        return recipes
    
    def save_recipes(self):
        with open("stored_recipes.json", "w") as f:
            json.dump(self.recipes, f, indent = 4)


    def list_recipes(self):
        for key, value in self.recipes.items():
            print(key, value["name"])


    def add_recipe(self):
        print("Let's add a new recipe!")
        name = input("Enter the name of the recipe: ")
        try:
            eggs = int(input("Enter the number of eggs (if no eggs are used enter 0): "))
            milk = int(input("Enter the amount of milk(mls) (if no milk is used enter 0): "))
            butter = int(input("Enter the amount of butter(g) (if no butter is used enter 0): "))
            flour = int(input("Enter the amount of flour(g) (if no flour is used enter 0): "))
            sugar = int(input("Enter the amount of sugar(g) (if no sugar is used enter 0): "))
            chocolate = int(input("Enter the amount of chocolate(g) (if no chocolate is used enter 0): "))
            vanilla = int(input("Enter the amount of vanilla(mls) (if no vanilla is used enter 0): "))
            bake_time = int(input("Enter the bake time(min) (if no bake time is used enter 0): "))
        except ValueError:
            print("\n -- Invalid input -- I can only accept numbers, please start again\n")
            self.add_recipe()

        new_key = str(len(self.recipes) + 1 )

        self.recipes[new_key] = {
            "name": name,
            "eggs": eggs,
            "milk": milk, 
            "butter": butter, 
            "flour": flour, 
            "sugar": sugar, 
            "chocolate": chocolate, 
            "vanilla": vanilla, 
            "bake time": bake_time}
        
        self.save_recipes()
        print(f"You have succsessfully added '{name}' to the list of recipes!")


# test = Recipe()


# test.select_recipe ()