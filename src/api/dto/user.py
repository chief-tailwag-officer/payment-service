from flask import Request

from src import ApiException
from src.api.dto.response import Response
from src.domain.user import User


class UserRequest:
    def __init__(self, request: Request):
        if request.is_json:
            self.full_name = request.json.get("fullname")
        else:
            raise ApiException("Unable to parse request.", 403)


class UserResponse(Response):
    def __init__(self, user: User):
        super().__init__(user)

        self.full_name = user.full_name
        self.balance = user.balance

    def to_json(self):
        return {
            "id": self.uuid,
            "dateCreated": self.date_created,
            "dateModified": self.date_modified,
            "name": self.full_name,
            "balance": self.balance
        }
