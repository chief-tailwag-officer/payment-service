from flask import Blueprint, request

from src.services import user_service

users = Blueprint("users", __name__)


@users.route('', methods=["POST"])
def create_user():
    return user_service.create_user(request)


@users.route('/<uuid:user_id>', methods=["GET"])
def get_user(user_id):
    return user_service.get_user(user_id)


@users.route('/<uuid:user_id>/add-promo', methods=["POST"])
def add_promotion(user_id):
    return user_service.add_promotion(request, user_id)
