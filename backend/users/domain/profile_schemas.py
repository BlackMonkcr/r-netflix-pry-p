class ProfileBase():
    nombre: str
    def __init__(self, attributes):
        self.nombre = attributes[0]

class ProfileCreate(ProfileBase):
    account_id: int

    def __init__(self, attributes):
        self.nombre = attributes[0]
        self.account_id = attributes[1]

class Profile(ProfileBase):
    id: int
    account_id: int

    def __init__(self, attributes):
        self.id = attributes[0]
        self.account_id = attributes[1]
        self.nombre = attributes[2]

class ProfileUpdate():
    nombre: str

    def __init__(self, attributes):
        self.nombre = attributes[0]

class ProfileInDB(ProfileBase):
    id: int
    account_id: int
    fecha_creacion: str
    
    def __init__(self, attributes):
        self.id = attributes[0]
        self.account_id = attributes[1]
        self.nombre = attributes[2]
        self.fecha_creacion = attributes[3]
