import uuid

from src import db
from src.domain.domain import Domain


class Transfer(Domain):
    __tablename__ = "transfer"

    sender_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('user.uuid'))
    recipient_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('user.uuid'))
    amount = db.Column(db.Float)

    def __init__(self, sender_id: uuid, recipient_id: uuid, amount: float):
        super().__init__()

        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.amount = amount
