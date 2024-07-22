from urllib import request
from django.shortcuts import render
from products.models import Products,Category
from django.contrib.auth.decorators import login_required
def shop_view(request):
    if request.method == 'POST':
        search = request.POST['search']
        products=Products.objects.filter(name__icontains=search)
        if products:
            return render(request,template_name='main/base.html',context={'products':products,'value':search,"massege":'Sucessfully'})
        else:
            return render(request,template_name='main/base.html',context={'products':products,'value':search,"massege":'not found'})
    products=Products.objects.all()
    return render(request, template_name='main/base.html',context={'products': products})

def home_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Products.objects.filter(name__icontains=search)
        return render(request, 'shop.html', {'products': products})
    product = Products.objects.all()
    category = Category.objects.all()
    cantext = {
        'products': product,
        'category': category
    }
    return render(request,'index.html',cantext)








def products_view(request):
    product=Products.objects.all()
    category=Category.objects.all()
    cantext={
        'products':product,
        'category':category
    }
    return render(request, 'shop.html',context=cantext)

def contact_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Products.objects.filter(name__icontains=search)
        return render(request, 'shop.html', {'products': products})
    product = Products.objects.all()
    category = Category.objects.all()
    cantext = {
        'products': product,
        'category': category
    }
    return render(request, 'contact.html', cantext)


@login_required()
def cart_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Products.objects.filter(name__icontains=search)
        return render(request, 'shop.html', {'products': products})
    product = Products.objects.all()
    category = Category.objects.all()
    cantext = {
        'products': product,
        'category': category
    }
    return render(request, 'cart.html', cantext)


def testimonial_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Products.objects.filter(name__icontains=search)
        return render(request, 'shop.html', {'products': products})
    product = Products.objects.all()
    category = Category.objects.all()
    cantext = {
        'products': product,
        'category': category
    }
    return render(request, 'testimonial.html', cantext)


def chackout_view(request):
    return render(request, 'chackout.html')
# def category(requast):
#     return render(request, 'shop.html')
login_required(login_url='auth')
def category_view (request):
    if request.method == "POST":
        search = request.POST['search']
        products = Products.objects.filter(name__icontains=search)
        return render(request, 'shop-detail.html', {'products': products})
    product = Products.objects.all()
    category = Category.objects.all()
    cantext = {
        'products': product,
        'category': category
    }
    return render(request, 'shop-detail.html', cantext)



