from django.shortcuts import render, redirect
from todo.models import *
from .forms import *
from django.http import HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
# .order_by('check-in', 'check-out', 'location')
def listTask(request):
    queryset = task.objects.order_by('complete','due')
    form = TaskForm()
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'tasks':queryset,
        'form':form,
        }
    return render(request, 'list_task.html', context)


def updateTask(request, pk):
    queryset = task.objects.get(id=pk)
    form = UpdateForm(instance=queryset)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect("/home")


    context = {
        'form':form
        }

    return render(request, 'update_task.html', context)

def deleteTask(request, pk):
    queryset = task.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect("/home")


    context = {
        'item':queryset
        }
    return render(request, 'delete_task.html', context)




def home1(request):
    return render(request,"index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()

        messages.success(request,"acc created")

        return redirect('/signin')
    return render(request, "signup.html")





def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request,user)
            return redirect("home/")

        else:
            messages.error(request,"invalid credentials")
            return HttpResponse("wrong password")

    return render(request,"signin.html")




def signout(request):
    return render(request,"index.html")
