import datetime
import uuid

from datetime import timezone


class DomainObject:

    def __init__(self):
        self.id = 123
        self.uuid = uuid.uuid4()
        self.date_created = datetime.datetime.now(timezone.utc)
        self.date_modified = datetime.datetime.now(timezone.utc)
