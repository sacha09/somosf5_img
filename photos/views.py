from django.shortcuts import render
from django.views.generic import ListView
from .models import Photo

class PhotoListView(ListView):
    model = Photo
    template_name = 'photos/photo_list.html'
    context_object_name = 'photos'