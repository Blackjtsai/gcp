## 1. build app-backend
docker image build -f  Dockerfile_backend . -t app-backend

## 2. create app-backend-8081 container
docker container create  -p 8082:9002   --name w2-8082 app-backend