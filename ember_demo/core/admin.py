from django.contrib import admin
from .models import Product, Review


class ProductAdmin(admin.ModelAdmin):

    class Meta:
        model = Product


class ReviewAdmin(admin.ModelAdmin):

    class Meta:
        model = Review

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
