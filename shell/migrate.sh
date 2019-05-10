#!/usr/bin/env bash
echo '>>>>>>>当前目录：'
pwd
echo '>>>>>>>开始迁移数据库...'
python ../startup.py db init
python ../startup.py db migrate
python ../startup.py db upgrade
echo '>>>>>>>迁移结束...'
