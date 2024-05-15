from flask import Blueprint, request

from src.api.dto.transfer import TransferRequest, WithdrawRequest
from src.services import transfer_service

transfers = Blueprint("transfers", __name__)


@transfers.route('', methods=["POST"])
def transfer():
    return transfer_service.transfer_funds(TransferRequest(request))


@transfers.route('/withdraw', methods=["POST"])
def withdraw():
    return transfer_service.withdraw(WithdrawRequest(request))
