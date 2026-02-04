"""
Card
"""
from django.db import models

# Create your models here.

class Card(models.Model):
    """
    Card model

    Qatorlar:

    --karta raqam
    --amal qilish muddati
    --telefon raqam
    -- statut

    """
    S_ACTIVE="active"
    S_INACTIVE="inactive"
    S_EXPIRED="expired"

    STATUS_CHOICES = [
        (S_ACTIVE,"Active"),
        (S_INACTIVE,"Inactive"),
        (S_EXPIRED,"Expired"),
    ]
    card_number = models.CharField(max_length=16, unique=True)
    expire = models.DateTimeField()
    phone = models.CharField(max_length=13 ,unique=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=S_ACTIVE
    )
    def __str__(self):
        return str(self.card_number)
