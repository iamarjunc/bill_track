import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bill_tracker.settings")

from django.core.asgi import get_asgi_application

application = get_asgi_application()   # ✅ THIS LINE FIXED