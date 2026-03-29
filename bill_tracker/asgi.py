import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bill_tracker.settings')

# 👇 ADD THIS BLOCK
import django
django.setup()

from django.core.management import call_command

try:
    call_command('migrate')
except Exception:
    pass

# 👇 existing
application = get_asgi_application()