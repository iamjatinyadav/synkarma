from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Post 
from rest_framework import permissions
from base.permissions import IsOwnerOrReadOnly
from rest_framework.throttling import UserRateThrottle
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class PostView(generics.ListCreateAPIView, generics.GenericAPIView):
    serializer_class = PostSeraializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ["title", "body","author__username"]
    ordering_fields = ('id',)

    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):
    serializer_class = PostSeraializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    throttle_classes = [UserRateThrottle]


