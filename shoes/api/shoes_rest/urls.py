from django.urls import path
from .views import api_shoe, api_shoes

urlpatterns = [
    path("shoes/", api_shoes, name="api_create_shoes"),
    path(
        "bins/<int:bin_vo_id>/shoes/",
        api_shoes,
        name="api_shoes",
        ),
    path("shoes/<int:id>/", api_shoe, name="api_shoes"),
]
