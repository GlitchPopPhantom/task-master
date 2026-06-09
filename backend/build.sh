#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# This command creates your database tables in the cloud
python manage.py migrate
