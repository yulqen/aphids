#!/usr/bin/env bash

SETTINGS='--settings=aphids_api.settings.staging'

teardown() {
    echo "Initialising staging on Heroku..."
    heroku config:set DJANGO_SETTINGS_MODULE=aphids_api.settings.staging
    heroku run ./scripts/initialise.sh
    heroku run ./manage.py makemigrations
    heroku run ./manage.py migrate
    heroku run ./manage.py populate
}

if [ "$1" == "--teardown" ];
then
    teardown
else
    heroku config:set DJANGO_SETTINGS_MODULE=aphids_api.settings.staging
    heroku ps:scale web=0
    heroku ps:scale web=1
fi
