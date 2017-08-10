#!/usr/bin/env bash

echo "Launching heroku locally with specific settings..."
heroku local web -e aphids_api/settings/.heroku_env
