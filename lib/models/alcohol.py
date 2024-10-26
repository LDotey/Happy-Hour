from models.__init__ import CURSOR, CONN


class Alcohol:


    def __init__(self, type_of, brand, proof, id = None):
        self.id = id
        self.type_of = type_of
        self.brand = brand
        self.proof = proof
 