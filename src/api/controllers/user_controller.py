from flask import Blueprint, request

from src.api.dto.user_response import UserResponse
from src.domain.user import User

users = Blueprint("users", __name__)


# TODO:
# Implement endpoints to create and retrieve users.
# Each user should have a unique ID, a name, and a balance

@users.route('', methods=["POST"])
def create_user():
    if request.is_json:
        user = User(request.json.get("fullname"), 0)

        return UserResponse(user).to_json(), 201
    else:
        return {"error": "Only application/json content type is supported"}


@users.route('/<uuid:id>', methods=["GET"])
def get_user(id):
    return "Not Implemented"
