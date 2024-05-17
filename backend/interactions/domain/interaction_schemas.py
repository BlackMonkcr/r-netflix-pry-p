class InteractionBase():
    account_id: int
    content_id: int
    interaction_type: str


    def __init__(self, attributes):
        self.account_id = attributes[0]
        self.content_id = attributes[1]
        self.interaction_type = attributes[2]


class InteractionCreate(InteractionBase):
    def __init__(self, attributes):
        self.account_id = attributes[0]
        self.content_id = attributes[1]
        self.interaction_type = attributes[2]

class Interaction(InteractionBase):
    id: int
    def __init__(self, attributes):
        self.id = attributes[0]
        self.account_id = attributes[1]
        self.content_id = attributes[2]
        self.interaction_type = attributes[3]