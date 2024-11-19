from web3 import Web3
from config.settings import Config

class Web3Service:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(Config.WEB3_PROVIDER_URL))
        self.contract_address = Config.CONTRACT_ADDRESS
        # Aquí puedes agregar la ABI de tu contrato
        self.contract_abi = []

    @staticmethod
    def is_valid_address(address):
        return Web3.isAddress(address)

    def transfer(self, sender_address, receiver_address, amount):
        # Aquí se agregaría la lógica para interactuar con el contrato inteligente
        # Por ejemplo:
        contract = self.web3.eth.contract(address=self.contract_address, abi=self.contract_abi)
        # Suponiendo que la función transfer se llama 'transferTokens' en el contrato
        transaction = contract.functions.transferTokens(receiver_address, amount).buildTransaction({
            'from': sender_address,
            'gas': 2000000,
            'gasPrice': self.web3.toWei('10', 'gwei'),
            'nonce': self.web3.eth.getTransactionCount(sender_address),
        })
        # Firmar y enviar la transacción
        signed_txn = self.web3.eth.account.signTransaction(transaction, private_key="YourPrivateKey")
        tx_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return tx_hash.hex()
