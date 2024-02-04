
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

COMMUNITY_INFO = [
    ('Townsville', 'CA'),
    ('Villageville', 'NY'),
    ('Hamletville', 'TX'),
    ('Cityburg', 'FL'),
    ('New York', 'NY'),
    ('Los Angeles', 'CA'),
    ('Chicago', 'IL'),
    ('Houston', 'TX'),
    ('Phoenix', 'AZ'),
    ('Philadelphia', 'PA'),
    ('San Antonio', 'TX'),
    ('San Diego', 'CA'),
    ('Dallas', 'TX'),
    ('San Jose', 'CA'),
    ('Austin', 'TX'),
    ('Jacksonville', 'FL'),
    ('Fort Worth', 'TX'),
    ('Columbus', 'OH'),
    ('Charlotte', 'NC'),
    ('San Francisco', 'CA'),
    ('Indianapolis', 'IN'),
    ('Seattle', 'WA'),
    ('Denver', 'CO'),
    ('Washington', 'DC'),
]

VALID_STATES = {'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 
                'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 
                'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 
                'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'}

ADMIN_INFO = {
    
    'admin1@example.com': {
        'password': 'admin1_pass',
        'name': 'Admin One',
        'communities': [('Washington' , 'DC'), ('Columbus' , 'OH')]
    },
    'admin2@example.com': {
        'password': 'admin2_pass',
        'name': 'Pres. Shafik',
        'communities': [('Dallas', 'TX'), ('Columbus' , 'OH')]
    },
    'john.admin@example.com': {
        'password': 'john_pass123',
        'name': 'John Administrator',
        'communities': [('Townsville', 'CA') , ('Columbus' , 'OH')]
    },
    'alice.admin@example.com': {
        'password': 'alice_pass456',
        'name': 'Alice Administrator',
        'communities': [('Hamletville', 'TX') ,('Columbus' , 'OH')]
    },
    'bob.admin@example.com': {
        'password': 'bob_pass789',
        'name': 'Bob Administrator',
        'communities': [('New York', 'NY'), ('Los Angeles','CA')]
    },
    'susan.admin@example.com': {
        'password': 'susan_pass123',
        'name': 'Susan Administrator',
        'communities': [('Chicago','IL') , ('Houston', 'TX')]
    },
    'david.admin@example.com': {
        'password': 'david_pass456',
        'name': 'David Administrator',
        'communities': [('Phoenix','AZ'), ('Philadelphia','PA')]
    },
    'emily.admin@example.com': {
        'password': 'emily_pass789',
        'name': 'Emily Administrator',
        'communities': [('San Antonio','TX'),('San Diego','CA')]
    },
    'michael.admin@example.com': {
        'password': 'michael_pass123',
        'name': 'Michael Administrator',
        'communities': [('Dallas','TX'), ('San Jose','CA')]
    },
    'jessica.admin@example.com': {
        'password': 'jessica_pass456',
        'name': 'Jessica Administrator',
        'communities': [('Austin','TX'),('Jacksonville','FL')]
    },
    'ryan.admin@example.com': {
        'password': 'ryan_pass789',
        'name': 'Ryan Administrator',
        'communities': [('Fort Worth','TX'),('Columbus','OH')]
    },
    'lisa.admin@example.com': {
        'password': 'lisa_pass123',
        'name': 'Lisa Administrator',
        'communities': [('Charlotte','NC'), ('San Francisco','CA')]
    },
}

EVENTS = {

    "Trash Pickup": {
        "Status" : False,
        "Creator" : 'ryan.admin@example.com',
        "Community": ('Columbus','OH'),
        "Address": "116th and Broadway",
        "members": ["JeffBezos", "SigmundFreud", "BarackObama"],
        "tasks": {"Setup": False , "Registration":True, "Cleanup":False}
    },
    "Food Drive": {
        "Status" : True,
        "Creator" : 'alice.admin@example.com',
        "Community": ('Dallas','TX'),
        "Address": "116th and Broadway",
        "members": ["MalcolmX", "Oprah", "ElonMusk"],
        "tasks": {"Catering": True, "Security":True, "Entertainment":True}
    },
    "Side Walk Sweeping": {
        "Status" : False,
        'Creator' : 'john.admin@example.com',
        "Community": ('Columbus','OH'),
        "Address": "Manhattan",
        "members": ["Grace", "Heidi", "Ivan"],
        "tasks": {"Invitations": False, "Decorations": False, "Photography": True}
    }
}
