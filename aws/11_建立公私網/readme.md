11_建立公司網 - 公私分明才能網路安全
================================

## 知識點

+ 建立公有網段
+ 建立私有網段

## 官網

https://docs.aws.amazon.com/zh_tw/vpc/latest/userguide/configure-subnets.html

## 實戰演習


### 子網所需VPC

+ blackjlearnaws-vpc
  + 先使用建構一個AZ，多個AZ日後說明


### 公開網路

主要用於對外服務器，如 Web ，API 服務器。

+ 設定
  + 標籤建立：blackjlearnaws-web-1a
  + 可用區域；ap-northeast-1a
  + 網段決定；172.16.10.0/24

### 私有網路

主要用於內部使用的服務器，如 DB，Redis等

+ 設定
  + 標籤建立：blackjlearnaws-db-1a
  + 可用區域；ap-northeast-1a
  + 網段決定；172.16.20.0/24



