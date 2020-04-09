from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):

    GENDER = [
        (0, ('Man')),
        (1, ('Woman')),
    ]

    phone = models.CharField(max_length=12, null=True, blank=True)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, default=0, null=True, blank=True)
    avatar = models.ImageField(default='default.png', upload_to='users_images')
    IIN = models.CharField(max_length=15, null=True, blank=True)
    is_businessman = models.BooleanField(default=0)

    def __str__(self):
        return self.username

