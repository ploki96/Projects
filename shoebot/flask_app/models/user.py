from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.purchase import Purchase
from flask_app.models.login_info import Login_Info
from flask import flash
import re
        


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]{8,255}$')
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9._-]{2,255}$')
NAME_REGEX = re.compile(r"^[A-Z]{1}[\w. '-]{1,254}$") 


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.purchases = []
        self.login_infos = []
    
    @classmethod
    def single_user(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        user = connectToMySQL('shoebot_schema').query_db(query, data)
        return user[0]
        

    @classmethod
    def single_user_w_purchases(cls, data):
        query = "SELECT * FROM users LEFT JOIN purchases ON users.id = purchases.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL('shoebot_schema').query_db(query, data)
        user = cls(results[0])
        for row in results:
            purchase = {
                'id': row['purchases.id'],
                'name': row['name'],
                'link': row['link'],
                'purchase': row['purchase'],
                'created_at': row['purchases.created_at'],
                'updated_at': row['purchases.updated_at'],
                'user_id': row['user_id']
            }
            user.purchases.append(Purchase(purchase))
        return user

    @classmethod
    def single_user_w_logins(cls, data):
        query = "SELECT * FROM users LEFT JOIN login_infos ON users.id = login_infos.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL('shoebot_schema').query_db(query, data)
        user = cls(results[0])
        for row in results:
            login_info = {
                'id': row['login_infos.id'],
                'website': row['website'],
                'username': row['username'],
                'password': row['password'],
                'created_at': row['login_infos.created_at'],
                'updated_at': row['login_infos.updated_at'],
                'user_id': row['user_id']
            }
            user.login_infos.append(Login_Info(login_info))
        return user

    # @classmethod
    # def show_purchases(cls, data):
    #     query = "SELECT * FROM users_paintings LEFT JOIN users ON users.id = users_paintings.user_id WHERE users.id = %(id)s;"
    #     results = connectToMySQL('shoebot_schema').query_db(query, data)
    #     return results


    # @classmethod
    # def purchase(cls, data):
    #     query = "SELECT * FROM users_paintings WHERE user.id = %(users)s AND painting.id = %(paintings)s;"
    #     result = connectToMySQL('shoebot_schema').query_db(query, data)
    #     if not result:
    #         query = "INSERT INTO users_paintings (users_paintings.user_id, users_paintings.painting_id) VALUES (%(users)s, %(paintings)s);"
    #         return connectToMySQL('shoebot_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('shoebot_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('shoebot_schema').query_db(query, data)

    @classmethod
    def check_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('shoebot_schema').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @staticmethod
    def validate_user(input):
        is_valid = True

        query = "SELECT * FROM users WHERE email = %(email)s;"
        results_email = connectToMySQL('shoebot_schema').query_db(query, input)
        if len(results_email) >= 1:
            flash('Email address already used.')
            is_valid = False

        if not NAME_REGEX.match(input['first_name']): 
            flash("Invalid first name!")
            is_valid = False

        if not NAME_REGEX.match(input['last_name']): 
            flash("Invalid last name!")
            is_valid = False

        if not EMAIL_REGEX.match(input['email']): 
            flash("Invalid email!")
            is_valid = False
        
        if not PASSWORD_REGEX.match(input['password']): 
            flash("Invalid password")
            is_valid = False
        return is_valid
        
