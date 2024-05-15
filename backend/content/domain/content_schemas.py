class ContentBase():
    title: str
    description: str
    release_date: str
    type: str
    def __init__(self, attributes):
        self.title = attributes[0]
        self.description = attributes[1]
        self.release_date = attributes[2]
        self.type = attributes[3]

class ContentCreate(ContentBase):
    account_id: int

    def __init__(self, attributes):
        self.title = attributes[0]
        self.description = attributes[1]
        self.release_date = attributes[2]
        self.type = attributes[3]
        self.account_id = attributes[4]

class Content(ContentBase):
    id: int
    account_id: int

    def __init__(self, attributes):
        self.id = attributes[0]
        self.account_id = attributes[1]
        self.title = attributes[2]
        self.description = attributes[3]
        self.release_date = attributes[4]
        self.type = attributes[5]

class ContentUpdate():
    title: str
    description: str
    release_date: str
    type: str

    def __init__(self, attributes):
        self.title = attributes[0]
        self.description = attributes[1]
        self.release_date = attributes[2]
        self.type = attributes[3]

class ContentInDB(ContentBase):
    id: int
    account_id: int
    created_at: str
    
    def __init__(self, attributes):
        self.id = attributes[0]
        self.account_id = attributes[1]
        self.title = attributes[2]
        self.description = attributes[3]
        self.release_date = attributes[4]
        self.type = attributes[5]
        self.created_at = attributes[6]