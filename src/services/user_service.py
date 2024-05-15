from flask import Request

from src import User, db, app
from src.api.dto.user_response import UserResponse
from src.services import transfer_service


def create_user(request: Request):
    if request.is_json:
        user = User(full_name=request.json.get("fullname"), balance=0)

        db.session.add(user)
        db.session.commit()

        app.logger.info(f'Create new user: {user.uuid}')
        return UserResponse(user).to_json(), 201
    else:
        return {"error": "Only application/json content type is supported"}


# This is for testing purposes
def add_promotion(request: Request, user_id):
    if request.is_json:
        amount = request.json.get("amount")
        user = transfer_service.change_balance(user_id, amount)

        app.logger.info(f'Added promotional money: {user.uuid}')
        return UserResponse(user).to_json(), 201
    else:
        return {"error": "Only application/json content type is supported"}


def get_user(id):
    user = User.query.filter_by(uuid=id).first()

    if user:
        return UserResponse(user).to_json(), 201
    else:
        return {"error": f'User with id \'{id}\' not fount'}, 404
