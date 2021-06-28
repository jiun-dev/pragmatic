from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    # null false -> 무조건 있어야하는 부분
    text = models.CharField(max_length=255, null=False)