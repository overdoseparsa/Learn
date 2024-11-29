from typing import Any
from django.db import models
from django.contrib.auth.models import User

class Loan(
    models.Model
):
    author = models.ForeignKey(
        User , on_delete=models.CASCADE
    )
    price = models.PositiveBigIntegerField()

    datetime_get = models.DateTimeField(

    )
    datetime_push = models.DateTimeField(
        blank= False , null=True
    )
    is_settle = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.author.username} -> {self.price}'
    


