from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def Home(request):
    return render(request,'homePage.html')

def register(request):
    if request.method=='POST':
        first_name=request.post['first_name']
        last_name = request.post['last_name']
        gender=request.post['gender']
        degree=request.post['degree']
        birth_date=request.post['birth_date']
        email=request.post['email']
        password=request.post['password']


        newUser=User(first_name=first_name,last_name=last_name,gender=gender,degree=degree,
                     birth_date=birth_date,email=email,password=password)

        newUser.save()

    context={}
    return render(request,'signUp.html')

def login(request):
    return render(request,'sighIn.html')
