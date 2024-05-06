from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Menu, Tag, Category


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


# Create your views here.
def index(request):
    t = get_object_or_404(Tag, name="Hot")
    c = get_object_or_404(Category, name="Pizza")
    HotPizzaPosts = Menu.objects.filter(tags=t, category=c)[:6]
    MenuPricing = Menu.objects.all()[:8]
    HotPizzaPosts1, HotPizzaPosts2 = split_list(HotPizzaPosts)
    MenuPricing1, MenuPricing2 = split_list(MenuPricing)
    context = {"HotPizzaPosts1": HotPizzaPosts1, "HotPizzaPosts2": HotPizzaPosts2, "MenuPricing1": MenuPricing1, "MenuPricing2": MenuPricing2}
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
    pizza = get_object_or_404(Category, name="Pizza")
    pasta = get_object_or_404(Category, name="Pasta")
    salad = get_object_or_404(Category, name="Salad")
    drink = get_object_or_404(Category, name="Drink")
    PizzaMenu = Menu.objects.filter(category=pizza)
    PizzaMenu1, PizzaMenu2 = split_list(PizzaMenu)
    PastaMenu = Menu.objects.filter(category=pasta)
    PastaMenu1, PastaMenu2 = split_list(PastaMenu)
    SaladsMenu = Menu.objects.filter(category=salad)
    SaladsMenu1, SaladsMenu2 = split_list(SaladsMenu)
    DrinksMenu = Menu.objects.filter(category=drink)
    DrinksMenu1, DrinksMenu2 = split_list(DrinksMenu)
    context = {"PizzaMenu1": PizzaMenu1, "PizzaMenu2": PizzaMenu2, "PastaMenu1": PastaMenu1,
               "PastaMenu2": PastaMenu2, "SaladsMenu1": SaladsMenu1, "SaladsMenu2": SaladsMenu2,
               "DrinksMenu1": DrinksMenu1, "DrinksMenu2": DrinksMenu2, }
    return render(request, "menu.html", context)


def order(request):
    context = {}
    return render(request, "services.html", context)
