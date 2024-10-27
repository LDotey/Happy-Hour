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
        print(f"{i}. {alcohol.type_of} | Brand: {alcohol.brand} | Proof: {alcohol.proof}")

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

    alcohol_instance = Alcohol(type_of, brand, proof)
    alcohol_instance.save()
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


