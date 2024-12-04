from flask import request, jsonify
from Services.AuthenticationService import AuthService
from Models.userModel import User

class UserController:
    @staticmethod
    def create_user():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        # Validación de los datos de entrada
        if not username or not password:
            return jsonify({"error": "Usuario y contraseña son requeridos"}), 400
        
        # Crear el usuario
        try:
            auth_service = AuthService()
            auth_service.register(username, password)
            return jsonify({"message": "Usuario creado exitosamente"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
