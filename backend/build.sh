#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. Compile static assets safely
# We pass the dummy string inline ONLY for collectstatic so it doesn't touch your real env
DATABASE_URL="postgres://dummy:dummy@localhost:5432/dummy" python manage.py collectstatic --no-input

# 3. Run live migrations against your actual Render database
python manage.py migrate
