from book import Book
from recipe import Recipe
from datetime import datetime
import time

salad = Recipe("salad", 2, 20, ['avocado', 'arugula', 'tomatoes', 'spinach'],
               "It's a salad.", "starter")

salad2 = Recipe("salad2", 2, 20, ['avocado', 'arugula', 'tomatoes', 'spinach'],
                "It's a salad.", "starter")

sandwich = Recipe("sandwich", 1, 15, ['ham', 'bread', 'cheese', 'tomatoes'],
                  "It's a sandwich.", "lunch")

cake = Recipe("cake", 3, 60, ['flour', 'sugar', 'eggs'],
              "It's a cake.", "dessert")

my_list = {'starter': [salad, salad2],
           'lunch': [],
           'dessert': []}

print(f"\n{str(salad)}")
print(f"\n{str(sandwich)}")
print(f"\n{str(cake)}")

cookbook = Book("My_book", datetime.now(), datetime.now(), my_list)
cookbook.get_recipe_by_name("salad2")
cookbook.get_recipe_by_name("tomate")
cookbook.get_recipes_by_types("starter")
cookbook.get_recipes_by_types("lol")
cookbook.add_recipe(sandwich)
cookbook.add_recipe(cake)
cookbook.get_recipe_by_name("sandwich")
cookbook.get_recipes_by_types("dessert")
cookbook.add_recipe(cake)
cookbook.get_recipes_by_types("dessert")
print()
cookbook.add_recipe("Yolo")

print()
