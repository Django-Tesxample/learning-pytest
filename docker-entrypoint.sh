#!/bin/bash

echo "Entrypoint"

#python manage.py migrate                          # Apply database migrations
python manage.py collectstatic --clear --noinput  # clearstatic files
python manage.py collectstatic --noinput          # collect static files

# Prepare log files and start outputting logs to stdout
touch /data/logs/gunicorn.log
touch /data/logs/access.log

tail -n 0 -f /data/logs/*.log &
# echo Starting nginx

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn situr.wsgi:application \
    -b 0.0.0.0:8000
    --name app \
    --workers=5 --threads=2 \
    --log-level=info \
    --log-file=/data/logs/gunicorn.log \
    --access-logfile=/data/logs/access.log &
#exec service nginx start