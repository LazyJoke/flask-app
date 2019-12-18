## 1. 本地开发

> 环境依赖
> Python 3.7.5

#### 1.1 启动服务

```bash
# 进入当前项目根目录
cd yourprojectdir
# 安装 pipenv
pip install pipenv
# 创建虚拟环境, 并安装依赖
pipenv install
# 启动服务  -m: 'dev'、'prod'
export ROOT_DIR=$(pwd)/app && python startup.py -H 0.0.0.0 -P 10001 -M dev
```

#### 1.2 执行测试

```bash
# 进入当前项目根目录
cd yourprojectdir
# 执全部测试
export ROOT_DIR=$(pwd)/app && python test.py
```

#### 1.3 数据库自动初始化或迁移

```bash
sh shell/migrate.sh
```

#### 1.4 swagger UI

服务启动后，在浏览器访问 `http://127.0.0.1:10001/ui`，即可查看所有的 `API` 文档

## 2. 制作 Docker 镜像

```bash
sh shell/build.sh
```

## 3. docker-compose 启动

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
sh shell/migrate.sh
```

####  3.3 停止镜像

```bash
cd deploy

docker-compose down
```
