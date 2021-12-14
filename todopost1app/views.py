
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Task
from . forms import Todoforms
from django.contrib import messages
from django.contrib.auth.models import User,auth




# Create your views here.

def fun(request):

    return render(request,"index.html")




















def task_view(request):
    obj1=Task.objects.all()
    if request.method=='POST':
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        date=request.POST.get('date')

        obj=Task(title=title,desc=desc,date=date)
        obj.save()

    return render(request,'task_view.html',{'obj1':obj1})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')

    return render(request,'delete.html',{'task':task})
def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('login')
    else:
            return render(request, "login.html")


def reg(request):
        if request.method=="POST":
                first_name=request.POST['first_name']
                last_name=request.POST['last_name']
                username=request.POST['username']
                password1=request.POST['password1']
                password2=request.POST['password2']
                email=request.POST['email']
                if password1==password2:
                        if User.objects.filter(username=username).exists():
                                messages.info(request,"username already taken")
                                return redirect('reg')
                        elif User.objects.filter(email=email).exists():
                                messages.info(request,"email already taken")
                                return redirect('reg')
                        else:
                                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                                user.save();
                                print("user created")
                else:
                        print("password not matched")
                        return redirect('reg')
                return redirect('/')
        else:
                return render(request, 'registration.html')


def logout(request):

        auth.logout(request)
        return redirect('/')
