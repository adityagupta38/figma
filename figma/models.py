from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', editable=False)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gen_choice = (
        ('', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices= gen_choice)


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', editable=False)
    photo = models.ImageField(upload_to='user_posts')
