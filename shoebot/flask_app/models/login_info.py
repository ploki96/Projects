from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash



class Login_Info:
    def __init__(self, data):
        self.id = data['id']
        self.website = data['website']
        self.username = data['username']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def add_login_info(cls, data):
        query = "INSERT INTO login_infos (name, link, purchased, user_id) VALUES (%(name)s, %(link)s, 'N' , %(user_id)s);"
        return connectToMySQL('shoebot_schema').query_db(query, data)


    @classmethod
    def delete_login_info(cls, data):
        query = "DELETE FROM login_infos WHERE id = %(id)s"
        return connectToMySQL('shoebot_schema').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM login_infos;"
        results = connectToMySQL('shoebot_schema').query_db(query)
        paintings = []
        for painting in results:
            paintings.append( cls(painting) )
        return paintings
    
    @classmethod
    def get_login_info(cls, data):
        query = "SELECT * FROM login_infos WHERE id = %(id)s;"
        result = connectToMySQL('shoebot_schema').query_db(query, data)
        return result
