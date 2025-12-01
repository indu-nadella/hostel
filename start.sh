python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn hostel_management_system.wsgi:application --bind 0.0.0.0:$PORT