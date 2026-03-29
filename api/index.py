import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bill_tracker.settings")

from django.core.asgi import get_asgi_application

app = get_asgi_application()