from django.urls import path,include
from . import views 
urlpatterns = [
    path('',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('task-list/',views.task_list,name='task-list')
]