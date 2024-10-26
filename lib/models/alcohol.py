from models.__init__ import CURSOR, CONN


class Alcohol:

    all = {}

    def __init__(self, type_of, brand, proof, id = None):
        self.id = id
        self.type_of = type_of
        self.brand = brand
        self.proof = proof
    
    @property
    def type_of(self):
        return self._type_of
    
    @type_of.setter
    def type_of(self, type_of):
        if isinstance(type_of, str) and len(type_of):
            self._type_of = type_of
        else: 
            raise ValueError("Type_of must be a non-empty string")
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str) and len(brand):
            self._brand = brand
        else:
            raise ValueError("Brand must be a non-empty string")
        
    @property
    def proof(self):
        return self._proof
    
    @proof.setter
    def proof(self, proof):
        if isinstance(proof, int) and proof >= 1 and proof <= 200:
            self._proof = proof
        else:
            raise ValueError("Proof must be a number between 1 and 200")
        
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS alcohols (
            id INTEGER PRIMARY KEY, 
            type_of TEXT
            brand TEXT
            proof INTEGER)
            '''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS alcohols;
            '''
        CURSOR.execute(sql)
        CONN.commit()