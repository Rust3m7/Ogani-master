from pyexpat import model
from django.shortcuts import render,redirect
from core.models import Blog, BlogCategory, Product, ProductCategory, BlogCategory, Discount_Product

from core.forms import ContactForm
# Create your views here.

def home(request):

    return render(request, "index.html")



def shop(request):
 

    return render(request, 'shop-grid.html')




def blog(request):
    context = {
        'title' : 'Ogani Blog',
        'departments' : BlogCategory.objects.all(),
        'blogs' : Blog.objects.all(),
        'recent' : Blog.objects.all().order_by('-created_at')
    }


    return render(request, 'blog.html',context)




def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    
    
    context = {
        'title' : 'Ogani Contact',
        'departments' : ProductCategory.objects.all(),
        'form' : form,    
    }

    return render(request, 'contact.html', context)




def shop_details(request, slug):


    return render(request, 'shop-details.html')




def blog_details(request, slug):
 

    return render(request, 'blog-details.html')





def checkout(request):

    return render(request, 'checkout.html')




def shopping_cart(request):
  
    return render(request, 'shoping-cart.html')




def discount_details(request, slug):


    return render(request, 'discount_details.html')




def departments(request,slug):
   
    return render(request, 'departments.html')

