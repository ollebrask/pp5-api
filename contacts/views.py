from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Contact
from .serializers import (
    ContactListSerializer,
    ContactDetailSerializer,
    ContactSerializer
)
from .permissions import IsSuperUser


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
    permission_classes = [IsSuperUser]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ['email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    ordering_fields = ['created_at']


class ContactDetailView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializer
    permission_classes = [IsSuperUser]
