03_建立VM建立快照 - 把自己的系統克隆
==============================

## 知識點

* 在VM安裝必要的軟件包
* 打包VM 成快照
* 以快照建立的VM

## 實戰演習

### 在Amazon安裝必要的軟包

+ Docker
+ Node.js
+ Git
+ nano
+ nmap

```bash


$ sudo apt update
$ sudo apt upgrade

#########################################
# 安裝Node.js
$ curl -sL https://rpm.nodesource.com/setup_12.x | sudo bash -
$ sudo apt install   nodejs
$ node -v

# 安裝Git
$ sudo apt install  git -y
$ git version

# 安裝 Git SSH KEY -> 將id_rsa.pub 貼到GITHUB中
$ cd ~/.ssh
$ ssh-keygen -t rsa -C"blackjtsai@gmail.com"


# 可選安裝nmap
$ sudo apt install nmap -y

# 安裝 **nano**
$ sudo apt install nano

# 安裝 Docker
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ DRY_RUN=1 sudo sh ./get-docker.sh

# 修改docker 附加組給 ec2-user
$ sudo usermod $USER -aG docker

# OS重新啟動
$ docker version

# 安裝Docker-compose
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ docker-compose version


```
### 將系統打包成 快照

+ Name : vm-snap

### 從 vm-snap 啟動我們的實例


