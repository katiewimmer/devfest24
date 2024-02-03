from info import USER_INFO, COMMUNITY_INFO

def get_user_info(email):
    user_info = USER_INFO.get(email, None)
    if user_info:
        password = USER_INFO.get('password', None)
        name = user_info.get('name', None)
        return password, name

def check_password_match(email, password):
    user_password = USER_INFO.get(email, {}).get('password', None)
    return password == user_password

def add_user(email, password, name):
    # Check if the email already exists in the dictionary
    if email in USER_INFO:
        print(f"Error: User with email {email} already exists.")
        return

    # Add the new user to the dictionary
    USER_INFO[email] = {'password': password, 'name': name}
    print(f"Successfully added user {name}!")

def get_community_info(name):
    community_info = COMMUNITY_INFO.get(name, None)
    if community_info:
        state = COMMUNITY_INFO.get('stateAbrv', None)
        population = COMMUNITY_INFO('population', None)
        return state, population


if authenticate_user(username, password):
    print("Authentication successful.")
else:
    print("Authentication failed.")
