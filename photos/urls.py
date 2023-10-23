from django.urls import path
from .views import (
    PhotoListView,
    PhotoDetailView,
    PhotoCreateView,
    PhotoUpdateView,
    photo_delete
)

app_name = 'photos'

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    path('<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('create/', PhotoCreateView.as_view(), name='photo_create'),
    path('<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('<int:pk>/delete/', photo_delete, name='photo_delete'),
]