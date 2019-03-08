from django.db import models


class Bill(models.Model):
    class Meta:
        ordering = ('due_day',)
        
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    name = models.TextField()
    key = models.TextField()
    paid = models.BooleanField()
    due_day = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='bills', on_delete=models.CASCADE)


class Institution(models.Model):
    class Meta:
        ordering = ('name',)

    owner = models.ForeignKey('auth.User', related_name='institutions', on_delete=models.CASCADE)
    id = models.TextField(primary_key=True)
    name = models.TextField()


class BankAccount(models.Model):
    class Meta:
        ordering =('institution', 'short_name')

    owner = models.ForeignKey('auth.User', related_name='accounts', on_delete=models.CASCADE)
    institution = models.ForeignKey('Institution', related_name='accounts', on_delete=models.CASCADE)
    id = models.TextField(primary_key=True)
    short_name = models.TextField()
    full_name = models.TextField()
    type = models.TextField()
    balance = models.DecimalField(max_digits=7, decimal_places=2)


class Transaction(models.Model):
    class Meta:
        ordering = ('date',)

    account = models.ForeignKey('BankAccount', related_name='transactions', on_delete=models.CASCADE)
    name = models.TextField()
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField()

