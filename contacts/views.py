from rest_framework import generics
from .models import Contact
from .serializers import ContactListSerializer, ContactDetailSerializer, ContactSerializer
from .permissions import IsSuperUser

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
    permission_classes = [IsSuperUser]

class ContactDetailView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializer
    permission_classes = [IsSuperUser]
