#!/usr/bin/env bash

pipenv lock -r  > requirements.txt

docker image build -f Dockerfile -t flask_app_demo:latest .