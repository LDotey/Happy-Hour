from models.__init__ import CURSOR, CONN
from models.alcohol import Alcohol

class Cocktail:

    all = {}

    def __init__(self, name, ingredients, method, alcohol_id, id = None):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.method = method
        self.alcohol_id = alcohol_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def ingredients(self):
        return self._ingredients
    
    @ingredients.setter
    def ingredients(self, ingredients):
        if isinstance(ingredients, str) and len(ingredients):
            self._ingredients = ingredients
        else:
            raise ValueError("Ingredients must be a non-empty string")
        
    @property
    def method(self):
        return self._method
    
    @method.setter
    def method(self, method):
        if isinstance(method, str) and len(method):
            self._method = method
        else:
            raise ValueError("Method must be a non-empty string")
        
    @property
    def alcohol_id(self):
        return self._alcohol_id
    
    @alcohol_id.setter
    def alcohol_id(self, alcohol_id):
        if type(alcohol_id) is int and Alcohol.find_by_id(alcohol_id):
            self._alcohol_id = alcohol_id
        else:
            raise ValueError("Alcohol_id must reference an alcohol in the database")
        
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Cocktail instances"""
        sql = '''
            CREATE TABLE IF NOT EXISTS cocktails
            id INTEGER PRIMARY KEY,
            name TEXT, 
            ingredients TEXT, 
            method TEXT
            alcohol_id INTEGER, 
            FOREIGN KEY (alcohol_id) REFERENCES alcohols(id)
            '''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Cocktail instances"""
        sql = '''
            DROP TABLE IF EXISTS cocktails
            '''
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = '''
            INSERT INTO cocktails (name, ingredients, method, alcohol_id)
            VALUES (?, ?, ?, ?)
            '''
        CURSOR.execute(sql, (self.name, self.ingredients, self.method, self.alcohol_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = '''
            UPDATE cocktails
            SET name = ?, ingredients = ?, method = ?, alcohol_id = ?
            WHERE id = ?
            '''
        CURSOR.execute(sql, (self.name, self.ingredients, self.method, self.alcohol_id, self.id))
        CONN.commit()

    def delete(self):
        sql = '''
            DELETE FROM cocktails
            WHERE id = ?
            '''
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

