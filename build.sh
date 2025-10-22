#!/usr/bin/env bash
# Exit immediately if a command fails
set -o errexit

# On Linux (Render), ensure persistent media folder exists
mkdir -p /mnt/media

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
