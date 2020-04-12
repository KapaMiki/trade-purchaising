from django.db import models
from project.settings import AUTH_USER_MODEL
from django.core.exceptions import ValidationError



class Company(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    activity = models.TextField()
    description = models.TextField()
    created_data = models.DateField()
    BIN = models.CharField(max_length=50)
    photo = models.ImageField(default='default.png', upload_to='companies_images')
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

    def clean_fields(self, exclude=None):
        if self.owner.is_businessman == 0:
            raise ValidationError('User is not businessman')
