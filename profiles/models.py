from django.db import models
from django.db.models.signals import post_save
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

    class Meta:
        """Meta class that will return  
        our Profile instances in reverse order,  so the most recently created is first.  
        The 'created_at' relate to created_at field name. And the minus sign at  
        the beginning of the string, indicates  that we want our results in reverse.
        """
        ordering = ['-created_at']

        def __str__(self):
            return f"{self.owner} 's profile"

def create_profile(sender, instance, created, **kwargs):
    # Because we are  
    # passing this function to the post_save.connect  method, it requires the following arguments:  
    # the sender model, its instance, created  - which is a boolean value of whether or  
    # not the instance has just been created, and  kwargs. Inside the create_profile function,  
    # if created is True, we’ll create a profile  whose owner is going to be that user.
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)