from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Profile, ViewProfile, ViewPublication, UpdateProfile

urlpatterns = [
    path("inicio/", views.index, name="index"),
    path("profile/", Profile.as_view(), name="profile"),
    path("viewprofile/<int:id>", views.ViewProfile, name="viewprofile"),
    path("viewpublication/<int:pk>", ViewPublication.as_view(), name="viewpublication"),
    path("updateprofile/<int:pk>", UpdateProfile.as_view(), name="updateprofile"),
    path("follow/<int:id>/", views.follow, name="follow"),
    path("unfollow/<int:id>/", views.unfollow, name="unfollow"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)