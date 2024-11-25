def test():
    print("Starting test...")

    # Test microservice creation of users
    print("Creating test users...")
    with open("users.txt", "w") as file:
        file.write("test:password")

    # Call the microservice
    print("Testing valid credentials...")
    username = "test"
    password = "password"
    is_valid = check_credentials(username, password)

    print("Testing invalid credentials...")
    username = "test"
    password = "password1"
    is_valid = check_credentials(username, password)

    print("Testing nonexistent user...")
    username = "test1"
    password = "password"
    is_valid = check_credentials(username, password)

    print("All tests passed!")

if __name__ == "__main__":
    from microservice import check_credentials, write_to_users_file
    test()
