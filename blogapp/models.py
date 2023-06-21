from django.db import models

class SignUp(models.Model):
    user_email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

class WriteToUs(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default='Aliyar')
    artile = models.TextField()
# Create your models here.
