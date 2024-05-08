from django import forms
from django.contrib import admin
from .models import Tag, Category, Menu, BlogPost, Comments, Profile, BlogPostCategory, ContactModel, Order, OrderModel

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

class YourModelAdminForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'rows': 10}) # Adjust 'rows' as needed
        }

class YourModelAdmin(admin.ModelAdmin):
    form = YourModelAdminForm


admin.site.register(OrderModel, YourModelAdmin)