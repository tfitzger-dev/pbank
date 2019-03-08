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
