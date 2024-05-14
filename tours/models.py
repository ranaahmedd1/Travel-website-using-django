from django.db import models
from django.contrib.postgres.fields import ArrayField

# from django.forms import ImageField
# import PIL for image resizing
from PIL import Image
# Create your models here.


class Images(models.Model):
    image = models.TextField()
    def __str__(self):
        return self.image

class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=40,null=False)
    country=models.CharField(max_length=40,null=False)
    attractions=models.TextField(default=None,null=False,verbose_name='attractions of the city ')
    cityImages = models.ForeignKey( Images, on_delete=models.CASCADE, null=True )

    def __str__(self):
        return self.name
    

    # images=models.ImageField(upload_to='static/images',null=False,default=None)
    # oneImage=models.TextField()
    # images=ArrayField(models.TextField(),size=4)
