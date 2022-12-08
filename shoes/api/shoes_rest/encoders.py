from common.json import ModelEncoder
from .models import Shoe, BinVO

class BinVODetailEncoder(ModelEncoder):
    model = BinVO
    properties = ["closet_name", "bin_number", "bin_size", "import_href",]

class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = ["id","manufacturer","color","model_name","bin"]
    encoders = {
        "bin" : BinVODetailEncoder(),
    }

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