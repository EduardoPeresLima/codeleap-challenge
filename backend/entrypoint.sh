#!/bin/bash
# entrypoint.sh

# Stop exection in case of error
set -e

echo "Running migrations..."
python manage.py migrate

echo "Starting Gunicorn..."
exec gunicorn codeleapChallenge.wsgi:application --bind 0.0.0.0:8000
