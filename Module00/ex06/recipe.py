r_sandwich = {'ingredient' : ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal' : 'lunch',
        'time' : 10}
r_cake = {'ingredient' : ['flour', 'sugar', 'eggs'],
        'meal' : 'dessert',
        'time' : 60}
r_salad = {'ingredient' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal' : 'lunch',
        'time' : 15}

cookbook = {'sandwich' : r_sandwich,
        'cake' : r_cake,
        'salad' : r_salad}

def print_recipe(name):
    found = 0
    for key in cookbook.keys():
        if key == name:
            found = 1
    if found == 0:
        print("\nThe recipe you entered doesn't exist, try again!\n")
    else:
        print(f"\nRecipe for {name}:")
        print(f"\nIngredients list: {cookbook[name]['ingredient']}")
        print(f"To be eaten for {cookbook[name]['meal']}.")
        print(f"Takes {cookbook[name]['time']} minutes of cooking.\n")
        print("Enjoy!\n")


def delete_recipe(name):
    found = 0
    for key in cookbook.keys():
        if key == name:
            found = 1
    if found == 1:
        del [cookbook[name]]
        print(f"\nYour recipe {name} was deleted!\n")
    else:
        print("\nThe recipe you entered doesn't exist, try again!\n")

def add_recipe(name, ingredient, meal, time):
    r_new = {'ingredient' : ingredient,
            'meal' : meal,
            'time' : time}
    cookbook[name] = r_new


def print_all_cookbook():
    for key in cookbook.keys():
        print_recipe(key)

def print_options():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")

the_end = 0
while the_end == 0:
    print_options()
    choice = input(">> ")
    if choice == "1":
        name = input("\nHow do you call this recipe?\n")
        ingredient = input("\nEnter ingredients: [ <1>, <2>, <3> ]\n")
        meal = input("\nWhat is the type of meal? (lunch, dessert...)\n")
        time = input("\nHow much time does it take to cook?\n")
        add_recipe(name, ingredient, meal, time)
        print(f"\nYour recipe {name} was added!\n")
    elif choice == "2":
        name = input("\nWhich recipe you want to delete?\n")
        delete_recipe(name)
   elif choice == "5":
       print("\nThe cookbook is closed.\n")
        the_end = 1
