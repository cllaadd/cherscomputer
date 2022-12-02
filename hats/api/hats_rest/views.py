from django.shortcuts import render
from common.json import ModelEncoder
from .models import LocationVO, Hat
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json

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
        "fabric",
        "style",
        "color"
    ]

@require_http_methods(["GET", "POST"])
def api_hats(request, location_vo_id=None):
    if request.method == "GET":
        if location_vo_id == None:
            hats = Hat.objects.all()
        else:
            hats = Hat.objects.filter(location=location_vo_id)
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
                status=400,
            )

        hat = Hat.objects.create(**content)
        return JsonResponse(
            hat,
            encoder = HatDetailEncoder,
            safe=False,
        )

@require_http_methods("GET", "DELETE")
def api_hat(request, id):
    if request.method == "POST":
        hat=Hat.objects.get(id=id)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )
    else:
        count, _ = Hat.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
