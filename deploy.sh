#!/bin/bash

APP_DIR="/home/ubuntu/my_app"
COMPOSE_FILE="/home/ubuntu/my_app/docker-compose.yml"

# 최신 코드 pull
cd $APP_DIR
git pull

# Docker Compose로 컨테이너 재시작
# -d: 백그라운드에서 실행
# --build: Dockerfile을 사용하여 이미지 재빌드
sudo docker-compose -f $COMPOSE_FILE down
sudo docker-compose -f $COMPOSE_FILE up -d --build