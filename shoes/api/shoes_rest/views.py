from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .acls import get_photo
import json

from common.json import ModelEncoder
from .models import Shoe, BinVO


class BinVODetailEncoder(ModelEncoder):
    model = BinVO
    properties = ["closet_name", "bin_number", "bin_size", "import_href",]

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
        "bin",
    ]
    encoders = {
        "bin" : BinVODetailEncoder(),
    }


@require_http_methods(["GET","POST"])
def api_shoes(request, bin_vo_id=None):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        return JsonResponse(
            {"shoes": shoes},
            encoder=ShoeListEncoder,
        )
    else:
        content = json.loads(request.body)
        photo = get_photo(content["color"], content["manufacturer"], content["model_name"])
        content.update(photo)

        try:
            bin_href = f"/api/bins/{bin_vo_id}/"
            binVO = BinVO.objects.get(import_href=bin_href)
            content["bin"] = binVO
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin id"},
                status=400,
            )

        shoe = Shoe.objects.create(**content)
        return JsonResponse(
            shoe,
            encoder=ShoeDetailEncoder,
            safe=False,
        )

@require_http_methods(["GET","DELETE"])
def api_shoe(request,id):
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
