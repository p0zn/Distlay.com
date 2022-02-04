from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    first_name = models.CharField(max_length=50,verbose_name="First Name")
    last_name = models.CharField(max_length=50,verbose_name="Last Name")
    username = models.CharField(max_length=50,verbose_name="Username")
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(max_length=50,verbose_name="Password")
    confirm = models.CharField(max_length=50,verbose_name="Confirm Password")


    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_images')
    profession = models.CharField(max_length=100, verbose_name="Profession", default="Developer", null=True)

    def __str__(self):
        return self.user.username

   



