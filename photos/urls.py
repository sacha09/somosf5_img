from django.urls import path
from .views import (
    PhotoListView,
)

app_name = 'photos'

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
]