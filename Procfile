web: gunicorn config.wsgi:application
worker: celery worker --app=aphids_api.taskapp --loglevel=info
