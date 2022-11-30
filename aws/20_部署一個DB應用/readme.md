部署一個DB應用 -- MySQL+ phpMyadmin 我來了
===========================

## 知識點

* 在私有網段中安裝 MySQL@Docker
* 在私有網段安裝 phpMyadmin
* 在公有網段中連接MSQL數據實例

## 實戰演習

### 數據庫端( blackjtsai-db-1a)



```bash
$ ssh -i ./xxxxx.pem 172.16.20.10

# mysql image pull
$ docker pull mysql:5.7.40
$ docker run --name mysql -e MYSQL_ROOT_PASSWORD=eason821 -p 3306:3306 --restart=always mysql
$ docker ps

# 進入容器bash-shell 測試
docker exec -it mysql bash -p
>mysql -u root -p -h 127.0.0.1
mysql> show databases;
mysql> exit;

# phpmyadmin image pull , run
$ docker pull phpmyadmin
$ docker run --name phpmyadmin -d --link mysql:db -p 8083:80 phpmyadmin

```


#### 201_mariadb
===============

```bash
$ docker pull mariadb:10.8
$ docker run --detach --name mariadb -p 3306:3306 --env MARIADB_USER=blackjtsai --env MARIADB_PASSWORD=eason821 --env MARIADB_ROOT_PASSWORD=eason821  mariadb:latest

```
