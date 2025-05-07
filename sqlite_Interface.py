import sqlite3
class SQLiteInterface:

    def __init__(self):
        self.con = sqlite3.connect("recipe.db")
        self.cursor = self.con.cursor()

        if not self.check_table_exists():
            self.create_table()


#-----------------------------------------------------------------------
   #check if a table is there 
    def check_table_exists(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='recipes'")
        return self.cursor.fetchone() is not None

#-----------------------------------------------------------------------
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT UNIQUE NOT NULL,
                            description TEXT NOT NULL
                    )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredients (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT UNIQUE NOT NULL,
                            quantity TEXT NOT NULL,
                            recipe_id INTEGER NOT NULL,
                            FOREIGN KEY (recipe_id) REFERENCES recipes (id)
                    )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS instructions (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            step_number INTEGER NOT NULL,
                            instruction TEXT NOT NULL,
                            recipe_id INTEGER NOT NULL,
                            FOREIGN KEY (recipe_id) REFERENCES recipes (id)
                    )
        """)
        self.con.commit()
        print("Table created successfully")

#-----------------------------------------------------------------------
    def add_recipe(self, name, description):  #add a recipe to the database
        try:
            self.cursor.execute("INSERT INTO recipes (name, description) VALUES (?, ?)", (name, description))
            self.con.commit()
            print(f"Recipe '{name}' added successfully")
        except sqlite3.IntegrityError:
            print(f"Recipe '{name}' already exists")
            
    def add_ingredient(self, name, quantity, recipe_id):  #add an ingredient to the database
        try:
            self.cursor.execute("INSERT INTO ingredients (name, quantity, recipe_id) VALUES (?, ?, ?)", (name, quantity, recipe_id))
            self.con.commit()
            print(f"Ingredient '{name}' added successfully to recipe ID {recipe_id}")
        except sqlite3.IntegrityError:
            print(f"Ingredient '{name}' already exists in recipe ID {recipe_id}")
            
    def add_instruction(self, step_number, instruction, recipe_id):  #add an instruction to the database
        try:
            self.cursor.execute("INSERT INTO instructions (step_number, instruction, recipe_id) VALUES (?, ?, ?)", (step_number, instruction, recipe_id))
            self.con.commit()
            print(f"Instruction '{instruction}' added successfully to recipe ID {recipe_id}")
        except sqlite3.IntegrityError:
            print(f"Instruction '{instruction}' already exists in recipe ID {recipe_id}")
            
            
#-----------------------------------------------------------------------
    def get_all_recipes(self):
        self.cursor.execute("Select id, name FROM recipes")
        recipes = self.cursor.fetchall()
        return recipes
    