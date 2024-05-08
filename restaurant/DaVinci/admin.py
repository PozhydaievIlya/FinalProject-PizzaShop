from django.contrib import admin
from .models import Tag, Category, Menu, BlogPost, Comments, Profile, BlogPostCategory, ContactModel

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Comments)
admin.site.register(Profile)

class MenuAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ['name', 'category', 'price', 'pk']
    list_filter = ['category']


admin.site.register(Menu, MenuAdmin)
admin.site.register(BlogPostCategory)
admin.site.register(ContactModel)