from django.urls import path
from .views import TagList, TagDetail

urlpatterns = [
    path('tags/', TagList.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetail.as_view(), name='tag-detail'),
]