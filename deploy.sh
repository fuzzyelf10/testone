#!/bin/sh

docker build -t test-app .
docker stop my-test-app
docker rm my-test-app
docker run --restart=always -p 80:5000 -d --name my-test-app test-app:latest