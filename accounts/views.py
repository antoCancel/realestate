from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, 'Passwords does not match')
            return redirect('register')
        else:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Username already taken')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'Email already in use')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'Registeration successful, now log in')
                    return redirect('login')
    else:
        return render(request, 'accounts/register.html')

def loginhere(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid cred')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logouthere(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):

    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    data = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', data)
    