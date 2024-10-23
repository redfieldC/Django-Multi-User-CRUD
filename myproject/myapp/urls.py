from django.urls import path,include
from . import views 
urlpatterns = [
    path('',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('task-list/',views.task_list,name='task-list'),
    path('task-create/',views.task_create,name='task-create'),
    path('task-update/<int:task_id>/', views.task_update, name='task-update'),
    path('task-delete/<int:task_id>/', views.task_delete, name='task-delete'),
]