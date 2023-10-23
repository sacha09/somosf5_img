from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Photo
from .forms import PhotoForm

class PhotoListView(ListView):
    model = Photo
    template_name = 'photos/photo_list.html'
    context_object_name = 'photos'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photos/photo_detail.html'
    context_object_name = 'photo'

class PhotoCreateView(CreateView):
    model = Photo
    template_name = 'photos/photo_form.html'
    form_class = PhotoForm
    success_url = reverse_lazy('photos:photo_list')