"""
WSGI config for _core project.
"""

import os
import sys
from pathlib import Path

# Load .env file manually for web app
env_file = Path(__file__).resolve().parent.parent / '.env'
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_core.settings')

application = get_wsgi_application()
