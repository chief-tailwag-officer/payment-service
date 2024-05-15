from flask import Blueprint, request

from src.services import user_service

users = Blueprint("users", __name__)


@users.route('', methods=["POST"])
def create_user():
    return user_service.create_user(request)


@users.route('/<uuid:id>', methods=["GET"])
def get_user(id):
    return user_service.get_user(id)
