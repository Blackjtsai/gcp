15_建立EC2實例 -- 開啟我們的雲端服務器之旅
=====================================

## 知識點

* 建立一個公網可訪問的EC2服務器實例

## 實戰演練

### EC2實例具體設置

+ blackjlearnaws-web-1a
+ Amazon Linux 2 AMI
+ t2.micro
+ blackjlearnaws-vpc
+ 自動分配公有IP
+ 內網IP:172.16.10.10/32
+ Name:blackjlearnaws-web1
+ 密鑰對: blackjlearnaws-ssh-key

### SSH連接

```bash
$ cp ~/Downloads/blackjlearnaws-ssh-key.pem ./
$ chmod 400 blackjlearnaws-ssh-key.pem

#Amazon Linux 2
$ ssh -i ./blackjlearnaws-ssh-key.pem ec2-user@3.112.45.44


```

