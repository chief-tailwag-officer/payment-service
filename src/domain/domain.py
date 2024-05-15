from datetime import datetime

import uuid

from src import db, Base


# Force common structure to the tables
class Domain(Base, db.Model):
    __abstract__ = True

    id = db.Column(db.Integer(), primary_key=True, unique=True)
    uuid = db.Column(db.UUID(as_uuid=True), default=uuid.uuid4())
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime, default=datetime.utcnow)
