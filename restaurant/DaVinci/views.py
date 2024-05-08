from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm, UserUpdateForm, RegistrationForm, ProfilePhotoForm, PostForm, ContactForm
from .models import Menu, Tag, Category, BlogPost, Profile, BlogPostCategory
from django.contrib.messages import constants as messages
from django.utils.timezone import now


def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


# Create your views here.
def index(request):
    ResentPosts = BlogPost.objects.order_by("-published_date")[:3]
    t = get_object_or_404(Tag, name="Hot")
    c = get_object_or_404(Category, name="Pizza")
    HotPizzaPosts = Menu.objects.filter(tags=t, category=c)[:6]
    MenuPricing = Menu.objects.all()[:8]
    HotPizzaPosts1, HotPizzaPosts2 = split_list(HotPizzaPosts)
    MenuPricing1, MenuPricing2 = split_list(MenuPricing)
    # Get in touch (Contact)
    if request.method == 'POST':
        Cform = ContactForm(request.POST)
        if Cform.is_valid():
            contactElement = Cform.save(commit=False)
            contactElement.save()
    else:
        Cform = ContactForm()
    context = {"HotPizzaPosts1": HotPizzaPosts1, "HotPizzaPosts2": HotPizzaPosts2,
               "MenuPricing1": MenuPricing1, "MenuPricing2": MenuPricing2,
               "ResentPosts": ResentPosts, "Cform": Cform}
    return render(request, "index.html", context)


def about(request):
    # Get in touch (Contact)
    if request.method == 'POST':
        Cform = ContactForm(request.POST)
        if Cform.is_valid():
            contactElement = Cform.save(commit=False)
            contactElement.save()
    else:
        Cform = ContactForm()
    context = {"Cform": Cform}
    return render(request, "about.html", context)


def blog(request):
    posts = BlogPost.objects.order_by("-published_date")
    category = BlogPostCategory.objects.all()
    context = {"posts": posts, "category": category}
    return render(request, "blog.html", context)


def post(request, id=None):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
    ResentPosts = BlogPost.objects.order_by("-published_date")[:3]
    category = BlogPostCategory.objects.all()
    post = get_object_or_404(BlogPost, pk=id)
    # A comment form
    form = CommentForm(request.POST or None)
    comment = None
    if form.is_valid():
        # Create a Comment object before saving it to the database
        comment = form.save(commit=False)
        comment.post = post
        # Save the comment to the database
        comment.save()
        pass
    # List of active comments for this article
    comments = post.comments.all().order_by("-date")
    context = {"post": post, "comment": comment, "form": form, "comments": comments, "ResentPosts": ResentPosts,
               "category": category}
    return render(request, "blog-single.html", context)


def contact(request):
    # Get in touch (Contact)
    if request.method == 'POST':
        Cform = ContactForm(request.POST)
        if Cform.is_valid():
            contactElement = Cform.save(commit=False)
            contactElement.save()
    else:
        Cform = ContactForm()
    context = {"Cform":Cform}
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
    OrderMenu = Menu.objects.all().order_by("category")
    context = {"OrderMenu": OrderMenu}
    return render(request, "order.html", context)


def blog_logout(request):
    logout(request)
    return redirect('/')


def blog_login(request):
    context = {}
    return render(request, 'registration/login.html', context)


def profile(request, pk):
    if request.user.is_authenticated:
        currentUser = User.objects.get(id=request.user.id)
    profile_user = Profile.objects.get(user_id=pk)
    if request.method == "POST":
        photoForm = ProfilePhotoForm(request.POST or None, request.FILES or None, instance=profile_user)
        if photoForm.is_valid():
            photoForm.save()
            return redirect(f'/profile/{pk}')

    photoForm = ProfilePhotoForm()
    context = {"photoForm": photoForm, "profile_user": profile_user}
    return render(request, 'profile.html', context)


def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            # Log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    context = {"form": form, }
    return render(request, 'registration/registration.html', context)


def profile_update(request):
    # Update form
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        UpdateForm = UserUpdateForm(request.POST or None, instance=current_user)
        if UpdateForm.is_valid():
            UpdateForm.save()
            login(request, current_user)
            return redirect(f'/profile/{request.user.id}')
        context = {"UpdateForm": UpdateForm}
        return render(request, 'profile_update.html', context)
    else:
        messages.SUCCESS(request, "You must be logged in")
        return redirect('index')


def create(request):
    current_user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = now()
            post.user = current_user
            post.save()
            return index(request)
    form = PostForm()

    context = {"form": form}
    return render(request, 'create.html', context)


def category(request, name=None):
    category = BlogPostCategory.objects.all()
    c = get_object_or_404(BlogPostCategory, name=name)
    posts = BlogPost.objects.filter(category=c).order_by("-published_date")
    context = {"posts": posts, "category": category}
    return render(request, 'blog.html', context)
