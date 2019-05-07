#!/usr/bin/env bash
echo '>>>>>>>当前目录：'
pwd
echo '>>>>>>>开始删除已存在的 migrations 目录...'
rm -rf ../migrations
echo '>>>>>>>删除成功'
echo '>>>>>>>开始迁移数据库...'
python ../startup.py db init
python ../startup.py db migrate
python ../startup.py db upgrade
echo '>>>>>>>迁移结束，开始启动服务...'
python ../startup.py runserver -h 0.0.0.0 -p 10001 -d