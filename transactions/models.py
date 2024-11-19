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
