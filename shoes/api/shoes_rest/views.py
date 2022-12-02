from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import Shoe, BinVO


class BinVOEncoder(ModelEncoder):
    model = BinVO
    properties = ["closet_name", "bin_number", "bin_size"]

class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = ["id","manufacturer","color","model_name"]

class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "id",
        "manufacturer",
        "color",
        "model_name",
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
        content = json.loads(request.body)
        shoe = Shoe.objects.create(**content)
        return JsonResponse(
            shoe,
            encoder=ShoeDetailEncoder,
            safe=False,
        )

@require_http_methods(["GET","DELETE"])
def api_show_shoe(request,id):
    if request.method == "GET":
        try:
            shoe = Shoe.objects.get(id=id)
            return JsonResponse(
                shoe,
                encoder=ShoeDetailEncoder,
                safe=False
            )
        except Shoe.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
    else:
        count, _ = Shoe.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
