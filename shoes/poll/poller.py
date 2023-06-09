import django
import os
import sys
import time
import json
import requests
import json

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoes_project.settings")
django.setup()

from shoes_rest.models import BinVO


def get_bins():
    response = requests.get("http://wardrobe-api:8000/api/bins/")
    content = json.loads(response.content)
    for binVO in content["bins"]:
        BinVO.objects.update_or_create(
            import_href=binVO["href"],
            defaults={
                "closet_name": binVO["closet_name"],
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
