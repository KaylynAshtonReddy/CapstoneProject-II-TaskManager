# This program will provide assistance for a small business
# that can help it to manage tasks assigned to each member of the team

# ======Updates to file============
# Ammended the menu to add in additional section if the user is an admin
# Updated variable names


# =====importing libraries===========
# Import datetime libraries for recording current date
from datetime import datetime

date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")

# =====Login==========================

# Declaring variables for the while loop to run
logged_in = False

# Creating empty string variable that will be assigned new values
# Opening the file containing the registered usernames and passwords
user_name_saved = ""
password_saved = ""
user_file = open("user.txt", "r")

# The loop will continue to request a user to login until
#  a user contained in the User.txt file logs in


def login():
    while not logged_in:

        # Request user for input within the loop, so that it can continue requesting input
        login_user = input("Kindly enter your username: ")
        login_pass = input(
            "Kindly enter your password for username '{}': ".format(login_user))

        # Loop through each line in the file to search
        # if the entered username and password matches any contained in the file
        for lines in user_file:

            # Strip the white spaces between words
            # Split the words by the comma and a space
            # Using index slicing to create a temporary column for usernames and passwords in the file
            temp = lines.strip()
            temp = temp.split(", ")
            user_name_saved = temp[0]
            password_saved = temp[1]

            # A nested if stated condition if the username and password matches
            # If a match is found, the While Loop beomes True and stops running
            if login_user == user_name_saved and login_pass == password_saved:
                logged_in = True
                print("\n Welcome to the Task Manager!\n  ")
                user_file.seek(0)
                break

        # If no match is found the while loop will stay False and continue to run
        # Requesting the user to enter in the credentials
        if login_user != user_name_saved or login_pass != password_saved:
            logged_in = False
            print("Please enter a valid username and password")
            user_file.seek(0)

    # Closing the file
    user_file.close


login()

# New loop for logged in user
while True:

    if login_user != "admin":
        # presenting the standard_menu to the user and
        # making sure that the user input is converted to lower case.
        standard_menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        e - Exit:
    ''').lower()

    if login_user == "admin":
        # presenting the admin standard_menu to the user
        standard_menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        adm - admin standard_menu
        e - Exit:
    ''').lower()

    # Setting a condition which will only allow the 'admin' user access to register a user
    if standard_menu == "r":
        if login_user != "admin":

            print("\n You are not an admin user, only admin can register new users. \n")

        elif login_user == "admin":

            #         # Create a new menu to display for admin.
            #         admin_menu = (input("""
            # Please select one of the following options:
            # r - register a new user
            # d - display statistics = Total number of tasks & users
            # e - exit
            # """))

            # Requesting the admin user to enter new details for user to be registered.
            # if menu == "r":

            new_user = (input("Please enter a new user name: "))
            new_user_password = (input("Please enter a new password: "))

            new_password = False

            # Add a 'while loop' untill the condition is met(True).
            # Admin user is requested to enter the password twice
            # Only if both passwords match will the data be saved to the user.txt file.
            while new_password == False:
                confirm_new_password = input(
                    "Please retype your password to confirm: ")

                if new_user_password == confirm_new_password:
                    new_password = True

                elif new_password == False:
                    print("Your passwords do not match!")

                elif standard_menu == "e":
                    exit()

            # Close file
            with open('user.txt', 'a')as user_file:
                user_file.write(f"\n{new_user}, {new_user_password}")

        # standard_menu item to display statistics for all users
    elif standard_menu == "adm":
        admin_menu = (input("""
    Please select one of the following options:
    d - display statistics = Totaadminl number of tasks & users
    e - exit
    """))
        if admin_menu == 'd':
            # These varibles will only count the lines inside the 'txt' files,
            # but since we are storing every new task & user on a new line,
            # we can just count the lines for the desired results.
            num_of_tasks = 0
            num_of_users = 0

            with open("tasks.txt", "r") as task_file:
                for line in task_file:
                    num_of_tasks += 1
            print("\n See below statistics: \n")
            print(f"\nTotal number of tasks: {num_of_tasks}")

            with open("user.txt", "r") as user_file:
                for line in user_file:
                    num_of_users += 1
            print(f"Total number of users: {num_of_users}\n")

        elif standard_menu == "e":
            exit()

    # standard_menu item to add a task
    # Logged in user will be requested to enter some data
    # Data will be stored into the tasks.txt file
    elif standard_menu == 'a':
        pass

        user_name_task = input("Enter in the username: ")
        user_task_title = input("Enter in the title of the task: ")
        user_task_descrip = input("Enter in the description of the task: ")
        task_due_date = input("Enter in the due date: ")

        with open("tasks.txt", "a") as tasks:

            tasks.write(("\n" + user_name_task + "," + " " +
                         user_task_title + ", " + user_task_descrip + ", " + task_due_date + date + ","+"No"))

            print("\n Task has been successfully added!")

    # standard_menu item which will allow the logged in user to view all the tasks
    # which are assigned to every user
    elif standard_menu == 'va':
        pass

        task_file = open("tasks.txt", "r")

        # Looping through each line item, splitting it
        # Using list comprehension to create variables for each index in list
        for line in task_file:
            new_task_username, new_task_tile, new_task_description, new_task_due_date, new_task_completion_date = line.split(
                ",", maxsplit=4)

            # Formatting the print display for an easy to read view
            print(f"""
        New task username:       {new_task_username}
        Task tile:              {new_task_tile}
        Task description:       {new_task_description}
        Task due date:          {new_task_due_date}
        Task completion:         {new_task_completion_date}
        """)

        task_file.close()

    # standard_menu item to view the tasks assigned to the currently logged in user
    elif standard_menu == 'vm':
        pass

        with open("tasks.txt", "r") as task_file:

            print("\n Listed below are all your tasks: \n")

            for line in task_file.readlines():
                new_task_username, new_task_tile, new_task_description, new_task_due_date, new_task_completion_date = line.split(
                    ",", maxsplit=4)

                # Condition to check which user is actually logged in
                if login_user == new_task_username:

                    # Formatting the print display for an easy to read view
                    print(f"""
                    New task username:       {new_task_username}
                    Task tile:              {new_task_tile}
                    Task description:       {new_task_description}
                    Task due date:          {new_task_due_date}
                    Task completion:         {new_task_completion_date}
                    """)

        task_file.close()

    elif standard_menu == 'e':
        print('Goodbye!!!')

        exit()

    # Print the below message,if the user enters a value that is not listed in the menu
    else:
        print("You have made a wrong choice, Please Try again")
