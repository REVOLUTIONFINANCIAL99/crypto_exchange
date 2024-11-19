from web3 import Web3

# Conectar a Ganache
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))  # La URL predeterminada de Ganache

# Verificar la conexión
if w3.isConnected():
    print("Conectado a Ganache")
else:
    print("No se pudo conectar a Ganache")
