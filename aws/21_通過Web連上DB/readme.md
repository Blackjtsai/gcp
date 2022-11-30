21_通過Web連上DB --Web 安裝 phpMyadmin
======================================

## 知識點

* Web端 安裝docker phpMyadmin


## 實戰演習

### Web端( blackjtsai-web-1a)

```bash
$ ssh -i ./xxxxx.pem 172.16.20.10

# phpmyadmin image pull , run
$ docker pull phpmyadmin
$ docker run --name phpmyadmin -d -e PMA_HOST=54.178.50.10 -p 8083:80 phpmyadmin

# 更新phpMyadmin 匯入檔案資料大小
# 訪問您的 phpmyadmin docker 容器：docker exec -it [container name or is] bash
$ docker exec -it phpmyadmin bash
$ cd /usr/local/etc/php/conf.d/
$ nano nano phpmyadmin-misc.ini

---------------------------
allow_url_fopen=Off
max_execution_time=${MAX_EXECUTION_TIME}
max_input_vars=10000
memory_limit=128M
post_max_size=20M
upload_max_filesize=20M
```





