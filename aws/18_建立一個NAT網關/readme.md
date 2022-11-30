18_部署一個DB應用 - 還不行，還差一步設置
======================================

## 知識點

* 建立DB私有網路安全組，開放3306-Mssql端口
* 在公開網路中建立NAT網關
* 建立DB私有網路路由表，設置NAT網關


## 實戰演習

> 看圖說話

### NAT網關

+ Name : blackjtsaiaws-web-nat
+ Subnet : blackjtsaiaws-web-1a
+ ELastic IP (收費的 要刪掉喔~)
  +  Elastic IP Address（Elastic IP Address，簡稱EIP），是可以獨立購買和持有的公網IP地址資源。目前，EIP可綁定到專用網路類型的ECS執行個體、專用網路類型的私網SLB執行個體和NAT Gateway上。  
  +  https://docs.aws.amazon.com/zh_tw/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html


### 安全組

+ Name : blackjlearnaws-db-sg
+ Port : 3306
## 路由表

+ Name : blackjlearnaws-db-rtb
+ Target : blackjlearnaws-web-nat -> 0.0.0.0/0


-----------------------------------------------
### NAT 類型

+ 網路位址轉換(英語：Network Address Translation，縮寫：NAT)是一種實現內網主機與外網通訊的方法，它會在IP封包通過路由器或防火牆時重寫來源IP地址或目的IP位址的技術，NAT在真實的網絡環境中隨處可見，

+ 主要是為了處理兩個問題：

  + IPv4地址不夠用，IP地址只有32位，最多能提供 2^32 組(42億)，NAT技術可讓本地的電腦設備，分享共同的公有IP位址
安全問題。
  + 使用NAT後，可以把主機隱藏在內網中，不會讓真實的IP位址曝露，防止遭到駭客入侵

+ 不過，NAT 也帶來一些缺點：
  + NAT設備會對封包進行修改，這樣就降低了傳輸的效率
  + 有的協議無法通過NAT，因此需要穿透技術來解決

---------------------------------------------------------