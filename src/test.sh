#!/bin/bash

python ./manage.py migrate

pip install -r test_requirements.txt

mkdir -p artifacts
touch ./artifacts/testresults.txt

set -o pipefail
pytest | tee artifacts/testresults.txt
