#!/usr/bin/env bash

docker-compose run surveyor python manage.py loaddata /dev_data/surveyor/sites.yaml
docker-compose run surveyor python manage.py loaddata /dev_data/surveyor/auth.yaml
docker-compose run surveyor python manage.py loaddata /dev_data/surveyor/surveys.yaml
