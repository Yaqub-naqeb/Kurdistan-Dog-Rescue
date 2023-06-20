from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='success_stories'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
]