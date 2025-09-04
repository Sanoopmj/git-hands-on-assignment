
new line added to dev branch

def login():
    # predefined username and password
    username = "admin"
    password = "12345"

    # take user input
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    # check credentials
    if user == username and pwd == password:
        print("✅ Login successful!")
    else:
        print("❌ Login failed! Invalid username or password.")

# call the function
login()
new line added to the features/login branch

