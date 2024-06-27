from rest_framework import generics
from rest_framework import permissions
from .models import Tag
from .serializers import TagSerializer

class TagList(generics.ListCreateAPIView):
    """
    List tags or create a new tag.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a tag.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]