from flask import Blueprint
from Controllers.userController import UserController

user_blueprint = Blueprint('user', __name__)

# Ruta para crear un nuevo usuario
user_blueprint.route('/register', methods=['POST'])(UserController.create_user)
