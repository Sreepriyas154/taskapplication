from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View
from task.models import Task
from task.forms import Registrationform,Loginform
from django.contrib.auth.models import User

class Indexview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html") 
class Loginview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")
# class Registrationview(View):
    # def get(self,request,*args,**kwargs):
        # return render(request,"registration.html")
class Taskaddview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"addtask.html")
    def post(self,request,*args,**kwargs):
        name=request.POST.get("username")
        task=request.POST.get("task")
        Task.objects.create(user=name,taskname=task)
        return render(request,"addtask.html")
class Tasklistview(View):
    def get(self,request,*args,**kwargs):
        qs=Task.objects.all()
        return render(request,"tasklist.html",{"todos":qs})

class Taskdetailview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        task=Task.objects.get(id=id)
        return render(request,"task-detail.html",{"todo":task})
class Taskdeleteview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Task.objects.filter(id=id).delete()
        return redirect("todo-list")

class  Registratioview(View):
    def get(self,request,*args,**kwargs):
        form=Registrationform()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=Registrationform(request.POST)
        if form.is_valid:
            User.objects.create_user(**form.cleaned_data)
            return redirect("todo-list")
        else:
            return render(request,"register.html",{"form":form})

class Loginview(View):
    def get(self,request,*args,**kwargs):
        form=Loginform()
        return render(request,"login.html",{"form":form})
    