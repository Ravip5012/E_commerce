from django.db import models

from django.contrib.auth.models import User



class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    details= models.CharField(max_length=500)
    # user_image= models.ImageField(upload_to="profile_picture/")