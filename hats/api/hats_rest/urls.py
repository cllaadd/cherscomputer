from django.urls import path
from .views import api_hat, api_hats

urlpatterns = [
    path(
        "locations/<int:location_vo_id>/hats/",
        api_hats,
        name="api_hats",
        ),
    path("hats/<int:id>/", api_hat, name="api_hat"),
]
