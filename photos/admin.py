from django.contrib import admin
from .models import Photo, FavoritePhoto

admin.site.register(Photo)
admin.site.register(FavoritePhoto)