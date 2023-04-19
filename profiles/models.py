from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_lenght=255, blank=True)
    content = models.TextField(blank=True)
#   to store images in our database, we need  a different kind of model field called an  
#   ImageField, for this field we need  to define parameters for upload_to,  
#   the value is a folder name called images with a slash sign.
    image = models.ImageField(
        upload_to='images/', default='../default_profile_de0exc' #this default is the file name from Cloudinary
    )

   