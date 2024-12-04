import re

# Validación para direcciones de Ethereum
def validate_address(address):
    pattern = r"^0x[a-fA-F0-9]{40}$"
    return re.match(pattern, address) is not None

# Formateo de tokens (por ejemplo, convertir de wei a ether)
def format_token_amount(amount, decimals=18):
    return amount / (10 ** decimals)
