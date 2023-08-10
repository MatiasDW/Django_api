from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=200)
    contract_date = models.DateField()
    urls = models.URLField()
    contract_admin = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
