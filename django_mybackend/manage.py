#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import json
import os
import sys

from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_my_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def success(data=None, msg='成功'):
    return HttpResponse(json.dumps({"code": 0, "msg": msg, "data": data}))


def error(msg='失败'):
    return HttpResponse(json.dumps({"code": 500, "msg": msg, "data": None}))


@ensure_csrf_cookie
def get_csrf_token(request):
    token = get_token(request)
    return success({"token": token})


if __name__ == '__main__':
    main()
