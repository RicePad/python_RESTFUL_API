from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(ownner=self.request.user)

class SnippetListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
