from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=32, unique=False)
    email = models.EmailField()

    class Meta:
        db_table = "user"
        verbose_name = '客户'
        verbose_name_plural = verbose_name
