from django.contrib import admin
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

    def __str__(self):
        return self.user_email

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
    image = models.URLField(default="http://placehold.it/900x300")
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
