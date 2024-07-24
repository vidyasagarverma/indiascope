from django.db import models

# Create your models here.
class Form(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=200)
    message=models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"