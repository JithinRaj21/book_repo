from django.db import models


# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='media',default='')

    def __str__(self):
        return self.name
