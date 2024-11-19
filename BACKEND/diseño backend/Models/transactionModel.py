from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_address = db.Column(db.String(42), nullable=False)
    receiver_address = db.Column(db.String(42), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_hash = db.Column(db.String(66), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Transaction {self.transaction_hash}>'
