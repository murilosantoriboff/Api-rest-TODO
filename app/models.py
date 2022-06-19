from django.db import models

class Todo(models.Model):
    nome = models.CharField(max_length=120)
    feito = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)
