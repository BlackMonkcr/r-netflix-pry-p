class SubscriptionBase():
    plan: str
    start_date: str
    end_date: str
    status: str

    def __init__(self, attributes):
        self.plan = attributes[0]
        self.start_date = attributes[1]
        self.end_date = attributes[2]
        self.status = attributes[3]


class SubscriptionCreate(SubscriptionBase):
    account_id: int

    def __init__(self, attributes):
        self.account_id = attributes[0]
        self.plan = attributes[1]
        self.start_date = attributes[2]
        self.end_date = attributes[3]
        self.status = attributes[4]

class Subscription(SubscriptionBase):
    id: int
    account_id: int

    def __init__(self, attributes):
        self.id = attributes[0]
        self.account_id = attributes[1]
        self.plan = attributes[2]
        self.start_date = attributes[3]
        self.end_date = attributes[4]
        self.status = attributes[5]