## 1. build app-backend
docker image build -f  Dockerfile_frontend . -t app-frontend

## 2. create app-backend-8082 container
docker container create  -p 8081:9001   --name w1-8081  app-frontend