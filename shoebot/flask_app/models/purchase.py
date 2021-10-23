from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from typing import final
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from flask_app.functions.purchasing_sites import amazon, bestbuy
# import random, string, re



class Purchase:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.link = data['link']
        self.purchase = data['purchase']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def add_purchase(cls, data):
        query = "INSERT INTO purchases (name, site, link, purchase, user_id) VALUES (%(name)s, %(site)s, %(link)s, 'N' , %(user_id)s);"

        return connectToMySQL('shoebot_schema').query_db(query, data)


    @classmethod
    def delete_purchase(cls, data):
        query = "DELETE FROM purchases WHERE id = %(id)s"
        return connectToMySQL('shoebot_schema').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM purchases;"
        results = connectToMySQL('shoebot_schema').query_db(query)
        paintings = []
        for painting in results:
            paintings.append( cls(painting) )
        return paintings
    
    @classmethod
    def get_purchase(cls, data):
        query = "SELECT * FROM purchases WHERE id = %(id)s;"
        result = connectToMySQL('shoebot_schema').query_db(query, data)
        return result
    
    @classmethod
    def purchased(cls):
        query = "Select id FROM purchases ORDER BY id DESC LIMIT 1"
        result = connectToMySQL('shoebot_schema').query_db(query)
        print(result)
        print(result[0])
        data = {
            'id': result[0]['id']
        }
        query2 = "UPDATE purchases SET purchase = 'Y' WHERE id = %(id)s"
        return connectToMySQL('shoebot_schema').query_db(query2, data)

    @classmethod
    def amazon(cls):
        return amazon()

    @classmethod
    def bestbuy(cls):
        return bestbuy()
    
        


        
\

