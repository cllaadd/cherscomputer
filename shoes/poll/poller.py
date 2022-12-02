import django
import os
import sys
import time
import json
import requests
import json

from api.shoes_rest.models import BinVO

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoes_project.settings")
django.setup()

# Import models from hats_rest, here.
# from shoes_rest.models import Something


def get_bins():
    response = requests.get("http://wardrobe:8100/api/bins/")
    content = json.loads(response.content)
    for binVO in content["bins"]:
        BinVO.objects.update_or_create(
            import_href=binVO["href"],
            defaults={
                "closet_name": binVO["closet_name"]
                    "bin_number":binVO["bin_number"],
                    "bin_size":binVO["bin_size"],
            }
        )


def poll():
    while True:
        print('Shoes poller polling for data')
        try:
            get_bins()
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(60)


if __name__ == "__main__":
    poll()
