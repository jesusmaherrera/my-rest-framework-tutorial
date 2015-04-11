from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

from snippets.serializer import UserSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetriveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer