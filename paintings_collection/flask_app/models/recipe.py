from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.thirtymin = data['thirtymin']
        self.date = data['date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


    @classmethod
    def add_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, thirtymin, date, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(thirtymin)s, %(date)s, %(user_id)s);"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def edit_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, thirtymin = %(thirtymin)s, date = %(date)s WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL('recipes_schema').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes_schema').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes
    
    @classmethod
    def get_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL('recipes_schema').query_db(query, data)
        print(result, "wefwfwf")
        return result

    @staticmethod
    def validate_recipe(input):
        is_valid = True
        if len(input['name']) > 255 or len(input['name']) < 1:
            flash('Name must be between 1 and 255 characters')
            is_valid = False
        if len(input['description']) > 255 or len(input['description']) < 1:
            flash('Description must be between 1 and 255 characters')
            is_valid = False
        if len(input['instructions']) > 255 or len(input['instructions']) < 1:
            flash('Instructions must be between 1 and 255 characters')
            is_valid = False
        if len(input['date']) != 10:
            flash('Please input a correct date')
            is_valid = False
        return is_valid


