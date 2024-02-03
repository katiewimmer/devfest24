
USER_INFO = {
    'john.doe@example.com': {'password': 'jd_pass123', 'name': 'John Doe'},
    'alice.smith@example.com': {'password': 'as_pass456', 'name': 'Alice Smith'},
    'bob.jones@example.com': {'password': 'bj_pass789', 'name': 'Bob Jones'},
    'susan.white@example.com': {'password': 'sw_pass123', 'name': 'Susan White'},
    'david.jackson@example.com': {'password': 'dj_pass456', 'name': 'David Jackson'},
    'emma.jones@example.com': {'password': 'ej_pass789', 'name': 'Emma Jones'},
    'michael.smith@example.com': {'password': 'ms_pass123', 'name': 'Michael Smith'},
    'olivia.davis@example.com': {'password': 'od_pass456', 'name': 'Olivia Davis'},
    'nathan.wilson@example.com': {'password': 'nw_pass789', 'name': 'Nathan Wilson'},
    'chloe.taylor@example.com': {'password': 'ct_pass123', 'name': 'Chloe Taylor'},
    'james.anderson@example.com': {'password': 'ja_pass456', 'name': 'James Anderson'},
    'lily.martin@example.com': {'password': 'lm_pass789', 'name': 'Lily Martin'},
    'ryan.miller@example.com': {'password': 'rm_pass123', 'name': 'Ryan Miller'},
    'ava.johnson@example.com': {'password': 'aj_pass456', 'name': 'Ava Johnson'},
    'william.moore@example.com': {'password': 'wm_pass789', 'name': 'William Moore'},
}

COMMUNITY_INFO = {
    'Townsville': {'stateAbrv': 'CA', 'population': 5000},
    'Villageville': {'stateAbrv': 'NY', 'population': 3000},
    'Hamletville': {'stateAbrv': 'TX', 'population': 2000},
    'Cityburg': {'stateAbrv': 'FL', 'population': 8000},
    'New York': {'stateAbrv': 'NY', 'population': 8336817},
    'Los Angeles': {'stateAbrv': 'CA', 'population': 3979576},
    'Chicago': {'stateAbrv': 'IL', 'population': 2693976},
    'Houston': {'stateAbrv': 'TX', 'population': 2320268},
    'Phoenix': {'stateAbrv': 'AZ', 'population': 1680992},
    'Philadelphia': {'stateAbrv': 'PA', 'population': 1584138},
    'San Antonio': {'stateAbrv': 'TX', 'population': 1547253},
    'San Diego': {'stateAbrv': 'CA', 'population': 1423851},
    'Dallas': {'stateAbrv': 'TX', 'population': 1343573},
    'San Jose': {'stateAbrv': 'CA', 'population': 1030119},
    'Austin': {'stateAbrv': 'TX', 'population': 964254},
    'Jacksonville': {'stateAbrv': 'FL', 'population': 903889},
    'Fort Worth': {'stateAbrv': 'TX', 'population': 895008},
    'Columbus': {'stateAbrv': 'OH', 'population': 892533},
    'Charlotte': {'stateAbrv': 'NC', 'population': 885708},
    'San Francisco': {'stateAbrv': 'CA', 'population': 881549},
    'Indianapolis': {'stateAbrv': 'IN', 'population': 876384},
    'Seattle': {'stateAbrv': 'WA', 'population': 744955},
    'Denver': {'stateAbrv': 'CO', 'population': 716492},
    'Washington': {'stateAbrv': 'DC', 'population': 702455},
}

VALID_STATES = {'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 
                'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 
                'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 
                'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'}

ADMIN_INFO = {
    'admin1@example.com': {
        'password': 'admin1_pass',
        'name': 'Admin One',
        'communities': ['Washington', 'Columbus']
    },
    'admin2@example.com': {
        'password': 'admin2_pass',
        'name': 'Admin Two',
        'communities': ['Dallas', 'Fort Worth']
    },
    'john.admin@example.com': {
        'password': 'john_pass123',
        'name': 'John Administrator',
        'communities': ['Townsville', 'Villageville']
    },
    'alice.admin@example.com': {
        'password': 'alice_pass456',
        'name': 'Alice Administrator',
        'communities': ['Hamletville', 'Cityburg']
    },
    'bob.admin@example.com': {
        'password': 'bob_pass789',
        'name': 'Bob Administrator',
        'communities': ['New York', 'Los Angeles']
    },
    'susan.admin@example.com': {
        'password': 'susan_pass123',
        'name': 'Susan Administrator',
        'communities': ['Chicago', 'Houston']
    },
    'david.admin@example.com': {
        'password': 'david_pass456',
        'name': 'David Administrator',
        'communities': ['Phoenix', 'Philadelphia']
    },
    'emily.admin@example.com': {
        'password': 'emily_pass789',
        'name': 'Emily Administrator',
        'communities': ['San Antonio', 'San Diego']
    },
    'michael.admin@example.com': {
        'password': 'michael_pass123',
        'name': 'Michael Administrator',
        'communities': ['Dallas', 'San Jose']
    },
    'jessica.admin@example.com': {
        'password': 'jessica_pass456',
        'name': 'Jessica Administrator',
        'communities': ['Austin', 'Jacksonville']
    },
    'ryan.admin@example.com': {
        'password': 'ryan_pass789',
        'name': 'Ryan Administrator',
        'communities': ['Fort Worth', 'Columbus']
    },
    'lisa.admin@example.com': {
        'password': 'lisa_pass123',
        'name': 'Lisa Administrator',
        'communities': ['Charlotte', 'San Francisco']
    },
}

events = {

    "Trash Pickup": {
        "Community": "Columbia University",
        "Address": "116th and Broadway",
        "members": ["JeffBezos", "SigmundFreud", "BarackObama"],
        "tasks": {"Setup": 0 , "Registration":1, "Cleanup":0}
    },
    "Food Drive": {
        "Community": "Columbia University",
        "Address": "116th and Broadway",
        "members": ["MalcolmX", "Oprah", "ElonMusk"],
        "tasks": {"Catering": 0, "Security":1, "Entertainment":0}
    },
    "Event3": {
        "Community": "New York University",
        "Address": "Manhattan",
        "members": ["Grace", "Heidi", "Ivan"],
        "tasks": ["Invitations", "Decorations", "Photography"]
    }
}
