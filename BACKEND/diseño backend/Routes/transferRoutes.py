from flask import Blueprint
from Controllers.transferController import TransferController

transfer_blueprint = Blueprint('transfer', __name__)

# Ruta para realizar una transferencia de tokens
transfer_blueprint.route('/transfer', methods=['POST'])(TransferController.transfer_tokens)
