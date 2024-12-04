from django.db import models
from users.models import CustomUser

class SmartContract(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="contracts")
    contract_name = models.CharField(max_length=200)
    contract_address = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contract_name} ({self.contract_address})"
