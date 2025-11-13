from django.shortcuts import render, redirect, get_object_or_404
from .models import Cracker,Offer,UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Home page - list all crackers
def home(request):
    crackers = Cracker.objects.all()
    return render(request, 'home.html', {'crackers': crackers})

# Add cracker page without Django Form
def add_cracker(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if name and price and image:  # basic validation
            Cracker.objects.create(
                name=name,
                price=price,
                description=description,
                image=image
            )
            return redirect('home')

    return render(request, 'add_cracker.html')

# View cracker details
def view_cracker(request, pk):
    cracker = get_object_or_404(Cracker, pk=pk)
    return render(request, 'view_cracker.html', {'cracker': cracker})

def offers(request):
    offers_list = Offer.objects.all()
    return render(request, 'offers.html', {'offers': offers_list})

def add_offer(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        discount = request.POST['discount']
        image = request.FILES['image']

        # Save new offer
        Offer.objects.create(
            title=title,
            description=description,
            discount=discount,
            image=image
        )
        return redirect('offers')

    return render(request, 'add_offer.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')

        # Generate a simple user ID (auto increment based on last user)
        last_user = UserProfile.objects.order_by('-userid').first()
        if last_user:
            userid = last_user.userid + 1
        else:
            userid = 1

        # Save new user
        UserProfile.objects.create(
            username=username,
            userid=userid,
            phone=phone
        )
        messages.success(request, "Registration successful! Your User ID is {}".format(userid))
        return redirect('login')

    return render(request, 'register.html')

# Login User
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        userid = request.POST.get('userid')

        try:
            user = UserProfile.objects.get(username=username, userid=userid)
            request.session['user_id'] = user.userid  # store in session
            request.session['username'] = user.username
            messages.success(request, "Login successful! Welcome {}".format(user.username))
            return redirect('home')
        except UserProfile.DoesNotExist:
            messages.error(request, "Invalid username or User ID")
            return redirect('login')

    return render(request, 'login.html')

# -------------------------------
# Logout User
# -------------------------------
def logout_user(request):
    request.session.flush()
    messages.success(request, "You have been logged out.")
    return redirect('login')

def contact(request):
    # Simply render the static contact page
    return render(request, 'contact.html')