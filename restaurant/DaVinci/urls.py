from django.contrib.auth.views import LoginView

from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("blog", views.blog, name="blog"),
    path("contact", views.contact, name="contact"),
    path("menu", views.menu, name="menu"),
    path("order", views.order, name="order"),
    path("blog/post/<int:id>", views.post, name="post"),
    path("blog/login", LoginView.as_view(), name="blog_login"),
    path("blog/logout/", views.blog_logout, name="blog_logout"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path("blog/registration/", views.registration, name="registration"),
    path("blog/profile_update", views.profile_update, name="profile_update"),
    path("blog/registration", views.registration, name="registration"),
    path("blog/create", views.create, name="create"),
    path("category/<str:name>", views.category, name="category"),
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
]