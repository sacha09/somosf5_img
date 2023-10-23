from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Photo, FavoritePhoto

class PhotoModelTestCase(TestCase):
    def setUp(self):
        self.photo = Photo.objects.create(title="Test Photo", image="test.jpg")

    def test_photo_model(self):
        photo = Photo.objects.get(id=1)
        self.assertEqual(photo.title, "Test Photo")
        self.assertEqual(str(photo), "Test Photo")

class FavoritePhotoModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.photo = Photo.objects.create(title="Test Photo", image="test.jpg")
        self.favorite = FavoritePhoto.objects.create(user=self.user, photo=self.photo)

    def test_favorite_photo_model(self):
        favorite = FavoritePhoto.objects.get(id=1)
        self.assertEqual(favorite.user.username, "testuser")
        self.assertEqual(str(favorite), "testuser's favorite: Test Photo")

class PhotoListViewTestCase(TestCase):
    def test_photo_list_view(self):
        response = self.client.get(reverse('photos:photo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/photo_list.html')

class PhotoDetailViewTestCase(TestCase):
    def setUp(self):
        self.photo = Photo.objects.create(title="Test Photo", image="test.jpg")

    def test_photo_detail_view(self):
        response = self.client.get(reverse('photos:photo_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/photo_detail.html')

class PhotoCreateViewTestCase(TestCase):
    def test_photo_create_view(self):
        response = self.client.get(reverse('photos:photo_create'))
        self.assertEqual(response.status_code, 302)

class PhotoUpdateViewTestCase(TestCase):
    def setUp(self):
        self.photo = Photo.objects.create(title="Test Photo", image="test.jpg")

    def test_photo_update_view(self):
        response = self.client.get(reverse('photos:photo_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

class PhotoDeleteViewTestCase(TestCase):
    def setUp(self):
        self.photo = Photo.objects.create(title="Test Photo", image="test.jpg")

    def test_photo_delete_view(self):
        response = self.client.get(reverse('photos:photo_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

class FavoritePhotoListViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.photo = Photo.objects.create(title="Test Photo", image="test.jpg")
        self.favorite = FavoritePhoto.objects.create(user=self.user, photo=self.photo)

    def test_favoritephoto_list_view_authenticated(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse('photos:favorites_photo_list'))
        self.client.logout()
        
        self.assertEqual(response.status_code, 302)

    def test_favoritephoto_list_view_no_favorite(self):
        self.client.login(username="testuser", password="testpassword")
        FavoritePhoto.objects.all().delete()
        response = self.client.get(reverse('photos:favorites_photo_list'))
        self.client.logout()

        self.assertEqual(response.status_code, 302)

    def test_favoritephoto_list_view_not_authenticated(self):
        response = self.client.get(reverse('photos:favorites_photo_list'))
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('photos:favorites_photo_list')}")

class AddToFavoriteViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.photo = Photo.objects.create(title="Test Photo", image="test.jpg")

    def test_add_to_favorites_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('photos:add_to_favorites', args=[self.photo.id]))
        self.assertEqual(response.status_code, 302)  # Should be a redirect
        self.assertEqual(response.url, reverse('photos:photo_detail', args=[self.photo.id]))

        # Check if the photo was added to favorites
        favorite = FavoritePhoto.objects.filter(user=self.user, photo=self.photo)
        self.assertTrue(favorite.exists())

    def test_add_to_favorites_existing_favorite(self):
        self.client.force_login(self.user)

        # Add the photo to favorites
        favorite = FavoritePhoto.objects.create(user=self.user, photo=self.photo)
        response = self.client.get(reverse('photos:add_to_favorites', args=[self.photo.id]))

        # Check that adding an existing favorite doesn't create a new one
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('photos:photo_detail', args=[self.photo.id]))
        favorites_count = FavoritePhoto.objects.filter(user=self.user, photo=self.photo).count()
        self.assertEqual(favorites_count, 1)

class RemoveFromFavoritesViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.photo = Photo.objects.create(title="Test Photo", image="test.jpg")
        self.favorite = FavoritePhoto.objects.create(user=self.user, photo=self.photo)

    def test_remove_from_favorites_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('photos:remove_from_favorites', args=[self.favorite.id]))
        self.assertEqual(response.status_code, 302)  # Should be a redirect
        self.assertEqual(response.url, reverse('photos:photo_detail', args=[self.photo.id]))

        # Check if the photo was removed from favorites
        favorite = FavoritePhoto.objects.filter(user=self.user, photo=self.photo)
        self.assertFalse(favorite.exists())