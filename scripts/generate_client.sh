#!/usr/bin/env bash
# This uses openapi-generator to generate a client
# However, recent versions of openapi-generator seem to have a difficult time
# with token authentication.  So this is no longer the recommended approach.

docker run --rm -v "$(pwd):/local" \
    openapitools/openapi-generator-cli:v7.1.0 \
    generate \
    -i /local/schema.yaml \
    -g python \
    --package-name surveyor_client \
    -o /local/client

