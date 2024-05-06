from django.contrib import admin
from .models import Tag, Category, Menu

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)


class MenuAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ['name', 'category', 'price', 'pk']
    list_filter = ['category']



admin.site.register(Menu, MenuAdmin)
