from django.db import models

# Create your models here.
class Service (models.Model):
    stitre = models.CharField(max_length=50)
    sdescription = models.CharField(max_length=200)

    def __str__(self):
        return self.stitre

class Client(models.Model):
    cnom = models.CharField(max_length=50)
    cemail = models.EmailField(max_length=50)
    cquartier = models.CharField(max_length=100)
    
    cmessage = models.TextField()

    def __str__(self):
        return self.cemail

