from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Tasks
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

def logout_view(request):
  logout(request)
  return redirect('login')


def task_list(request):
   if request.user.is_authenticated:
    tasks = Tasks.objects.filter(owner=request.user)
    return render(request,'taskList.html',{'tasks':tasks})
   else:
      return redirect('login')

def task_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')

            task = Tasks.objects.create(
                title=title,
                description=description,
                owner=request.user
            )
            messages.success(request, 'Task created successfully!')
            return redirect('task-list')  
        return render(request, 'taskCreate.html') 
    else:
        return redirect('login')

def task_update(request, task_id):
    if not request.user.is_authenticated:
        return redirect('login')  

    task = Tasks.objects.filter(id=task_id, owner=request.user).first()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if task:
            task.title = title
            task.description = description
            task.save()
            messages.success(request, 'Task updated successfully')
            return redirect('task-list')
        else:
            messages.error(request, 'Task not found or you do not have permission to update it.')

    return render(request, 'taskUpdate.html', {'task': task})

def task_delete(request, task_id):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if user is not authenticated

    task = Tasks.objects.filter(id=task_id, owner=request.user).first()

    if not task:
        messages.error(request, 'Task not found or you do not have permission to delete it.')
        return redirect('task-list')

    if request.method == 'POST':
        task.delete()  # Delete the task
        messages.success(request, 'Task deleted successfully.')
        return redirect('task-list')

    return render(request, 'task_confirm_delete.html', {'task': task})