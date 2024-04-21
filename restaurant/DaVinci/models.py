from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=30, verbose_name="Position name")
    image = models.URLField(default="http://placehold.it/900x300")
    description = models.TextField(verbose_name="Description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    tags = models.ManyToManyField(Tag)
    price = MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=11)


