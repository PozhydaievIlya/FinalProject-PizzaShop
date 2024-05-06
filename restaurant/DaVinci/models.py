from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product category"
        verbose_name_plural = "Product categories"



class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product tag"
        verbose_name_plural = "Product tags"


class Menu(models.Model):
    name = models.CharField(max_length=30, verbose_name="Position name")
    image = models.ImageField(upload_to="static/Product_images", default="static/images/400x400.png")
    short_description = models.CharField(max_length=80, verbose_name="Short description for post")
    description = models.TextField(verbose_name="Description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    tags = models.ManyToManyField(Tag)
    price = MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=11)

    def __str__(self):
            return f'{self.pk}. {self.category} |  {self.name}'
            pass

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    image = models.URLField(default="http://placehold.it/900x300")

    def __str__(self):
        return self.title


class ContactModel(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)

    def __str__(self):
        return self.user_email

    class Meta:
        verbose_name = "Користувачі для розсилки"
        verbose_name_plural = "Користувачі для розсилки"