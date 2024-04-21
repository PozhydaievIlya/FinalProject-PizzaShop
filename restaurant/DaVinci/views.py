from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def blog(request):
    context = {}
    return render(request, "blog.html", context)


def blog_single(request):
    context = {}
    return render(request, "blog-single.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)


def menu(request):
    context = {}
    return render(request, "menu.html", context)


def services(request):
    context = {}
    return render(request, "services.html", context)
