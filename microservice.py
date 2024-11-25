import time

def write_to_users_file(username, password):
    # Adds a new user to users.txt.
    with open("users.txt", "a") as file:
        file.write(f"\n{username}:{password}")

def check_credentials(username, password):
    # Checks if the username and password exist in users.txt.
    with open("users.txt", "r") as file:
        for line in file:
            user, passw = line.strip().split(":")
            if user == username and passw == password:
                return True
    return False

def main():
    time.sleep(1)
    welcome = input("Already have an account? (yes/no): ").strip().lower()

    if welcome == "no":
        # Create a new account
        username = input("Enter a username: ").strip()
        password = input("Enter a password: ").strip()

        # Save new user information to users.txt
        write_to_users_file(username, password)
        # Write to output.txt upon successful login
        with open("output.txt", "w") as file:
            file.write(f"User {username} created successfully.")
        print("Account created successfully!")

    elif welcome == "yes":
        # Log in with an existing account
        login_attempts = 3  # Allow 3 attempts to log in
        while login_attempts > 0:
            login1 = input("Username: ").strip()
            login2 = input("Password: ").strip()

            if check_credentials(login1, login2):
                print("Login Success!")
                # Write to output.txt upon successful login
                with open("output.txt", "w") as file:
                    file.write(f"User {login1} logged in successfully.")
                break
            else:
                login_attempts -= 1
                print(f"Incorrect username or password. Attempts left: {login_attempts}")

        if login_attempts == 0:
            print("Attempts exceeded. Access denied.")
            with open("output.txt", "w") as file:
                file.write("Login failed: more than three attempts.")

    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
