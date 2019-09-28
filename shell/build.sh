#!/usr/bin/env bash

# 更新依赖到 requirements.txt
pipenv lock -r  > requirements.txt
# 构建镜像
docker image build -f Dockerfile -t flask_app_demo:latest .