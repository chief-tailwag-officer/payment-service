from uuid import UUID

from src import User, db


def change_balance(user_id: UUID, amount: float):
    user = User.query.filter_by(uuid=user_id).first()

    if user:
        user.balance = user.balance + amount
        db.session.add(user)
        db.session.commit()
        return user
