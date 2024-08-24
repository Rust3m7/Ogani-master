from django.contrib import admin
from .models import (
    Blog, ProductCategory, BlogCategory,   Product,
    Discount_Product, Discount_category, Contact, Setting, Category
)

admin.site.register(Setting)
admin.site.register(Category)
admin.site.register(BlogCategory)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Discount_category)
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','like','view','category']
    readonly_fields = ['like','view']
    search_fields = ['name','price']
    fields = ('name','menu', 'image', 'category', 'description', 'price','like','view','is_activate')
    list_filter = ['category','price','created_at']
    list_display_links = ['name']
    list_per_page=10


@admin.register(Discount_Product)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at', 'created_at',)
    search_fields = ('name', 'content')
    ordering = ('-created_at', '-price' )
    readonly_fields = ('heart', 'retweet', )


admin.site.site_header = 'Projects'