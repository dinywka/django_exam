from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'django_ads_app/register.html')
    elif request.method == 'POST':
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        try:
            User.objects.create(
                username=email,
                password=make_password(password),
                email=email,
            )
        except Exception as error:
            return HttpResponse(error)
        return HttpResponse("Вы зарегистрированы!")
    else:
        raise ValueError("Invalid method")

def tags(request):
    if request.method == 'GET':
        user_list = User.objects.all()
        print(user_list)
        return render(request, 'django_ads_app/tags.html', context={'user_list': user_list})

