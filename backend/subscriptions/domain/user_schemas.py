class UserBase():
    username: str
    email: str
    def __init__(self, attributes):
        self.username = attributes[0]
        self.email = attributes[1]

class UserCreate(UserBase):
    password: str

    def __init__(self, attributes):
        self.username = attributes[0]
        self.email = attributes[1]
        self.password = attributes[2]

class User(UserBase):
    id: int

    def __init__(self, attributes):
        self.id = attributes[0]
        self.username = attributes[1]
        self.email = attributes[2]

class UserUpdate():
    username: str = None
    email: str = None
    password: str = None

    def __init__(self, attributes):
        self.username = attributes[0]
        self.email = attributes[1]
        self.password = attributes[2]

class UserInDB(UserBase):
    password: str
    created_at: str
    
    def __init__(self, attributes):
        self.id = attributes[0]
        self.username = attributes[1]
        self.email = attributes[2]
        self.password = attributes[3]
        self.created_at = attributes[4]

    
