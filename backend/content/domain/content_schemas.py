class ContentBase():
    title: str
    description: str
    release_date: str
    type: str
    url_content: str
    url_cover: str
    def __init__(self, attributes):
        self.title = attributes[0]
        self.description = attributes[1]
        self.release_date = attributes[2]
        self.type = attributes[3]
        self.url_content = attributes[4]
        self.url_cover = attributes[5]

class ContentCreate(ContentBase):
    pass

class Content(ContentBase):
    content_id: int

    def __init__(self, attributes):
        self.title = attributes[0]
        self.description = attributes[1]
        self.release_date = attributes[2]
        self.type = attributes[3]
        self.url_content = attributes[4]
        self.url_cover = attributes[5]
        self.content_id = attributes[6]


class ContentUpdate():
    title: str
    description: str
    release_date: str
    type: str
    url_content: str
    url_cover: str

    def __init__(self, attributes):
        self.title = attributes[0]
        self.description = attributes[1]
        self.release_date = attributes[2]
        self.type = attributes[3]
        self.url_content = attributes[4]
        self.url_cover = attributes[5]

class ContentInDB(ContentBase):
    id: int
    created_at: str
    
    def __init__(self, attributes):
        self.id = attributes[0]
        self.title = attributes[2]
        self.description = attributes[3]
        self.release_date = attributes[4]
        self.type = attributes[5]
        self.url_content = attributes[6]
        self.url_cover = attributes[7]
        self.created_at = attributes[8]