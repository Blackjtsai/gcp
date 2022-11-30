13_建立供網路由表 -- 讓我們子網連接到互聯網
===========================================

## 知識點

* 理解路由表
* 建立路由表


## 官網

https://docs.aws.amazon.com/zh_tw/vpc/latest/userguide/VPC_Route_Tables.html

# 實戰演習


### 理解路由表

> 路由圖
> 建立VPC時候會自建一個VPC的路由 參考 1301 圖

### 建立路由表

+ RTB : blackjlearnaws-web-rbt
  * VPC: blackjlearnaws-vpc
  * Rule：加入 0.0.0.0/0 blackjlearnaws-igw
+ 把新的路由綁到 blackjlearnaws-web-1a 子網 (子網路開關設定)