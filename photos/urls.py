from django.urls import path
from .views import (
    PhotoListView,
    PhotoDetailView,
)

app_name = 'photos'

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    path('<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
]