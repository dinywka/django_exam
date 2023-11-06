from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib.auth import authenticate, login
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import UserSerializer

from . import models

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

def posts(request):
    if request.method == 'GET':
        return render(request, 'django_ads_app/posts.html')
    elif request.method == 'POST':
        title = request.POST.get("title", None)
        description = request.POST.get("description", None)
        image = request.FILES.get("image", None)
        models.Post.objects.create(author=request.user, title=title, description=description,
                                   image=image if image else None)
        return redirect(reverse("post_list"))
    else:
        raise ValueError("Invalid method")

def post_list(request: HttpRequest) -> HttpResponse:
    posts = models.Post.objects.all()
    selected_page = request.GET.get(key="page", default=1)
    return render(request, "django_ads_app/post_list.html", context={"current_page": selected_page})


def comments(request: HttpRequest, pk: str) -> HttpResponse:
    try:
        post = models.Post.objects.get(id=int(pk))
    except models.Post.DoesNotExist:
        return HttpResponse("Post not found", status=404)

    if request.method == "POST":
        text = request.POST.get("text", "")
        models.Comment.objects.create(post=post, author=request.user, text=text)

    return redirect(reverse("post_detail", args=(pk,)))

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer


class ObtainToken(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))

        if user:
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            login(request, user)
            return Response({'token': token})
        else:
            return Response({'error': 'Invalid credentials'})



