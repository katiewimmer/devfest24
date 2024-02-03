from info import users_info

def authenticate_user(username, password):
    if username in users_info and users_info[username] == password:
        return True
    return False

# Example usage
username = input("Enter username: ")
password = input("Enter password: ")

if authenticate_user(username, password):
    print("Authentication successful.")
else:
    print("Authentication failed.")
