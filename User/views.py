from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request , "index.html")

def reg(request):
    return render(request, "reg.html")

def user(request):
    return render(request, "user.html")

def reginsert(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(first_name=first_name, last_name=last_name,username=username, email=email, password=password)
        user.save()
        return render(request, "index.html")
    else:
        return HttpResponse('<script> alert("Submission Error...!!!") </script>')

def user_insert(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['password']
        user = User,object.create_user(name = name, contact_number = contact_number, email = email, address = address, password = password)
        user.save()
        return render(request, "index.html")
    else:
        return HttpResponse('<script> alert("Submission Error...!!!") </script>')
    