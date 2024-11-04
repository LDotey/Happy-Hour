# lib/cli.py

from helpers import (
    exit_program,
    # helper_1,
    # list_all_alcohols,
    alcohol_menu,
    add_an_alcohol,
    delete_an_alcohol, 
    update_an_alcohol, 
    list_all_cocktails,
    # list_all_cocktails_by_alcohol, 
    # list_cocktails_for_selected_alcohol,
    # get_cocktails_by_alcohol,
    # add_a_cocktail,
    # delete_a_cocktail,
    # update_a_cocktail
)


def main():
    while True:
        menu()
        choice = input(">>> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            alcohol_menu()
        elif choice == "2":
            add_an_alcohol()
        elif choice == "3":
            delete_an_alcohol()
        elif choice == "4":
            update_an_alcohol()
        elif choice == "5":
            list_all_cocktails()

        else:
            print("Invalid choice")


def menu():
    print("")
    print(" ~ Welcome to Happy Hour ~ ")
    print("")
    print("  Please select an option: ")
    print("")
    print("1. List all alcohols")
    print("2. Add an alcohol")
    print("3. Delete an alcohol")
    print("4. Update an alcohol")
    print("5. List all cocktails")
    print("")
    print("Press 0 to exit the program")
    print("")
    # print("6. List all cocktails by alcohol type")
    # print("7. Add a cocktail")
    # print("8. Delete a cocktail")
    # print("9. Update a cocktail")





if __name__ == "__main__":
    main()
