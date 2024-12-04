import unittest
from BACKEND import app  # Si app.py está en el directorio 'backend'


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_transfer_tokens(self):
        response = self.app.post('/transfer/transfer', json={
            'sender_address': '0xSenderAddress',
            'receiver_address': '0xReceiverAddress',
            'amount': 10
        })
        self.assertEqual(response.status_code, 200)

    def test_get_balance(self):
        response = self.app.get('/balance/balance?address=0xSomeAddress')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
