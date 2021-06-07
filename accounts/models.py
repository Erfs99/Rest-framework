from django.db import models

# Create your models here.
class Account(models.Model):
    name=models.CharField(max_length=150,blank=True,null=True)
    username=models.CharField(max_length=150,blank=False,null=False)
    calls=models.IntegerField(default=0)
    def __str__(self):
        return self.username