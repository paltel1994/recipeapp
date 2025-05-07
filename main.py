from RecipeInterface import RecipeInterface

RECIPE = RecipeInterface()

# add the ability to add a recipe to the database, with ingredients and instructions, 
# ingredients - should have a health rating,  1 - bad for you, 2 - no benefit, 3 - good for you.    recipe itself will have a net rating based on the scores of the individual ingredients.
# factor in the quantity of the ingredients 
# flavor profile - sweet, sour, salty, bitter, umami tied to the recipe level. 

print("""
===============================
   🧑‍🍳 Welcome to RecipeApp
===============================
""")

program_running = True
while program_running == True:
    
    print("\nMenu:")
    print("1. Add a new recipe")
    print("2. List recipes")
    print("3. View a recipe")
    print("4. Exit")
    
    choice = input("Please enter your choice: ").strip()
    
    match choice:
        case "1":
            name = input("Enter the recipe name: ").strip()
            description = input("Enter the recipe description: ").strip()
            
            ingredients = []
            while True:
                ingredient_name = input("Enter ingredient name (or 'done' to finish): ").strip()
                if ingredient_name.lower() == 'done':
                    break
                quantity = input(f"Enter quantity for {ingredient_name}: ").strip()
                ingredients.append({"name": ingredient_name, "quantity": quantity})
            
            instructions = []
            while True:
                instruction = input("Enter instruction (or 'done' to finish): ").strip()
                if instruction.lower() == 'done':
                    break
                instructions.append(instruction)
            
            RECIPE.add_recipe(name, description, ingredients, instructions)
        
        case "2":
            recipes = RECIPE.list_recipes()
            print("\nRecipes:")
            for recipe in recipes:
                print(f"{recipe[0]}: {recipe[1]}")
        
        case "3":
            pass
        
        case "4":
            program_running = False
        
        case _:
            print("Wrong choice. Please try again.")




