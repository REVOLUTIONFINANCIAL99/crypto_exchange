from django.db import models
from users.models import CustomUser

class Transfer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="transfers")
    receiver_wallet = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    asset_type = models.CharField(max_length=50)  # Por ejemplo: ETH, BTC, etc.
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transferencia de {self.amount} {self.asset_type} de {self.user} a {self.receiver_wallet}"

from django.db import models
from django.conf import settings

class Wallet(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wallet'
    )
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Wallet of {self.user.username}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.save()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.save()
            return True
        return False


class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAW', 'Withdraw'),
        ('TRANSFER', 'Transfer'),
        ('PURCHASE', 'Purchase'),
    )
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} in {self.wallet}"
