from flask import Request

from src import User, db, app
from src.api.api_exception import ApiException
from src.api.dto.user import UserResponse, UserRequest


def create_user(request: UserRequest):
    user = User(request.full_name, 0)

    db.session.add(user)
    db.session.commit()

    app.logger.info(f'Create new user: {user.uuid}')
    return UserResponse(user).to_json(), 201


# This is for testing purposes
def add_promotion(request: Request, user_id):
    if request.is_json:
        amount = request.json.get("amount")
        user = User.query.filter_by(uuid=user_id).first()

        user.balance = user.balance + amount
        db.session.add(user)
        db.session.commit()

        app.logger.info(f'Added promotional money: {user.uuid}')
        return UserResponse(user).to_json(), 201
    else:
        return {"error": "Only application/json content type is supported"}


def get_user(user_id):
    user = fetch_user(user_id)
    return UserResponse(user).to_json(), 201


def fetch_user(user_id):
    user = User.query.filter_by(uuid=user_id).first()

    if user:
        return user
    else:
        raise ApiException("User not found!", 404)
