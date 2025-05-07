from sqlite_Interface import SQLiteInterface

class RecipeInterface:
    
    def __init__(self):
        self.sqlite_interface = SQLiteInterface()
        pass
    
    def add_recipe(self, name, description, ingredients, instructions):  #add a recipe to the database
        recipe_id = self.sqlite_interface.add_recipe(name, description)
        
        for ingredient in ingredients:
            self.sqlite_interface.add_ingredient(recipe_id, ingredient['name'], ingredient['quantity'])
            
        for i, step in enumerate(instructions, start=1):
            self.sqlite_interface.add_instruction(recipe_id, i, step)
            
    def list_recipes(self):
        return self.sqlite_interface.get_all_recipes()
    
    
            