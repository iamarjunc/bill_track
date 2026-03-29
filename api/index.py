import os
import sys

# Add project root to path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bill_tracker.settings")

# 🔥 IMPORTANT: initialize Django first
import django
django.setup()

# Then load ASGI
from django.core.asgi import get_asgi_application

application = get_asgi_application()