class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        s = f"Recipe {self.name} ({self. recipe_type} - lvl {self.cooking_lvl}"
        s = s + f" - {self.cooking_time}m of cooking): {self.description}\n"
        s = s + f"You'll need the following ingredients: {self.ingredients}!"
        return s

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name and isinstance(name, str):
            self._name = name
        else:
            raise ValueError("The name should be a non-empty string")

    @property
    def cooking_lvl(self):
        return self._cooking_lvl

    @cooking_lvl.setter
    def cooking_lvl(self, cl):
        if (cl and isinstance(cl, int) and cl >= 1 and cl <= 5):
            self._cooking_lvl = cl
        else:
            s = "The cooking level should be a number betwwen 1 & 5"
            raise ValueError(s)

    @property
    def cooking_time(self):
        return self._cooking_time

    @cooking_lvl.setter
    def cooking_time(self, ct):
        if (ct and isinstance(ct, int) and ct >= 0):
            self._cooking_time = ct
        else:
            s = "The cooking time should be a positive number"
            raise ValueError(s)

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        error = 0
        if ingredients and isinstance(ingredients, list):
            for elem in ingredients:
                if not isinstance(elem, str):
                    error = 1
        else:
            error = 1
        if error == 0:
            self._ingredients = ingredients
        else:
            s = "The ingredients have to be a string-only list"
            raise ValueError(s)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if not description:
            pass
        elif isinstance(description, str):
            self._description = description
        else:
            s = "The description can be a string or left empty"
            raise ValueError(s)

    @property
    def recipe_type(self):
        return self._recipe_type

    @recipe_type.setter
    def recipe_type(self, type):
        error = 0
        if type and isinstance(type, str):
            if (type != "starter" and type != "lunch" and type != "dessert"):
                error = 1
        else:
            error = 1
        if error == 0:
            self._recipe_type = type
        else:
            s = "The recipe type can either be starter, lunch or dessert"
            raise ValueError(s)
