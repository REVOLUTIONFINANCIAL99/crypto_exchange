class Config:
    # Configuración de la base de datos (si es necesario)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración de Ganache (Blockchain)
    WEB3_PROVIDER_URL = "http://127.0.0.1:8545"  # URL de Ganache
    WEB3_INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
    CONTRACT_ADDRESS = "0xYourContractAddressHere"
    
    # Otros parámetros de configuración
    SECRET_KEY = 'your_secret_key'
