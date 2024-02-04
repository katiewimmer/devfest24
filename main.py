from info import USER_INFO, COMMUNITY_INFO, VALID_STATES, ADMIN_INFO, EVENTS

## Functions for Users
def get_user_info(email):
    user_info = USER_INFO.get(email, None)
    if user_info:
        password = USER_INFO.get('password', None)
        name = user_info.get('name', None)
        return name

def check_user_password_match(email, password):
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

## Functions for Communities
def get_community_info(name, state):
    key = f"{name}_{state}"
    community_data = COMMUNITY_INFO.get(key, None)

    if community_data:
        population = community_data.get('population', None)
        return population
    else:
        return None, None

def add_community(name, state, pop):
    key = f"{name}_{state}"
    
    # Checks that the community doesn't already exist
    if key not in COMMUNITY_INFO:
        # Checks if the state abbreviation is valid
        if state.upper() in VALID_STATES and len(state) == 2:
            COMMUNITY_INFO[key] = {'stateAbrv': state.upper(), 'population': pop}
            print(f"Community '{name}, {state}' added successfully.")
        else:
            print(f"Error: '{state}' is not a valid state abbreviation.")
    else:
        print(f"Community '{name}, {state}' already exists.")

## Functions for Admins
def get_admin_info(email):
    admin_info = ADMIN_INFO.get(email, None)
    if admin_info:
        password = USER_INFO.get('password', None)
        name = ADMIN_INFO.get('name', None)
        return name

def check_admin_password_match(email, password):
    admin_password = ADMIN_INFO.get(email, {}).get('password', None)
    return password == admin_password

def add_admin(email, password, name):
    if email not in ADMIN_INFO:
        ADMIN_INFO[email] = {'password': password, 'name': name, 'communities': []}
        print(f"Admin '{name}' added successfully.")
    else:
        print(f"Admin '{name}' already exists.")


def add_community_info(city, state, population):
    if city in COMMUNITY_INFO:
        print("Error: Community already Exists!")
        return
    else:
        COMMUNITY_INFO[city] = {'stateAbrv': state, 'population': population}
        print(f"Successfully added community {city}!")


def add_event(title, community, status, address, tasks, admin_name):

    if community not in COMMUNITY_INFO:
        print("Error: Community doesn't exists!")
        return
    EVENTS[title] = {"Community" : community,
                     "Status" : status,
                     "Creator" : admin_name,
                     "Address" : address,
                     "Members" : [],
                     "Tasks" : []}
    

def add_member_to_event(title, member):
    if title not in EVENTS:
        print("Error: Event doesn't exists!")
    EVENTS[title]["Members"].add(member)

def change_task_status(title, admin_name, status, event, task):
    if admin_name not in event:
        print("Error: Unauthorized User")
        return
    EVENTS[title][event]["tasks"][task] = status

def add_task(event, admin_name, new_task_name):
    if admin_name not in event:
        print("Error: Unauthorized User")
        return
    EVENTS[event]["tasks"][new_task_name] = False

def overall_event_status(title, admin, event, status):
    if admin not in event:
        print("Error: Unauthorized User")
        return
    EVENTS[title][event]["Overall"] = status


def town_search(town):

    city = ''
    for ch in town:
        if ch != ',':
            city += ch
        else:
            state = town[-2] + town[-1]
            break
    print("TOWN:", city)
    print("STATE:", state)
    admin_list = []
    event_list = []
    for admin in ADMIN_INFO:
        
        for com in ADMIN_INFO[admin]['communities']:
            print("Com: ", com,"\n")
            if com == (city,state):
                admin_list.append(ADMIN_INFO[admin])
                break
    for event in EVENTS:
        if EVENTS[event]['Community'] == (city,state):
            event_list.append(EVENTS[event])

    return admin_list, event_list
