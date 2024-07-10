from django.urls import path
from contacts import views

urlpatterns = [
    path('contacts/', views.ContactListView.as_view(), name='contact-list'),
    path(
        'contacts/<int:pk>/',
        views.ContactDetailView.as_view(),
        name='contact-detail'),
    path('contact/', views.ContactCreateView.as_view(), name='contact-create'),
]
