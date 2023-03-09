from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import NewPublication, EditPublication

urlpatterns = [
    path("newpublication/", NewPublication.as_view(), name="newpublication"),
    path("updatepublication/<int:pk>", EditPublication.as_view(), name="updatepublication"),
    path("deletepublication/<int:id>", views.deletepublication, name="delete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)