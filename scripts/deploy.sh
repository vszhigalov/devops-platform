#!/bin/bash

set -e

cd ~/apps/devops-platform

docker compose -f docker-compose.prod.yml pull

docker compose -f docker-compose.prod.yml up -d

docker compose -f docker-compose.prod.yml exec -T backend alembic upgrade head
