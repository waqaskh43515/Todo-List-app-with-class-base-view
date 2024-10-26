from django.urls import path
from .views import TaskList, taskdetail, taskcreate, taskupdate , taskdelete , customloginview, RegisterPage 

from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('login/', customloginview.as_view(), name='login'), 
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),  
    path('register/',RegisterPage.as_view(), name='register'),  

 

    path('', TaskList.as_view(), name='TaskList'),
    path('task/<int:pk>/', taskdetail.as_view(), name='task'),
    path('task-create/', taskcreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', taskupdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', taskdelete.as_view(), name='task-delete'),
]







