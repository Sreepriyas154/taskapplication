"""
URL configuration for taskapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task.views import Indexview,Loginview,Taskaddview,Tasklistview,Taskdetailview,Taskdeleteview,Registratioview,Loginview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Indexview.as_view()),
    path('login/',Loginview.as_view()),
    
    path('addtask',Taskaddview.as_view(),name="todo-add"),
    path('tasklist',Tasklistview.as_view(),name="todo-list"),
    path('task/<int:id>',Taskdetailview.as_view(),name="todo-detail"),
    path('task/<int:id>/remove',Taskdeleteview.as_view(),name="todo-delete"),
    path('accounts/register',Registratioview.as_view(),name="register"),
    path('accounts/login',Loginview.as_view(),name="signin"),
]
