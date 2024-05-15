from src import db
from src.domain.domain import Domain


class User(Domain):
    __tablename__ = "user"

    full_name = db.Column(db.String(255))
    balance = db.Column(db.Float)

    def __init__(self, full_name: str, balance: float):
        super().__init__()

        self.full_name = full_name
        self.balance = balance
