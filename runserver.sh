#!/bin/bash

# Add /code folder to PYTHONPATH
export PYTHONPATH=/code:$PYTHONPATH

# Hack; will help web service to wait for db service.
sleep 10

# Enable this to make new migrations
python manage.py makemigrations

# Enable this to squash the migrations
# python manage.py squashmigrations rango 0004 --noinput

# Apply the migrations
python manage.py migrate --noinput

# Create superuser
python manage.py initadmin

# Populate Rango database
# NOTE: Disable once you've populated it
python populate_rango.py

# Start django server on port 8000
python manage.py runserver 0.0.0.0:8000
