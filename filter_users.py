import json

def read_file():
    """
    Opens and reads the users.json file
    :return: users data
    """
    try:
        with open("users.json", "r") as file:
            users = json.load(file)

        return users

    except FileNotFoundError:
        print("Error: The file 'users.json' was not found.")
        raise

    except json.JSONDecodeError:
        print("Error: The file 'users.json' contains invalid JSON.")
        raise


def filter_users_by_name(name, users):
    """
    Filter the users data by name
    Prints user data which fits to that name
    """
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age, users):
    """
    Filter users data by parameter age
    Prints user data which fits to that age
    """
    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email, users):
    """
    Filter  users data by parameter email
    Prints user data which fits to that email
    """
    filtered_users = [user for user in users if email in user["email"]]

    for user in filtered_users:
        print(user)


def main():
    """
    Asks the user to input the way to filter the data.
    Asks to enter the name/age/email to filter for.
    Executes the funktion by which the data gets filtered
    Prints a message if an invalid filter option was chosen
    """
    users = read_file()

    try:
        filter_option = input(
            "What would you like to filter by? (Currently, only 'name', 'age', 'email'): ").strip().lower()

        if filter_option == "name":
            name_to_search = input("Enter a name to filter users: ").strip()
            filter_users_by_name(name_to_search, users)

        if filter_option == "age":
            age_to_search = int(input("Enter an age to filter users: "))
            filter_users_by_age(age_to_search, users)

        if filter_option == "email":
            email_to_search = input("Enter an email to filter users: ").lower()
            filter_users_by_email(email_to_search, users)

    except ValueError:
        print("Invalid Input: age needs to be a number.")

if __name__ == "__main__":
    main()