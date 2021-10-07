from django.db import models


class Player(models.Model):
    id_player= models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description= models.CharField(max_length=150)
    phone= models.CharField(max_length=10)

    def __str__(self):
        return self.name



