from flask import Blueprint
from Controllers.balanceController import BalanceController

balance_blueprint = Blueprint('balance', __name__)

# Ruta para consultar el balance de un usuario
balance_blueprint.route('/balance', methods=['GET'])(BalanceController.get_balance)
