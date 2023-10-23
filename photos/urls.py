from django.urls import path
from .views import (
    PhotoListView,
    PhotoDetailView,
    PhotoCreateView,
    PhotoUpdateView,
    photo_delete,
    FavoritesPhotoListView,
    add_to_favorites,
    remove_from_favorites
)

app_name = 'photos'

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    path('<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('create/', PhotoCreateView.as_view(), name='photo_create'),
    path('<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('<int:pk>/delete/', photo_delete, name='photo_delete'),
    path('favoritos/', FavoritesPhotoListView.as_view(), name='favorites_photo_list'), 
    path('<int:photo_id>/add_to_favorites/', add_to_favorites, name='add_to_favorites'),
    path('<int:photo_id>/remove_from_favorites/', remove_from_favorites, name='remove_from_favorites'),
]