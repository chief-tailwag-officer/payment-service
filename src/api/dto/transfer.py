from flask import Request

from src import Transfer, ApiException
from src.api.dto.response import Response


class TransferRequest:
    def __init__(self, request: Request):
        if request.is_json:
            self.sender_id = request.json.get("senderId")
            self.recipient_id = request.json.get("recipientId")
            self.amount = request.json.get("amount")
        else:
            raise ApiException("Unable to parse request.", 403)


class WithdrawRequest:
    def __init__(self, request: Request):
        if request.is_json:
            self.user_id = request.json.get("userId")
            self.amount = request.json.get("amount")
        else:
            raise ApiException("Unable to parse request.", 403)


class TransferResponse(Response):
    def __init__(self, transfer: Transfer):
        super().__init__(transfer)

        self.sender_id = transfer.sender_id
        self.recipient_id = transfer.recipient_id
        self.amount = transfer.amount

    def to_json(self):
        return {
            "id": self.uuid,
            "dateCreated": self.date_created,
            "dateModified": self.date_modified,
            "senderId": self.sender_id,
            "recipientId": self.recipient_id,
            "amount": self.amount
        }
