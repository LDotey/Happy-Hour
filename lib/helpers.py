# lib/helpers.py
from models.alcohol import Alcohol
from models.cocktail import Cocktail

def header():
    print("***************************")

def footer():
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")

def exit_program():
    print("  Enjoy Responsibly!")
    print("")
    exit()

# Alcohol functions

def alcohol_menu():
    all_alcohols = Alcohol.get_all()
    for i, alcohol in enumerate(all_alcohols, start=1):
        print(f"{i}. {alcohol.type_of} | Brand: {alcohol.brand} | Proof: {alcohol.proof}%")
    # return all_alcohols
    # all_alcohols = starting_list()

    try:
        alcohol_choice = int(input("""\nWhich alcohol would you like to browse
                                   \nor press 0 to return to the previous menu: """))
        if alcohol_choice == 0:
            
                return None
            # exit_program()
        selected_alcohol = all_alcohols[alcohol_choice -1]
    except (IndexError, ValueError):
        print("Invalaid selection. Please try again.")
        return
    
    while True:
        print("")
        header()
        print("")
        print(f"{selected_alcohol.type_of} - {selected_alcohol.brand}")
        print("")
        print(f"1. List all {selected_alcohol.type_of} cocktails")
        print(f"2. Add a {selected_alcohol.type_of} cocktail")
        print(f"3. Delete a {selected_alcohol.type_of} cocktail")
        print(f"4. Update a {selected_alcohol.type_of} cocktail")
        print(f"5. Select a different alcohol")
        print("0. Back to the main menu")
        print("")
        footer()
        print("")

        cocktail_choice = input("Enter your selection >>>  ")
        if cocktail_choice == "0":
            break
        elif cocktail_choice == "1":
            list_all_cocktails_by_alcohol(selected_alcohol)
        elif cocktail_choice == "2":
            add_a_cocktail(selected_alcohol)
        elif cocktail_choice == "3":
            delete_a_cocktail(selected_alcohol)
        elif cocktail_choice == "4":
            update_a_cocktail()
        elif cocktail_choice == "5":
            alcohol_menu()
        else:
            print("Invalid choice")

def add_an_alcohol():
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

def delete_an_alcohol():

    all_alcohols = Alcohol.get_all()
    for i, alcohol in enumerate(all_alcohols, start=1):
        print(f"{i}. {alcohol.type_of} | Brand: {alcohol.brand} | Proof: {alcohol.proof}%")

    try:
        delete_alcohol = int(input("Please enter the alcohol # that you would like to delete"))
        if 1<= delete_alcohol <= len(all_alcohols):
            selected_alcohol = all_alcohols[delete_alcohol -1]
            selected_alcohol.delete()
            print(f"{selected_alcohol.type_of} has been deleted")
        else:
            print("Please try again")
    except ValueError:
        print("Invalid selection. Please try again.")

def update_an_alcohol():
    all_alcohols = Alcohol.get_all()
    for i, alcohol in enumerate(all_alcohols, start=1):
        print(f"{i}. {alcohol.type_of} | Brand: {alcohol.brand} | Proof: {alcohol.proof}%")

    try:
        update_alcohol = int(input("Which alcohol would you like to update?: "))
    except ValueError:
        print("Proof must be a number")
        return
    selected_alcohol = all_alcohols[update_alcohol -1]

    if selected_alcohol:
        try:
            type_of = input("Please enter the updated type of alcohol: ")
            brand = input("Please enter the updated brand: ")
            proof = int(input("Please enter the updated proof: "))
        except ValueError:
            print("Proof must be a number")
            return
    
        selected_alcohol.type_of = type_of
        selected_alcohol.brand = brand
        selected_alcohol.proof = proof
        selected_alcohol.update()
        print(f"{selected_alcohol.type_of} has been updated successfully!")


    else:
        print("Alcohol not found. Please try again")

# Cocktails functions

def list_all_cocktails():
    all_cocktails = Cocktail.get_all()
    if all_cocktails:
        for i, cocktail in enumerate(all_cocktails, start=1):
            print(f"{i}. {cocktail.name}")
    else:
        print("No cocktails found")
        all_cocktails

    while True:
        try:
            choice = int(input("Select which cocktail you'd like details of or press 0 to exit:  "))
            # import ipdb; ipdb.set_trace()
            if choice == 0:
                return None
            if 1 <= choice <= len(all_cocktails):
                selected_cocktail = Cocktail.find_by_id(all_cocktails[choice -1].id)
                formatted_cocktail = f"{selected_cocktail.name}\n{selected_cocktail.ingredients}\n{selected_cocktail.method}"
                print(formatted_cocktail)
            else:
                print("Invalid choice. Please try again. ")
        except ValueError:
            print("Please enter a valid number.")
           
