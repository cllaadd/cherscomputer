from django.shortcuts import render
from common.json import ModelEncoder
from .models import LocationVO, Hat
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
# from .acls import get_photo

class LocationVODetailEncoder(ModelEncoder):
    model = LocationVO
    properties = [
        "closet_name",
        "section_number",
        "shelf_number",
        "import_href"
        ]

class HatDetailEncoder(ModelEncoder):
    model = Hat
    properties = [
        "id",
        "fabric",
        "style",
        "color",
        "picture_url",
        "location",
    ]
    encoders = {
        "location": LocationVODetailEncoder(),
    }


class HatListEncoder(ModelEncoder):
    model = Hat
    properties = [
        "id",
        "fabric",
        "style",
        "color",
        "picture_url",
        "location",
    ]
    encoders = {
        "location": LocationVODetailEncoder(),
    }


@require_http_methods(["GET", "POST"])
def api_hats(request, location_vo_id=None):
    if request.method == "GET":
        if location_vo_id == None:
            hats = Hat.objects.all()
        else:
            location_href = f"/api/locations/{location_vo_id}/"
            # location = LocationVO.objects.get(import_href=location_href)
            locations = LocationVO.objects.filter(import_href=location_href)
            if len(locations) == 0:
                return JsonResponse(
                    {"message": "invalid location id"}
                )

            hats = Hat.objects.filter(location=location)
        return JsonResponse(
            {"hats": hats},
            encoder = HatListEncoder,
        )
    else:
        content = json.loads(request.body)

        try:
            location_href = f"/api/locations/{location_vo_id}/"
            location = LocationVO.objects.get(import_href=location_href)
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location id"},
                status=404,
            )

        hat = Hat.objects.create(**content)
        return JsonResponse(
            hat,
            encoder = HatDetailEncoder,
            safe=False,
        )

@require_http_methods(["GET", "DELETE"])
def api_hat(request, id):
    if request.method == "GET":
        #validation
        hat=Hat.objects.get(id=id)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )
    else:
        count, _ = Hat.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
