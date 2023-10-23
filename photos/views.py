from typing import Any
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Photo, FavoritePhoto
from .forms import PhotoForm

def favorite_photos(request):
    favorite_photos = FavoritePhoto.objects.all(user=request.user)
    return render(request, 'photos/favoritephoto_list.html', {'favorite_photos': favorite_photos})

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
    if request.user.is_superuser:
        photo = get_object_or_404(Photo, pk=pk)
        photo.delete()
        return redirect('photos:photo_list')
    else:
        return redirect('photos:photo_list')

class FavoritesPhotoListView(LoginRequiredMixin, ListView):
    model = FavoritePhoto
    template_name = 'photos/favoritesphoto_list.html'
    context_object_name = 'favorite_photos'
    login_url = reverse_lazy('account_login')

@login_required(login_url="account_login")
def add_to_favorites(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    favorite, created = FavoritePhoto.objects.get_or_create(user=request.user, photo=photo)
    if created:
        # Successfully added to favorites
        return redirect('photos:photo_detail', pk=photo_id)
    else:
        # Photo is already in favorites, handle accordingly
        return redirect('photos:photo_detail', pk=photo_id)

@login_required(login_url="account_login")
def remove_from_favorites(request,  photo_id):
    favorite = FavoritePhoto.objects.get(user=request.user, photo_id=photo_id)
    favorite.delete()
    # Successfully removed from favorites
    return redirect('photos:photo_detail', pk=photo_id)