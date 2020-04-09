from django.db import models
from apps.products.models import Product
from project.settings import AUTH_USER_MODEL





class Order(models.Model):
    STATUS = (
        (1, 'В обоботке'),
        (2, 'В пути'),
        (3, 'Доставлено'),
    )
    status = models.IntegerField(choices=STATUS, default=1)
    user = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, null=True, on_delete=models.PROTECT)
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'№ {self.id}: {self.product.name} for {self.user.first_name} {self.user.last_name}'

    @property
    def price(self):
        return self.product.price * self.count