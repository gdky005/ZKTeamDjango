from django.db import models


# Create your models here.

class WXMoneyInfo(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    name = models.TextField()
    money = models.TextField(default='0.00')
    # money = models.DecimalField(max_digits=5, decimal_places=2)


class WXMoneyItemInfo(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    name = models.TextField()
    time = models.DateTimeField()
    # values = models.DecimalField(max_digits=5, decimal_places=2)
    money = models.TextField(default='0.00')
    spendState = models.BooleanField()


class WXMoneyPZ(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    name = models.TextField()

    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

    startMoney = models.IntegerField()
    endMoney = models.IntegerField()

    spendState = models.BooleanField()
