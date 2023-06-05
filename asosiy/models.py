from django.db import models
from django.contrib.auth.models import User

class Muallif(models.Model):
    ism = models.CharField(max_length=70)
    yosh = models.SmallIntegerField()
    kasbi = models.CharField(max_length=80)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.ism

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=80)
    mavzu = models.CharField(max_length=80)
    matn = models.TextField()
    muallif = models.ForeignKey(Muallif , on_delete=models.CASCADE)
    def __str__(self):
        return self.sarlavha




