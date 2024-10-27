# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
    list_all_alcohols,
    add_an_alcohol,
    delete_an_alcohol, 
    update_an_alcohol
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_all_alcohols()
        elif choice == "2":
            add_an_alcohol()
        elif choice == "3":
            delete_an_alcohol()
        elif choice == "4":
            update_an_alcohol()

        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all alcohols")
    print("2. Add an alcohol")
    print("3. Delete an alcohol")
    print("4. Update an alcohol")
    print("5. ")
    print("6. ")


if __name__ == "__main__":
    main()
