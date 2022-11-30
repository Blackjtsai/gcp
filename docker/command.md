
-----------------------------------------基本指令------------------------------
# docker 基本指令

docker image pull hello-world
docker run -d -p 80:8000 docker/getting-started

## container
docker container run -it ubuntu bash
docker container ls
docker container stop 310dc5acd52f
docker container rm 310dc5acd52f

## image
docker image ls
docker image build -t pyramid-app  .
docker image build . -t pyramid-app
docker build . -t pyramid-app
docker build . --tag pyramid-app
docker image rm ubuntu

# 指定Dockerfile
docker image build -f  Dockerfile.test -t image-train-test .



---------------------------------從0-1 教學  建立 net6 web 使用 image ----------------------------------------------------------------------------------

# 第一種方式 指定Dockerfile 建立 疊層image 來使用
## 1. 先取ubuntu
docker image pull ubuntu
## 2. 新增Dockerfile_net6sdk Dockerfile執行文本
FROM ubuntu
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install dotnet6
## 3. build net6sdk image
docker image build -f  Dockerfile_net6sdk . -t net6sdk


## 4. 建立 web Dockerfile 執行文本
FROM net6sdk
WORKDIR /home/P3_Web_P
COPY ./P3_Web_P ./
ENTRYPOINT [ "dotnet","P3_Web.dll" ,"--urls" , "http://0.0.0.0:80"]

## 5. build web_8081 image
docker image build -f  Dockerfile_web . -t web

## 6. create web_8081 container
docker container create  -p 8081:80 -p 8082:81  --name u8081 web

docker container create  -p 8082:80  --name u8082 web

--------------------------------------從0-1 教學  建立 net6 web 使用 image 使用 原始  ------------------------------------------------

# 原始方式 指定Dockerfile 建立 疊層image 來使用
## 從0開始建立ubuntu 與 安裝 dotnet6Sdk 進而開佈建AP RUN
docker image pull ubuntu
docker run -it  --name u1 -p 8080:8080 ubuntu bash
exit
docker start u1
docker exec -it u1 bash

## 更新apt
apt update
apt upgrade

## 安裝 .net6
apt-get install -y dotnet6
exit

## 將程式碼放置u1目錄
docker cp ./P3_Web_P u1:/home

## 進入u1
docker exec -it u1 bash
cd P3_Web_P
ls
dotnet P3_Web.dll --urls http://0.0.0.0:8080

## commit
docker commit -m ".netcore_web" u1  p3_web:v1

## 建立container
docker run -it  --name u2 -p 8081:8080 p3_web:v1 bash
## 啟動u2
進入 /home/P3_Web_P
dotnet P3_Web.dll --urls http://0.0.0.0:8080


--------------------------------- 參考  ----------------------------------

# 參考
# https://www.youtube.com/watch?v=BLBC-7sRJq4

# 安裝 Flask 套件
+ pip install Flask

# 步驟二 : 將以下代碼存檔為 app.py
```
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World!"
```
# 步驟三 : 終端機指令執行
```
$ flask run
```

