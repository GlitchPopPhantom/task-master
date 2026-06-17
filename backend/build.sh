#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. CRITICAL FIX: Inject a temporary dummy fallback URL right here 
# so Django can compile static assets without needing your live database.
export DATABASE_URL="postgres://dummy:dummy@localhost:5432/dummy"

# 3. Compile static assets safely
python manage.py collectstatic --no-input

# 4. Remove or unset the dummy variable so the runtime container 
# uses your real production Render/Supabase variables instead.
unset DATABASE_URL

# 5. Run live migrations (This runs once the app transitions to live mode)
python manage.py migrate
