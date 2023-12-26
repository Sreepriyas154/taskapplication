
from django.shortcuts import render,redirect
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import View,ListView,DetailView,UpdateView

from task.models import Task
from task.forms import Registrationform,Loginform,Taskupdate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator



def sign_in(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper



class Indexview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html") 
class Loginview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")
# class Registrationview(View):
    # def get(self,request,*args,**kwargs):
        # return render(request,"registration.html")


@method_decorator(sign_in,name="dispatch")
class Taskaddview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"addtask.html")
    def post(self,request,*args,**kwargs):
        name=request.POST.get("username")
        task=request.POST.get("task")
        Task.objects.create(user=name,taskname=task)
        messages.success(request,"task has been created")
        return render(request,"addtask.html")
    
@method_decorator(sign_in,name="dispatch")
class Tasklistview(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            qs=Task.objects.filter(user=request.user)
             # qs=request.user.task_set.all()
            return render(request,"tasklist.html",{"todos":qs})
        else:
            return redirect("signin")
        
@method_decorator(sign_in,name="dispatch")
class Taskdetailview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        task=Task.objects.get(id=id)
        return render(request,"task-detail.html",{"todo":task})
    
@method_decorator(sign_in,name="dispatch")
class Taskdeleteview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Task.objects.filter(id=id).delete()
        messages.success(request,"task has been deleted")
        return redirect("todo-list")

class  Registratioview(View):
    def get(self,request,*args,**kwargs):
        form=Registrationform()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=Registrationform(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"your redistration has been success")
            return redirect("signin")
        else:
            messages.error(request,"registration failed")
            return render(request,"register.html",{"form":form})

class Loginview(View):
    def get(self,request,*args,**kwargs):
        form=Loginform()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("todo-list")
            else:
                messages.error(request,"invalid deatil")
                return render(request,"login.html",{"form":form})
            
@sign_in
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")


# class Tasklist(ListView):
    # model=Task
    # template_name="tasklist.html"
    # context_object_name="todos"
    
    # def get_queryset(self):
        # return Task.objects.filter(user=self.request.user)

# class TaskDetail(DetailView):
    # model=Task
    # template_name="task-detail.html"
    # context_object_name="todo"
    # pk_url_kwarg="id"
    

class  Taskupdateview(UpdateView):
    model=Task
    form_class=Taskupdate
    template_name="update.html"
    context_object_name="todo"
    pk_url_kwarg="id"
    success_url=reverse_lazy("todo-list")