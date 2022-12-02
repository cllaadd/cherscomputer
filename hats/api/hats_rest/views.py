from django.shortcuts import render
from common.json import ModelEncoder
from .models import LocationVO

class LocationVODetailEncoder(ModelEncoder):
    model = LocationVO
    properties = ["closet_name", "section_number", "shelf_number",]

class
