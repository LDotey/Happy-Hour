from models.__init__ import CONN, CURSOR
from models.cocktail import Cocktail
from models.alcohol import Alcohol

def seed_database():
    Cocktail.drop_table()
    Cocktail.create_table()
    Alcohol.drop_table()
    Alcohol.create_table()


# Add alcohols for testing
    Alcohol.create("Gin", "Hendricks", 40)
    Alcohol.create("Tequila", "Casamigos", 60)
    Alcohol.create("Bourbon", "Bulliet", 50)
    Alcohol.create("Rum", "Goslings", 40)
    Alcohol.create("Vodka", "Grey Goose", 40)


# Add cocktails for testing
    Cocktail.create("Paloma","Tequila, pink grapefruit juice, soda, fresh lime", "Mix 1.5oz tequila with 2oz juice and 1oz soda. Garnish with fresh lime", 2)
    Cocktail.create("Negroni", "Gin, Campari, Sweet Vermouth", "Mix equal parts of all 3 ingredients. Serve on ice", 1)
    Cocktail.create("Gin Martini", "Gin, Dry Vermouth, Bitters", "Add vermouth and gin to a glass of ice and stir. Strain into a chilled glass. Garnish with an olive", 1)
    Cocktail.create("Vodka Martini", "Vodka, Dry Vermouth", "Add vodka and dry vermouth to a shaker of ice. After shaking, straing into a chilled glass. Garnish with lemon peel", 5)
    Cocktail.create("Old Fashioned", "Bourbon, bitters, sugar", "Combine sugar, bitters and a splash of water to a whiskey glass. Once combined add ice to liking and 1.5oz of bourbon. Garnish with a luxardo cherry", 3)
    Cocktail.create("Dark & Stormy", "Dark rum, ginger beer, bitters", "Combine 2oz of dark rum with 3.5oz of ginger beer. Top with a dash of bitters and garnish with lime", 4)


seed_database()