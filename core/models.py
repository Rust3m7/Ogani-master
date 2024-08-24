from django.db import models
from ckeditor.fields import RichTextField
from core.utils.slug_title import generate_slug

# Create your models here.

Menu = (
    ('meat', 'Meat'),
    ('fastfood', 'Fastfood'),
    ('vegetables', 'Vegetables'),
)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_activate = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Setting(BaseModel):
    logo = models.ImageField(upload_to='logo/')
    # slider_image1 = models.ImageField(upload_to="slider/")
    # slider_image2 = models.ImageField(upload_to='slider/')
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=255)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)
    pinterest = models.URLField(null=True,blank=True)

    def __str__(self):
        return "First object"
    
    
class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='product/')
    like = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    menu = models.CharField(choices=Menu, max_length=20)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self) :
        return self.name
    
    @property
    def discount_price (self):
        if self.price > 10:
            return self.price - (self.price*0.1)
        return self.price
    
class BlogCategory(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'




class Contact(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.title
    
class ProductCategory(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='department_image', null=True, blank=True)
    slug = models.SlugField(unique=True)


    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(ProductCategory, self).save(*args, **kwargs)
    

class BlogCategory(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'


class Blog(BaseModel):
    title = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='blog/')
    category = models.ForeignKey('BlogCategory', on_delete=models.CASCADE, related_name='blogs')


    def __str__(self):
        return self.title
    



class Discount_Product(BaseModel):
    name = models.CharField(max_length=255)
    content = RichTextField()
    price = models.FloatField(default=0)
    discount_persentage = models.IntegerField()
    weight = models.FloatField(default=1)
    image = models.ImageField(upload_to='product', null=True, blank = True)
    heart = models.IntegerField(default=0)
    retweet = models.IntegerField(default=0)
    category = models.ForeignKey('Discount_category', on_delete=models.CASCADE, related_name='product')
    slug = models.SlugField(unique=True)

    
    class Meta:
        verbose_name = 'Discount Product'
        verbose_name_plural = 'Discount_Products'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(Discount_Product, self).save(*args, **kwargs)


class Discount_category(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='discount_images', null=True, blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Discount Category'
        verbose_name_plural = 'Discount Categories'