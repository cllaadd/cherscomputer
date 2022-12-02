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
    url = "http://wardrobe:8100/api/bins/"
    response = requests.get(url)
    content = json.loads(response.content)
    for binVO in content["bin"]:
        BinVO.objects.update_or_create(
            import_href=binVO["href"],
            defaults={"name": binVO["name"]},
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
