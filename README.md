## 1. 本地开发

#### 1.1 启动服务

```bash
python startup.py runserver -h 0.0.0.0 -p 10001 -d -r
```

#### 1.2 数据库自动初始化或迁移

```bash
sh shell/migrate.sh
```

## 2. 制作 Docker 镜像

```bash
sh shell/build.sh
```

## 3. docker-compose

####  3.1 启动镜像
```bash
cd deploy

docker-compose up -d
```

#### 3.2 数据库自动初始化或迁移

```bash
# 查看镜像 ID
docker ps | grep flask_app_demo

# 进入容器内部
docker exec -it $imageId /bin/bash

# 执行数据库迁移脚本
sh shell/build.sh
```

####  3.3 停止镜像

```bash
cd deploy

docker-compose down
```