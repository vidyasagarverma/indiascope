from django.db import models

class Form(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    message=models.CharField(max_length=2000)


def __str__(self):
    return f"{self.name} {self.email}"