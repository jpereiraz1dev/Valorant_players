from django.db import models

class Player(models.Model):

    roles = [
        ("DUELISTA","Duelista"),
        ("SENTINELA","Sentinela"),
        ("CONTROLADOR","Controlador"),
        ("INICIADOR","Iniciador"),
        ("FLEX","Flex"),
    ]

    nickname = models.CharField(max_length=30,blank=False,null=False)
    team = models.CharField(max_length=30,null=True,blank=False)
    role = models.CharField(choices=roles,null=False,blank=False)
    foto = models.CharField(max_length=30,blank=False,null=False)

