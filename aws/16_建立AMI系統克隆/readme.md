16_建立AMI -   把自己的系統克隆
==============================

## 知識點

* 在Amazon linux 2 上安裝必要的軟件包
* 打包Amazon linux 2 成AMI ( Amazon Machine Image )
* 以AMI啟動我們的EC2實例

## 官網

https://docs.aws.amazon.com/zh_tw/AWSEC2/latest/UserGuide/AMIs.html

## 實戰演習

### 在Amazon安裝必要的軟包

+ Docker
+ Node.js
+ Git

```bash

##################################################
# Amazon Linux 2
$ ssh -i ./blackjlearnaws-ssh-key.pem ec2-user@13.114.59.147
$ ssh -i ~/.ssh/blackjlearnaws-ssh-key.pem ec2-user@13.114.59.147
##################################################
# 安全登入訊息
$ touch .hushlogin
# 系統包升級
$ sudo yum update -y
# 確認系統包版本
$ cat /etc/os-release
###################################################
# Docker
$ sudo amazon-linux-extras list
$ sudo amazon-linux-extras install -y docker
# 修改docker 附加組給 ec2-user
$ sudo usermod -a -G docker ec2-user
$ docker version
# 啟動Docker服務
$ sudo systemctl start docker
# 確認docker運行
$ ps aux|grep docker
# 註冊Docker 服務
$ sudo systemctl enable docker
# 安裝Docker-compose
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ docker-compose version

#########################################
# 安裝Node.js
$ curl -sL https://rpm.nodesource.com/setup_12.x | sudo bash -
$ sudo yum install -y gcc-c++ make
$ sudo yum install -y nodejs
$ node -v

###########################################
# 安裝Git
$ sudo yum install  git -y
$ git version
# 可選安裝nmap
$ sudo yum install nmap -y
############################################
## exec 入 container 安裝 nano
$ apt-get update
$ apt-get upgrade
$ apt install nano
$ nano filename.xx
# OS重新啟動
$ sudo init 0
# $ sudo reboot
>
```
### 將系統打包成AMI

+ Name : blackjlearnaws-ami

### 從 AMI 啟動我們的實例

+ 參閱1603
