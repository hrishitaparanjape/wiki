from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_name>/", views.entry, name="entry"),
    path("create/", views.create_entry, name="create_entry"),
    path("edit/<str:title>/", views.edit_entry, name="edit_entry"),
    path("random/", views.random_entry, name="random_entry")
]
