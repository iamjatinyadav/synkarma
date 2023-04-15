from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='postsdetail'),
]