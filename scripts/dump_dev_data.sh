#!/usr/bin/env bash

docker-compose run surveyor python manage.py dumpdata --format yaml sites -o /dev_data/surveyor/01_sites.yaml
docker-compose run surveyor python manage.py dumpdata --format yaml auth -o /dev_data/surveyor/02_auth.yaml
docker-compose run surveyor python manage.py dumpdata --format yaml survey -o /dev_data/surveyor/03_surveys.yaml
