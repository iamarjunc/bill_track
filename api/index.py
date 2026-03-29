import os
import sys

# 👇 FIX PATH (IMPORTANT)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

# 👇 Correct settings path
os.environ["DJANGO_SETTINGS_MODULE"] = "bill_tracker.settings"

# 👇 Initialize Django
import django
django.setup()

# 👇 Load ASGI
from django.core.asgi import get_asgi_application

application = get_asgi_application()