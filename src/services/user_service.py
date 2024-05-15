from flask import Request

from src import User, db, app
from src.api.dto.user_response import UserResponse


# TODO:
# Implement endpoints to create and retrieve users.
# Each user should have a unique ID, a name, and a balance
def create_user(request: Request):
    if request.is_json:
        user = User(full_name=request.json.get("fullname"), balance=0)

        db.session.add(user)
        db.session.commit()

        app.logger.info(f'Create new user: {user.uuid}')
        return UserResponse(user).to_json(), 201
    else:
        return {"error": "Only application/json content type is supported"}


def get_user(id):
    user = User.query.filter_by(uuid=id).first()

    if user:
        return UserResponse(user).to_json(), 201
    else:
        return {"error": f'User with id \'{id}\' not fount'}, 404
