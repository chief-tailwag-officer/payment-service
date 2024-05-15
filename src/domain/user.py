from src.domain.domain_object import DomainObject


class User(DomainObject):

    def __init__(self, full_name: str, balance: float):
        super().__init__()

        self.full_name = full_name
        self.balance = balance
