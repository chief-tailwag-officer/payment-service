from src import User, db, Transfer, app
from src.api.api_exception import ApiException
from src.api.dto.transfer import TransferResponse, TransferRequest, \
    WithdrawRequest
from src.services import user_service


def transfer_funds(request: TransferRequest):
    sender = user_service.fetch_user(request.sender_id)
    recipient = user_service.fetch_user(request.recipient_id)

    validate_amount(request.amount, sender)

    sender.balance = sender.balance - request.amount
    recipient.balance = recipient.balance + request.amount

    transfer = Transfer(sender.uuid, recipient.uuid, request.amount)
    db.session.add(transfer)

    db.session.commit()

    app.logger.info(
        f'Create transfer: {sender.uuid} -> {request.amount} -> {recipient.uuid}')
    return TransferResponse(transfer).to_json(), 201


def withdraw(request: WithdrawRequest):
    user = user_service.fetch_user(request.user_id)

    validate_amount(request.amount, user)

    user.balance = user.balance - request.amount

    transfer = Transfer(user.uuid, user.uuid, request.amount)
    db.session.add(transfer)

    db.session.commit()

    app.logger.info(
        f'Withdraw money: {user.uuid} -> {request.amount}')
    return TransferResponse(transfer).to_json(), 201


def validate_amount(amount: float, sender: User):
    if amount < 1:
        raise ApiException("Amount has to be greater than zero!", 403)
    if sender.balance < amount:
        raise ApiException("Insufficient funds", 403)
