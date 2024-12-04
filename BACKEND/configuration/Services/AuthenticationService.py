from werkzeug.security import generate_password_hash, check_password_hash
from Models.userModel import User
from app import db  # Si 'db' está definido en app.py

class AuthService:
    @staticmethod
    def register(username, password):
        # Verificar si el usuario ya existe
        if User.query.filter_by(username=username).first():
            raise Exception("El nombre de usuario ya existe")
        
        # Crear un nuevo usuario
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None
