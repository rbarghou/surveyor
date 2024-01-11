#!/usr/bin/env bash

docker-compose exec surveyor ./manage.py generateschema > schema.yaml
