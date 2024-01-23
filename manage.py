#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def get_x(r): 
    return image_path/r['train_image_name']

def get_y(r): 
    return r['class']

def get_features(r): return image_path/r['image']

def get_output(r): return r['quality']


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diagnosisapp.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
