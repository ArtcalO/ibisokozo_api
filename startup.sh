#!/bin/bash
python manage.py collectstatic && gunicorn --workers 2 ibisokozo_api.wsgi