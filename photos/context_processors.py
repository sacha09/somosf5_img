from .models import FavoritePhoto

def favorite_photos(request):
    try:
        fav_photos = FavoritePhoto.objects.filter(user=request.user)
    except:
        fav_photos = None
    favorite_photos = []
    if fav_photos is not None:
        for photo in fav_photos:
            favorite_photos.append(photo.photo.id)

    return {'favorite_photos': favorite_photos}