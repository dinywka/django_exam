from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import UserListView, UserDetailView


urlpatterns = [
    path("register/", views.register, name='register'),
    path("tags/", views.tags, name='tags'),
    path("posts/", views.posts, name='posts'),
    path("post/list/", views.post_list, name="post_list"),
    path("comment/<str:pk>/", views.comments, name='comments'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
]

