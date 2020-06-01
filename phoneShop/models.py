from django.db import models
"""I learned how to write the code bellow through Code Institute and it is the only way I know how to do it. 
Source: https://codeinstitute.net/"""


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name
