from django.db import models


class Order(models.Model):

    product = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    count = models.IntegerField()
    price = models.FloatField()

    def __str(self) -> str:
        return str(self.title)
