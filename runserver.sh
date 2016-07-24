#!/bin/bash

export PYTHONPATH=/code;$PYTHONPATH

sleep 10	# Hack; will help web service to wait for db service.
python manage.py migrate
python manage.py initadmin
python manage.py runserver 0.0.0.0:8000