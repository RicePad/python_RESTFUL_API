from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(ownner=self.request.user)

class SnippetListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
