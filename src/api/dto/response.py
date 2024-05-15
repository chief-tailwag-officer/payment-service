from src.domain.domain_object import DomainObject


class Response:
    def __init__(self, domain: DomainObject):
        self.uuid = domain.uuid
        self.date_created = domain.date_created.isoformat()
        self.date_modified = domain.date_modified.isoformat()

    def to_json(self):
        return {
            "id": self.uuid,
            "dateCreated": self.date_created,
            "dateModified": self.date_modified
        }