def list_all_cocktails_by_alcohol(alcohol):
    # import ipdb; ipdb.set_trace()
    all_cocktails = alcohol.cocktails()
    if all_cocktails:
        for i, cocktail in enumerate(all_cocktails, start = 1):
            print(f"{i}. {cocktail.name}")
    else:
            print ("None found for this alcohol.")
    return all_cocktails

    

    # while True:
    #     print("")
    #     header()
    #     print("")
    #     print(f"2. Add a {selected_alcohol.type_of} cocktail")
    #     print(f"3. Delete a {selected_alcohol.type_of} cocktail")
    #     print(f"4. Update a {selected_alcohol.type_of} cocktail")
    #     print(f"5. Select a different alcohol")
    #     print("0. Back to the main menu")

def list_cocktails_for_selected_alcohol():
    all_alcohols = alcohol_menu()  # Get the list of alcohols
    try:
        alcohol_choice = int(input("Select which alcohol you'd like to see the cocktails of: "))
        selected_alcohol = all_alcohols[alcohol_choice - 1]  # Get the selected alcohol
        list_all_cocktails_by_alcohol(selected_alcohol)  # Use the alcohol_id
    except (IndexError, ValueError):
        print("Invalid selection. Please try again.")

def add_a_cocktail():
    alcohol_menu()

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

def delete_a_cocktail(selected_alcohol):
    # all_cocktails = list_all_cocktails_by_alcohol()
    all_cocktails = selected_alcohol.cocktails()
    if all_cocktails:
        for i, cocktail in enumerate(all_cocktails, start = 1):
            print(f"{i}. {cocktail.name}")

    try:
        delete_cocktail_index = int(input("Select the number of the cocktail you want to delete: "))
        selected_cocktail = all_cocktails[delete_cocktail_index -1]

        confirm = input(f"Are you sure you want to delete '{selected_cocktail.name}'? (y/n): ")
        if confirm.lower() == 'y':
            selected_cocktail.delete()
            print(f"The cocktail '{selected_cocktail.name}' has been deleted.")
            delete_alcohol_if_no_cocktails(selected_alcohol)
        else:
            print("Deletion canceled.")
        
    except(ValueError, IndexError):
        print("Invalid selection. Please try again.")

def update_a_cocktail():

    all_cocktails = list_all_cocktails()

    try:
        update_cocktail_index = int(input("Select the number of the cocktail you'd like to update: "))
        selected_cocktail = all_cocktails[update_cocktail_index -1]
    except ValueError:
        print("Invalid selection. Please try again.")
        return
    try:
        update_name = input(f"Please update the name of {selected_cocktail.name}: ")
        update_ingredients = input(f"Please update the ingredients of {selected_cocktail.name}: ")
        update_method = input(f"Please update the method for {selected_cocktail.name}: ")

        selected_cocktail.name = update_name
        selected_cocktail.ingredients = update_ingredients
        selected_cocktail.method = update_method
        selected_cocktail.update()

        print(f"{selected_cocktail.name} has been updated successfully!")

    except ValueError:
        print("Update not successful. Please try again.")

def delete_alcohol_if_no_cocktails(selected_alcohol):
    all_cocktails = selected_alcohol.cocktails()

    if not all_cocktails:
        selected_alcohol.delete()
        print(f"{selected_alcohol.type_of} has been deleted because there are no remaining {selected_alcohol.type_of} cocktails")
    else:
        print(f"{selected_alcohol.type_of} can not be deleted because there are still {selected_alcohol.type_of} cocktails remaining.")






# def get_cocktails_by_alcohol(alcohol_id):
#     all_cocktails = Cocktail.find_by_alcohol(alcohol_id)

#     if all_cocktails:
#         print(f"Cocktails: ")
#         for i, cocktail in enumerate(all_cocktails, start = 1):
#             print(f"{i}. {cocktail.name} | {cocktail.ingredients} | {cocktail.method}")
#     else:
#          print(f"No cocktails found with this alcohol")




# def find_alcohol_by_type():
#     type_of = input("Enter the type of alcohol: ")
#     alcohol = Alcohol.find_by_type_of(type_of)
#     print(alcohol) if alcohol else print(
#         f"Alcohol {type_of} not found")
    
