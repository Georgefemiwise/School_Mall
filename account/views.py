from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def registerUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name =request.POST['last_name']
        email =request.POST['email']
        username =request.POST['username']
        password1 =request.POST['password1']
        password2 =request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is taken please try again!')
                return redirect('register')

            elif  User.objects.filter(email=email).exists():
                messages.info(request,'Email already in use please try again!')
                return redirect('register')

            else:
                User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
                User.save
                return redirect('login')

    
        else:
            messages.info(request,'Password not the same!')

    else:
        return render(request, 'account/register.html')
        
def loginUser(request):
    if request.method == 'POST':


        username =request.POST['username']
        password =request.POST['password']

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            lname = user.last_name
            return render(request, 'books/index.html', {"name": f"{fname} {lname}"})

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'account/login.html')
