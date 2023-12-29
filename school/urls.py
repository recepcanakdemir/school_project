from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.index, name="index"),
    path("ogrenci_ekle", views.ogrenci_ekle, name="ogrenci_ekle"),
    path("edit/<int:student_id>", views.edit, name="edit"),
    path("sil/<int:student_id>", views.sil, name="sil"),
]
