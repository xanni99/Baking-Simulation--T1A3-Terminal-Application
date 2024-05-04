class Machine:
    def __init__(self, eggs: int=6, milk: int=500, butter: int=500, flour: int=500, sugar: int=500, chocolate: int=300, vanilla: int=50, water: int=250, soap: int= 50):
        self.eggs = eggs
        self.milk = milk
        self.butter = butter
        self.flour = flour
        self.sugar = sugar
        self.chocolate = chocolate
        self.vanilla = vanilla
        self.water = water
        self.soap = soap

    def refill_ingredients(self):
        print("\nWhat ingredient would you like to refill?\n")
        print(f"[1] Eggs, current amount = {self.eggs}/6\n")
        print(f"[2] Milk, current amount = {self.milk}/500\n")
        print(f"[3] Butter, current amount = {self.butter}/500\n")
        print(f"[4] Flour, current amount = {self.flour}/500\n")
        print(f"[5] Sugar, current amount = {self.sugar}/500\n")
        print(f"[6] Chocolate, current amount = {self.chocolate}/300\n")
        print(f"[7] Vanilla, current amount = {self.vanilla}/50\n")
        print(f"[8] Water, current amount = {self.water}/250\n")
        print(f"[9] Soap, current amount = {self.soap}/50\n")

        try:
            ingredient = int(input("Enter the number of the ingredient you would like to refill: "))
            if ingredient < 1 or ingredient > 9:
                raise ValueError

        except ValueError:
            print("\n Please enter a number between 1 and 9\n")
            self.refill_ingredients()
            
        match ingredient:
            case 1:
                try:
                    refill_amount = int(input("\nHow many eggs would you like to add?\n"))
                except ValueError:
                    print("\n -- Invalid input -- I can only accept numbers\n")
                    self.refill_ingredients()
                if refill_amount + self.eggs > 6:
                    print("\nI cannot store more than 6 eggs!\n")
                    self.refill_ingredients()
                self.eggs += refill_amount
                print(f"I now have {self.eggs} eggs!")
            case 2:
                try:
                    refill_amount = int(input("\nHow much milk(ml) would you like to add?\n"))
                except ValueError:
                    print("\n -- Invalid input -- I can only accept numbers\n")
                    self.refill_ingredients()
                if refill_amount + self.milk > 500:
                    print("\nI cannot store more than 500ml milk!\n")
                    self.refill_ingredients()
                self.milk += refill_amount
                print(f"I now have {self.milk}mls of milk!")
            case 3:
                try:
                    refill_amount = int(input("\nHow much butter(g) would you like to add?\n"))
                except ValueError:
                    print("\n -- Invalid input -- I can only accept numbers\n")
                    self.refill_ingredients()
                if refill_amount + self.butter > 500:
                    print("\nI cannot store more than 500g butter!\n")
                    self.refill_ingredients()
                self.butter += refill_amount
                print(f"I now have {self.butter}g of butter!")
            case 4:
                try:
                    refill_amount = int(input("\nHow much flour(g) would you like to add?\n"))
                except ValueError:
                    print("\n -- Invalid input -- I can only accept numbers\n")
                    self.refill_ingredients()
                if refill_amount + self.flour > 500:
                    print("\nI cannot store more than 500g flour!\n")
                    self.refill_ingredients()
                self.flour += refill_amount
                print(f"I now have {self.flour}g of flour!")
            case 5:
                try:
                    refill_amount = int(input("\nHow much sugar(g) would you like to add?\n"))
                except ValueError:
                    print("\n -- Invalid input -- I can only accept numbers\n")
                    self.refill_ingredients()
                if refill_amount + self.sugar > 500:
                    print("\nI cannot store more than 500g sugar!\n")
                    self.refill_ingredients()
                self.sugar += refill_amount
                print(f"You now have {self.sugar} sugar!")
            case 6:
                try:
                    refill_amount = int(input("\nHow much chocolate(g) would you like to add?\n"))
                except ValueError:
                    print("\n -- Invalid input -- I can only accept numbers\n")
                    self.refill_ingredients()
                if refill_amount + self.chocolate > 300:
                    print("\nI cannot store more than 300g chocolate!\n")
                    self.refill_ingredients()
                self.chocolate += refill_amount
                print(f"I now have {self.chocolate}g of chocolate!")
            case 7:
                try:
                    refill_amount = int(input("\nHow much vanilla(ml) would you like to add?\n"))
                except ValueError:
                    print("\n -- Invalid input -- I can only accept numbers\n")
                    self.refill_ingredients()
                if refill_amount + self.vanilla > 50:
                    print("\nI cannot store more than 50ml vanilla!\n")
                    self.refill_ingredients()
                self.vanilla += refill_amount
                print(f"I now have {self.vanilla}mls of vanilla!")
            case 8:
                try:
                    refill_amount = int(input("\nHow much water(ml) would you like to add?\n"))
                except ValueError:
                    print("\n -- Invalid input -- I can only accept numbers\n")
                    self.refill_ingredients()
                if refill_amount + self.water > 250:
                    print("\nI cannot store more than 250ml water!\n")
                    self.refill_ingredients()
                self.water += refill_amount
                print(f"I now have {self.water}mls of water!")
            case 9:
                try:
                    refill_amount = int(input("\nHow much soap(g) would you like to add?\n"))
                except ValueError:
                    print("\n -- Invalid input -- I can only accept numbers\n")
                    self.refill_ingredients()
                if refill_amount + self.soap > 50:
                    print("\nI cannot store more than 50g soap!\n")
                    self.refill_ingredients()
                self.soap += refill_amount
                print(f"I now have {self.soap}g of soap!")
            case _:
                print("\n Please enter a number between 1 and 9\n")
                self.refill_ingredients()

test = Machine()

test.refill_ingredients ()


        
