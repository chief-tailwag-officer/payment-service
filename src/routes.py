from flask import Blueprint, jsonify

from src import ApiException, app
from src.api.controllers.transfer_controller import transfers
from src.api.controllers.user_controller import users

# Main API blueprint
api = Blueprint('api', __name__)

# Register different blueprints for controllers
api.register_blueprint(users, url_prefix="/users")
api.register_blueprint(transfers, url_prefix="/transfers")


# Adding common exception handler
@app.errorhandler(ApiException)
def handle_api_exception(error):
    return jsonify(error.to_json()), error.status_code
