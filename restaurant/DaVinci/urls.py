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
]