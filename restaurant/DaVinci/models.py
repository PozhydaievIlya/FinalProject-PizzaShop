from datetime import datetime

from django.contrib import admin
from django.db import models
from django.db.models.signals import post_save
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
    image = models.ImageField(upload_to="Product_images", default="static/images/400x400.png")
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


# Not used!
class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    image = models.URLField(default="http://placehold.it/900x300")

    def __str__(self):
        return self.title


# Not used - end!


class ContactModel(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)
    text = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.user_name} messaging us! | Respond: {self.user_email}'

    class Meta:
        verbose_name = "Users get in touch"
        verbose_name_plural = "Users get in touch"


# profile & blog models
class BlogPostCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog post category"
        verbose_name_plural = "Blog post categories"


class BlogPost(models.Model):
    title = models.CharField(max_length=30, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Published date")
    category = models.ForeignKey(BlogPostCategory, on_delete=models.CASCADE, verbose_name="Post category")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    image = models.URLField(default="https://i.pinimg.com/736x/26/6f/60/266f60cae0cf8de803d642bef5ac5fea.jpg")
    short_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts on blog"


class Comments(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name="Назва посту", related_name='comments')
    username = models.CharField(max_length=30, verbose_name="Username")
    body = models.CharField(max_length=500, verbose_name="Comment")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f'Comment by {self.username} on {self.post} post'
        pass

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments on blog"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True,
                              upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "User profiles"


class Order(models.Model):
    customer = models.CharField(max_length=100, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} ordering! | Respond: {self.email}, Ship to: {self.address} - {self.date}'

    class Meta:
        verbose_name = "ORDER"
        verbose_name_plural = "ORDERS"