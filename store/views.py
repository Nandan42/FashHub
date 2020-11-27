from django.shortcuts import render,redirect
from .models import Contact,Journal,Product,Cart,Wishlist,events,Donations

# Create your views here.


def index(request):
    if request.method=='POST':
        email = request.POST['email']
        message = request.POST['Message']

        contact = Contact.objects.create(name=email,details=message)
        contact.save()
        
        # product = Product.objects.all()

        # context = {
        #     'product':product,
        # }
    return render(request,'index.html')

def eventform(request):
    if request.method=='POST':
        username = request.POST['Event Name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        organization = request.POST['Organisation']
        date = request.POST['date']
        venue = request.POST['venue']
        bio = request.POST['Bio']

        event = events.objects.create(name=username,organizer_name=organization,bio=bio,phone_number=phone_number,email=email,venue=venue,date=date)
        event.save()
        return redirect('/eventform')
    return render(request,'eventreg.html')

def eventpage(request):
    event = events.objects.all()
    context = {
        'events':event,
    }
    return render(request,'events.html',context=context)

def event(request,id):
    event = events.objects.get(id=id)
    context = {
        'event':event,
    }
    return render(request,'event.html',context=context)

def journal(request):
    journals = Journal.objects.all()
    context = {
        "journals":journals,
    }
    return render(request,'journal.html',context=context)

def journal_page(request,id):
    journal = Journal.objects.get(id=id)
    context = {
        'journal':journal,
    }
    return render(request,'journal-page.html',context=context)

def aboutus(request):
    return render(request,'aboutus.html')

# def products(request):
#     products = Product.objects.all()
    
#     context = {
#         "products":products,
#     }
#     return render(request,'products.html',context=context)

def product(request,id):
    product = Product.objects.get(id=id)

    context = {
        "product":product,
    }
    return render(request,'product.html',context=context)

def showcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {
        'cart':cart,
    }
    return render(request,'cart.html',context=context)

def addcart(request,id):
    product = Product.objects.get(id=id)
    Cart.objects.create(item=product,user=request.user)
    return redirect('/')

def buy(request,id):
    product = Product.objects.get(id=id)
    product.count-=1
    if product.count<0:
        product.count=0
    product.save()
    return redirect('/')

def buycart(request):
    cart = Cart.objects.filter(user=request.user)
    for item in cart:
        item.item.count-=1
        if item.item.count<0:
            item.item.count=0
        item.item.save()
    cart = Cart.objects.filter(user=request.user).delete()
    return redirect('/')

def showWishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlist':wishlist,
    }
    return render(request,'wishlist.html',context=context)

def addWishlist(request,id):
    product = Product.objects.get(id=id)
    Wishlist.objects.create(item=product,user=request.user)
    return redirect('/')
    
def removeWishlist(request,id):
    product = Product.objects.get(id=id)
    Wishlist.objects.get(item=product).delete()
    return redirect('showWishlist/')
#remove cart feature

def genderCategory(request,gender,category):
    product = Product.objects.filter(gender=gender,category=category)
    context = {
        "product":product,
        "gender":gender,
        "category":category,
    }
    return render(request,'sproducts.html',context=context)

def donation(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        address = request.POST['address']
        clothes_number = request.POST['clothes']

        donation = Donations.objects.create(phone_number=phone_number,email=email,Name=name,address=address,clothes_number=clothes_number)
        donation.save()
    return render(request,'donations.html')