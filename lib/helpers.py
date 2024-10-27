# lib/helpers.py
from models.alcohol import Alcohol
from models.cocktail import Cocktail

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Enjoy Responsibly!")
    exit()

# Alcohol functions

def list_all_alcohols():
    all_alcohols = Alcohol.get_all()
    for i, alcohol in enumerate(all_alcohols, start=1):
        print(f"{i}. {alcohol.type_of} | Brand: {alcohol.brand} | Proof: {alcohol.proof}%")

# def find_alcohol_by_type():
#     type_of = input("Enter the type of alcohol: ")
#     alcohol = Alcohol.find_by_type_of(type_of)
#     print(alcohol) if alcohol else print(
#         f"Alcohol {type_of} not found")
    

def add_an_alcohol(type_of, brand, proof):
    type_of = input("Please enter a type of alcohol: ")
    brand = input("Please enter the brand name of alcohol: ")
    # proof = input("Please enter the proof or percentage of alcohol: ")

    while True:
        try:
            proof = int(input("Please enter the proof or percentage of alcohol: "))
            break
        except ValueError:
            print("Proof must be an integer")

    print("You have successfull added the proof")

    Alcohol.create(type_of = type_of, brand = brand, proof = proof)
    
    print(f"{type_of} has now been added to the Alcohol list")

def delete_an_alcohol(type_of):
    all_alcohols = Alcohol.get_all()
    list_all_alcohols()

    try:
        delete_alcohol = int(input("Please enter the alcohol # that you would like to delete"))
        if 1<= delete_alcohol <= len(all_alcohols):
            selected_alcohol = all_alcohols[delete_alcohol -1]
            selected_alcohol.delete()
            print(f"The alcohol type {selected_alcohol.type_of} has been deleted")
        else:
            print("Please try again")
    except ValueError:
        print("Invalid selection. Please try again.")

def update_an_alcohol(proof):
    all_alcohols = Alcohol.get_all()
    list_all_alcohols()

    try:
        update_alcohol = int(input("Which alcohol would you like to update?: "))
    except ValueError:
        print("Proof must be a number")
        return
    selected_alcohol = all_alcohols[update_alcohol -1]

    if selected_alcohol:
        try:
            proof = int(input("Please enter the updated proof: "))
        except ValueError:
            print("Proof must be a number")
            return
    
        selected_alcohol.proof = proof
        selected_alcohol.update()

    else:
        print("Alcohol not found. Please try again")

# Cocktails functions

def list_all_cocktails():
    all_cocktails = Cocktail.get_all()
    for i, cocktail in enumerate(all_cocktails, start=1):
        print(f"{i}. {cocktail.name}")


def list_all_cocktails_by_alcohol(alcohol_id):
    all_cocktails = Cocktail.find_by_alcohol(alcohol_id)
    for i, cocktail in enumerate(all_cocktails, start = 1):
        print(f"{i}. {cocktail.name}")
    return all_cocktails


def get_cocktails_by_alcohol(alcohol_id):
    all_cocktails = Cocktail.find_by_alcohol(alcohol_id)

    if all_cocktails:
        print(f"Cocktails: ")
        for i, cocktail in enumerate(all_cocktails, start = 1):
            print(f"{i}. {cocktail.name} | {cocktail.ingredients} | {cocktail.method}")
        else:
            print(f"No cocktails found with this alcohol")

def add_a_cocktail():
    list_all_alcohols()

    alcohol_index = input("Please enter the number of the alcohol you want to use:")

    try:
        alcohol_index = int(alcohol_index) -1
        all_alcohols = Alcohol.get_all()

        if 0 <= alcohol_index < len(all_alcohols):
            selected_alcohol = all_alcohols[alcohol_index]
        else:
            print("Invalid selection. Please try again.")
            return
    except ValueError:
        print("Please enter a valid number")
        return

    name = input("Please enter the name of the cocktail: ")
    ingredients = input("Please enter the ingredients: ")
    method = input("Please enter the method for making the cocktail:")

    Cocktail.create(name = name, ingredients = ingredients, method = method, alcohol_id = selected_alcohol.id)
    print(f"{name} successfully added to the cocktail list!")

def delete_a_cocktail():
    all_cocktails = list_all_cocktails()

    try:
        delete_cocktail_index = int(input("Select the number of the cocktail you want to delete: "))
        selected_cocktail = all_cocktails[delete_cocktail_index -1]

        confirm = input(f"Are you sure you want to delete '{selected_cocktail.name}'? (y/n): ")
        if confirm.lower() == 'y':
            selected_cocktail.delete()
            print(f"The cocktail '{selected_cocktail.name}' has been deleted.")
        else:
            print("Deletion canceled.")
        
    except(ValueError, IndexError):
        print("Invalid selection. Please try again.")

def update_a_cocktail(name, ingredients, method):
    all_cocktails = list_all_cocktails()

    try:
        update_cocktail_index = int(input("Select the number of the cocktail you'd like to update: "))
        selected_cocktail = all_cocktails[update_cocktail_index -1]
    except ValueError:
        print("Invalid selection. Please try again.")
        return
    try:
        update_name = input(f"Please update the name of {selected_cocktail.name}")
        update_ingredients = input(f"Please update the ingredients of {selected_cocktail.name}")
        update_method = input(f"Please update the method for {selected_cocktail.name}")
    except ValueError:
        print("Update not successful. Please try again.")

        selected_cocktail.name = update_name
        selected_cocktail.ingredients = update_ingredients
        selected_cocktail.method = update_method
        selected_cocktail.update()

        print(f"{selected_cocktail.name} has been updated successfully!")