from flask import Flask
from config.settings import Config
from Routes.transferRoutes import transfer_blueprint
from Routes.balanceRoutes import balance_blueprint
from Routes.SingRoute import user_blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)

# Registrar las rutas
app.register_blueprint(transfer_blueprint, url_prefix='/transfer')
app.register_blueprint(balance_blueprint, url_prefix='/balance')
app.register_blueprint(user_blueprint, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
