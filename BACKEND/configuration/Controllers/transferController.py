from Services.web3Service import Web3Service
from flask import request, jsonify

class TransferController:
    @staticmethod
    def transfer_tokens():
        sender_address = request.json.get('sender_address')
        receiver_address = request.json.get('receiver_address')
        amount = request.json.get('amount')

        # Verificar si las direcciones son válidas
        if not Web3Service.is_valid_address(sender_address) or not Web3Service.is_valid_address(receiver_address):
            return jsonify({"error": "Dirección inválida"}), 400
        
        # Realizar la transferencia
        try:
            web3_service = Web3Service()
            tx_hash = web3_service.transfer(sender_address, receiver_address, amount)
            return jsonify({"transaction_hash": tx_hash}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
