from django.db import models
from apps.companies.models import Company
from apps.categories.models import Category
from project.settings import AUTH_USER_MODEL





class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    description = models.TextField()
    count = models.IntegerField()
    price = models.IntegerField()
    avatar = models.ImageField(default='default.png', upload_to='products_images')

    def __str__(self):
        return self.name



