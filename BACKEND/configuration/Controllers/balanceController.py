from Services.web3Service import Web3Service
from flask import request, jsonify

class BalanceController:
    @staticmethod
    def get_balance():
        address = request.args.get('address')
        
        # Verificar si la dirección es válida
        if not Web3Service.is_valid_address(address):
            return jsonify({"error": "Dirección inválida"}), 400

        try:
            web3_service = Web3Service()
            balance = web3_service.get_balance(address)
            return jsonify({"balance": balance}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
