from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Portal(models.Model):
    author = models.OneToOneField(
        User , on_delete=models.CASCADE , related_name='ProtalAurhor'
    )
    tikets_buy = models.ForeignKey(
        'Titkets' , on_delete=models.CASCADE , related_name='ProtalAurhor'
    )
    def __str__(self) -> str:
        return f'{self.author.username}'

class Titkets(models.Model):
    title = models.CharField(
        max_length=180 
    )
    price = models.PositiveBigIntegerField()

    date = models.DateTimeField(
        default=now 
    )

    def __str__(self) -> str:
        return f'{self.title} - > {self.price}'