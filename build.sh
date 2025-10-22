#!/usr/bin/env bash
set -o errexit

# Ensure persistent media folder exists on Render
mkdir -p /mnt/media

# Upgrade pip & install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
