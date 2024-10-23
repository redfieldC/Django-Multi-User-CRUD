from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def loginPage(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      return redirect('task-list')
    else:
      messages.error(request,'Invalid username or password')
  return render(request,'login.html')

def registerPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif password != password2:
            messages.error(request, 'Passwords do not match')
        else:
            # Create the user
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Registration successful')
            return redirect('login')

    return render(request, 'register.html')

def task_list(request):
   if request.user.is_authenticated:
    return render(request,'taskList.html')
   else:
      return redirect('login')

def logout_view(request):
  logout(request)
  return redirect('login')