# T1A3-Terminal Application

## Github Repository

The link to the GitHub repository for this project can be found [here](https://github.com/xanni99/T1A3-Terminal-Application).

## Styling

The code for this terminal application has adhered to the conventions outlined in the PEP 8 style guide. PEP 8 was chosen as it promotes a very readable and eye-pleasing coding style.

The PEP 8 style guide can be found [here](https://peps.python.org/pep-0008/).

## Application Features

describe each feature, providing a walkthrough of the logic of the application.
Ensure that the features allow you to demonstrate your understanding of the following language elements and concepts:

- Use of variables and the concept of variable scope
- loops and conditional control structures
- error handling

My terminal application, labeled Baker3000, is a baking simulation that runs as a machine that ultimately allows the user to bake themselves a tasty lil treat. In order to do this, the simulation includes 6 features (+ the ability to exit the simulation/turn off the machine) that can be accessed from a main interface. I will describe these features in more detail below.

### 1. Main Menu

The first feature of the application is the 'Main Menu'. The main menu is what the user will use to navigate the other features of the machine. After recieving the welcome message, this is where the user lands.

![](docs/main_menu.png)

As you can see from the image above, the main menu displays a message asking the user what they would like to do and to please select a number from the list of features that are available to them. 

In order to make this function like a main menu, something that the user can keep coming back to, I used a while loop with a nested match statement that uses the user's input to select the feature they would like to access. See the code below.

![](docs/main_menu_code.png)

After taking, user input as user_action, the match statement will match the user's input with the feature they have selected. Once each feature is run, the user will return back to the main menu (in the while loop) and will be promted to give another input. This will continue until the user_input == '7', in which case the loop will be broken (through the use of a 'break' statement ) and the simulation will end. In the case that the user enters invalid input (a string or an integer not in the match statement), an error message will occur asking the user to enter a valid input.

### 2. Bake a Treat

The second feature in the Baker3000 baking simulation is the of course, the ability for the user to bake a treat. When the user_input == '1', the user is taken to the following screen.

![](docs/bake_treat_1.png)

As you can see, the user is provided a list of the current available recipes that are stored on the machine. This list gets updated if the user adds a new recipe (feature will be described below). The user is then promted to provide the **number** of the recipe that they would like to bake. This occurs when the main menu calls the recipe_selection function


In order to bake the user a treat, the following steps occur:

1. The ingredient amounts required to make the chosen recipe have to be returned
2. It needs to be checked that there are enough ingredients currently stored in the machine in order to make the recipe
3. The baked good has to be made/displayed
4. The current ingredient levels of the machine needs to be updated accordingly
5. The baked good needs to be added to the history log (which will appear under the date today/the day the baked good was made)

These steps can be observed in the following code.

**INSERT BAKE_TREAT CODE HERE**

As you can see from the code above, this function accepts 'choice'. Choice refers to the user's selection of which baked treat they would like to bake. 

2 for loops had to be used. The first for loop is used in order to retreive the individual ingredient levels required for the chosen recipe. It can also be seen that within this loop the keys 'name' and 'bake time' were excluded from the loop as these are not ingredients and are not required in this part of the function. The second time the for loop is used is to reduce the amount of ingredients required by the recipe from the machine itself, in order to accurately represent the baked good being made. 


### 3. View Supply Levels

The third feature within the Baker3000 baking simulation, is the basic ability to view the current supply levels of the machine. Ultimately, this allows the user to guage what recipes they can and can't make and make the decision to refill ingredients if required. When the user selects this feature by inputting '......................

### 4. Refill Ingredients

### 5. Add a Recipe

### 6. Clean Machine

### 7. View Baking Log

### 8. Turn Off

## Implementation Plan

## Help Documentation

## References

van Rossum, G., Warsaw, B. and Coghlan, N. (2001). PEP 8 – Style Guide for Python Code. [online] Python.org. Available at: https://peps.python.org/pep-0008/.