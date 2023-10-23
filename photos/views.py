from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
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

    # add context data
    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Subir foto'
        return context

class PhotoUpdateView(UpdateView):
    model = Photo
    template_name = 'photos/photo_form.html'
    form_class = PhotoForm
    success_url = reverse_lazy('photos:photo_list')

     # add context data
    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar foto'
        return context

