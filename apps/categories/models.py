from django.db import models
from apps.companies.models import Company



class Category(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_offers(self):
        pass