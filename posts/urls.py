from django.urls import path
from .views import (sticky_list, sticky_details, sticky_create,
                    sticky_update, sticky_delete)

urlpatterns = [
    path('', sticky_list, name='sticky_list'),
    path("sticky/<int:pk>/", sticky_details, name="sticky_details"),
    path("sticky/new/", sticky_create, name="sticky_create"),
    path("sticky/<int:pk>/edit/", sticky_update, name="sticky_update"),
    path("sticky/<int:pk>/delete/", sticky_delete, name="sticky_delete"),
]
