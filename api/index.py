import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

os.environ["DJANGO_SETTINGS_MODULE"] = "bill_tracker.settings"

import django
django.setup()

from django.core.asgi import get_asgi_application

application = get_asgi_application()