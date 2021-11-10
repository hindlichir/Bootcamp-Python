from recipe import Recipe
from datetime import datetime
import time


class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name and isinstance(name, str):
            self._name = name
        else:
            raise ValueError("The name of the book has to be a string")

    @property
    def last_update(self):
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        if last_update and isinstance(last_update, datetime):
            self._last_update = last_update
        else:
            raise ValueError("The last update has to be in date format")

    @property
    def creation_date(self):
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        if creation_date and isinstance(creation_date, datetime):
            self._creation_date = creation_date
        else:
            raise ValueError("The creation date has to be in date format")

    @property
    def recipes_list(self):
        return self._recipes_list

    @recipes_list.setter
    def recipes_list(self, recipes_list):
        error = 0
        if recipes_list and isinstance(recipes_list, dict):
            if len(recipes_list.keys()) != 3:
                error = 1
            else:
                i = 0
                k = [0, 0, 0]
                for key in recipes_list.keys():
                    k[i] = key
                    i = i + 1
                if (k[0] == k[1] or k[0] == k[2] or k[1] == k[2]):
                    error = 1
                else:
                    for k in recipes_list.keys():
                        if k != "starter" and k != "lunch" and k != "dessert":
                            error = 1
        else:
            error = 1
        if error == 0:
            self._recipes_list = recipes_list
        else:
            s = "The recipes list is a dictionary with only 3 keys: "
            s = s + "starter, lunch and dessert"
            raise ValueError(s)

    def get_recipe_by_name(self, name):
        lst = self._recipes_list
        for key in lst.keys():
            for recipe in lst[key]:
                if recipe.name == name:
                    print(f"\n{str(recipe)}")
                    return recipe
        print(f"\nThe recipe {name} was not found!")

    def get_recipes_by_types(self, recipe_type):
        lst = self._recipes_list
        found = 0
        for key in lst.keys():
            if key == recipe_type:
                for recipe in lst[key]:
                    print(f"\n{str(recipe)}")
                found = 1
                break
        if found == 0:
            print(f"\nThe recipe type you entered isn't valid!")

    def add_recipe(self, recipe):
        if recipe and isinstance(recipe, Recipe):
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
        else:
            raise ValueError("You have to enter a Recipe instance!")
