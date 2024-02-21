from django.shortcuts import render, redirect
from .models import Product, CartItem, contact_info
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def home(request):
    return render(request, 'user/userhome.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'user/userhome.html', {'products': products})

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'user/cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'user/loginuser.html', {'form': AuthenticationForm()})
    else:
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(request, username=a, password=b)
        if user is None:
            return render(request, 'user/loginuser.html', {'form': AuthenticationForm(), 'error': 'Invalid credentials'})
        else:
            login(request, user)
            return redirect('/user/')  # Replace 'user_page' with the URL name of your user page
        

def signupuser(request):
    if  request.method == 'GET':
        return render(request,'user/signupuser.html',{'form': UserCreationForm()})
    else:
        a=request.POST.get('username')
        b=request.POST.get('password1')
        c=request.POST.get('password2')
        if b==c:
            #check whether user name is unique
            if (User.objects.filter(username = a)):
                return render(request, 'user/signupuser.html',{'form': UserCreationForm(), 'error':'Username already exists Try again with different username'})
            else:
                user=User.objects.create_user(username = a, password =b)
                user.save()
                login(request,user)
                return redirect('/user/')

        else:
            #password 1 and 2 do not match
            return render(request, 'user/signupuser.html',{'form': UserCreationForm(),'error':'Password Mismatch Try Again'})

def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('/user/')
    
def contact(request):   
    if request.method == 'GET':
        return render(request, 'user/contact.html')
    elif request.method == 'POST':
        email = request.POST.get('user_email')
        message = request.POST.get('message')
        x = contact_info(u_email=email, u_message=message)
        x.save()
        return render(request, 'user/contact.html', {'feedback': 'Your message has been recorded'})

def about_us(request):
    return render(request, 'user/about.html')