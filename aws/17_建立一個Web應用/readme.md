17_建立一個Web應用 - 建立Node.js+Docker的應用程序
=================================================

## 知識點

* 部署一個Node.js的 Web應用
* 把應用通過 Docker(Hub)方式進行部屬
* 修改安全組，追加開放80端口

## 今後預定

+ 部署到 ECR + ECS
* ECR (DockerHub)
* ECS (容器管理服務)

## 實戰演習

> 圖解說明

### Docker Hub

+ blackjlearnaws-web

https://hub.docker.com/r/komavideo/deeplearnaws-wed

### 修改安全組，追加開放80端口
### 開啟EC2執行個體
```
$ ssh -i ./blackjlearnaws-ssh-key.pem ec2-user@52.197.4.192
( 公司電腦 改用 VSCode SSH 連線方式 )
```

### 操作步驟

```bash
# 從DockerHub上獲取deeplearnaws-web鏡像
$ docker image ls
$ docker pull komavideo/deeplearnaws-web:latest
$ docker run --name deeplearnaws-web -p 80:3000 -d  komavideo/deeplearnaws-web:latest

* nmap 127.0.0.1 (看開啟端口)
* docker exec -it deeplearnaws-web sh (進入container裡面編輯)

$ docker container ls -a
$ docker logs -f deeplearnaws-web
$ docker container stop deeplearnaws-web
$ docker container rm deeplearnaws-web
$ docker ps
```

