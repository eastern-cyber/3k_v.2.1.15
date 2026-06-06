#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

# Load .env file at the very beginning
try:
    from environ import Env
    env = Env()
    env_file = Path(__file__).resolve().parent / '.env'
    if env_file.exists():
        # Use env.read_env() directly
        env.read_env(str(env_file))
        print(f"✓ Loaded environment variables from {env_file}")
    else:
        print(f"⚠ No .env file found at {env_file}")
except ImportError:
    print("⚠ django-environ not installed, skipping .env loading")
except Exception as e:
    print(f"⚠ Error loading .env: {e}")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
