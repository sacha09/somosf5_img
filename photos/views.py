from typing import Any
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photos/photo_form.html'
    form_class = PhotoForm
    success_url = reverse_lazy('photos:photo_list')
    login_url = reverse_lazy('account_login')

    # add context data
    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Subir foto'
        return context

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    template_name = 'photos/photo_form.html'
    form_class = PhotoForm
    success_url = reverse_lazy('photos:photo_list')
    login_url = reverse_lazy('account_login')

     # add context data
    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar foto'
        return context

@login_required(login_url="account_login")
def photo_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('photos:photo_list')