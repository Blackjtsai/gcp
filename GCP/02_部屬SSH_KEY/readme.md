02_部屬SSH_KEY --- 密要對
==========================================

## 產生一個新的密要對  id_rsa2

+ 看圖說話 0203
```
$ cd C:\Users\Blackjtsai\.ssh
$ ssh-keygen -t rsa
  id_rsa2
```

## 加密要對入GCP中繼資料區

+ 加 id_rsa2_pub 資料 入 中繼資料區中
+ 看圖說話 0201 / 0202



## VSCode 部屬 SSH連線資訊
+ C:\Users\Blackjtsai\.ssh\config
```
Host gcp-us-west-01
    HostName 34.168.144.33
    User blackjtsai
      IdentityFile ~/.ssh/id_rsa2
      IdentitiesOnly yes
```