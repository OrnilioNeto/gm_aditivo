from django.db import models
from datetime import datetime


# Create your models here.
class produto(models.Model):
    nome = models.TextField(max_length=15)
    assunto= models.TextField(max_length=20)    
    mensagem = models.TextField(max_length=40)
   