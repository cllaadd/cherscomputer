from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import Shoe, BinVO

class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = ["id","manufacturer","color","model_name"]

class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "manufacturer",
        "color",
        "model_name",
        "picture_url",
    ]


@require_http_methods(["GET","POST"])
def api_list_shoes(request):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        return JsonResponse(
            {"shoes": shoes},
            encoder=ShoeListEncoder,
        )
    else:
        return JsonResponse(
                {"message": "Did not work"},
                status=400,
            )
