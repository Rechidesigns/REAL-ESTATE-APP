from django.db import models

# Create your models here.


class Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField(default=False)

    def __str__(self):
        return self.title
 
class Lands(models.Model):
    title = models.CharField(max_length=150)
    c_o_t = models.BooleanField()
    location = models.Charfield(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(default=False)
    plots = models.IntegerField()
    
    def __str__(self):
        return self.title
