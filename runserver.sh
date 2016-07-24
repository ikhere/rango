#!/bin/bash

# Add /code folder to PYTHONPATH
export PYTHONPATH=/code:$PYTHONPATH

# Hack; will help web service to wait for db service.
sleep 10

# Enable this to make new migrations
python manage.py makemigrations

# Apply the migrations
python manage.py migrate

# Create superuser
python manage.py initadmin

# Start django server on port 8000
python manage.py runserver 0.0.0.0:8000

# Populate Rango database
# NOTE: Disable once you've populated it
# python populate_rango.py