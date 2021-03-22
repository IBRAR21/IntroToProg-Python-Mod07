# ------------------------------------------------- #
# Title: Assignment 07
# Description: A script to save user name and age to a binary file with exception handling
# ChangeLog: (Who, When, What)
# IBRAR,03.21.2021,Created Script
# ------------------------------------------------- #

import pickle

# Data -------------------------------------------- #
file_name = 'Userdata.dat'  # Binary file storing user name and age
user_data = {}  # Dictionary to store data
user_data_lst = []  # List of dictionaries


# Processing -------------------------------------- #
def load_existing_data(binary_file):
    """This function loads the list from a binary file and creates a file if one doesnot exist."""

    try:
        f = open(binary_file, 'rb')
        list_of_rows = pickle.load(f)
        f.close()
    except FileNotFoundError:
        f = open(binary_file, 'wb')
        list_of_rows = []
        f.close()
    return list_of_rows


def add_new_data(data_dictionary, list_of_rows):
    if data_dictionary != {}:
        list_of_rows.append(data_dictionary)
    return list_of_rows


def save_data_to_file(binary_file, list_of_rows):
    """This function writes a list (containing dictionaries) to a binary file"""
    f = open(binary_file, 'wb')
    pickle.dump(list_of_rows, f)
    f.close()


# Presentation ------------------------------------ #
def new_user_data():
    """Gets user name and age and then saves them into a dictionary"""
    user_name = None
    user_age = None
    user_data = {}
    try:
        user_name = input("Please enter your name: ").strip()
        if user_name.isnumeric():
            raise Exception("\n Error: Name cannot have numbers!")
        user_age = input("Please enter your age: ").strip()
        if not (user_age.isnumeric()):
            raise Exception("\n Error: Age must be a numeric value!")
        user_data = {"Name": user_name, "Age": user_age}
    except Exception as e:
        print(e, "\n")
    return user_data


def show_existing_data(list_of_rows):
    """Prints the current list"""
    print("\nCurrent User Data: ")
    for row in list_of_rows:
        print(row["Name"], ",", row["Age"])
    print()


# Main() ------------------------------------ #

# Load existing data to list from existing binary file
user_data_lst = load_existing_data(file_name)

# Get user input
user_data = new_user_data()

# Add user input to the list
add_new_data(user_data, user_data_lst)

# Save the updated list to the binary file
save_data_to_file(file_name, user_data_lst)

# Display latest data
show_existing_data(user_data_lst)
