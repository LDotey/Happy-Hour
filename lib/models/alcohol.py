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

    def save(self):
        sql = '''
            INSERT INTO alcohols (type_of, brand, proof)
            VALUES (?, ?, ?)
            '''
        
        CURSOR.execute(sql, (self.type_of, self.brand, self.proof))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, type_of, brand, proof):
        alcohol = cls(type_of, brand, proof)
        alcohol.save()
        return alcohol
    
    def update(self):
        sql = '''
            UPDATE alcohols
            SET type_of =?, brand = ?, proof = ?
            WHERE id = ?
            '''
        CURSOR.execute(sql, (self.type_of, self.brand, self.proof))
        CONN.commit()

    def delete(self):
        sql = '''
            DELETE FROM alcohols
            WHERE id = ?
            '''
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):

        alcohol = cls.all.get(row[0])
        if alcohol:
            alcohol.type_of = row[1]
            alcohol.brand = row[2]
            alcohol.proof = row[3]
        else:
            alcohol = cls(row[1], row[2], row[3])
            alcohol.id = row[0]
            cls.all[alcohol.id] = alcohol
        return alcohol
    
    @classmethod
    def get_all(cls):
        sql = '''
            SELECT *
            FROM alcohols
            '''
        
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    