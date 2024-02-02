python manage.py makemigrations
python manage.py migrate
gunicorn picasso_test.wsgi:application --bind 0:8000