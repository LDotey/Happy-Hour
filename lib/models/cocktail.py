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