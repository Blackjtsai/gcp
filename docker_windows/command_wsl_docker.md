# 安裝windows Ubuntu
+ wsl --set-default-version 2
+ wsl --update
+ wsl --install -d Ubuntu

# 啟動
+ wsl

# 關閉
+ wsl --shutdown

# 安裝docker
+ curl -fsSL https://get.docker.com -o get-docker.sh
+ sudo usermod $USER -aG docker
+ sudo sh get-docker.sh

# 啟動 docker
+ sudo service docker start

# vscode 需要安裝 WSL 外掛remote
+ ctrl+shift + p
+ 指定 NEW WSLWINDOW USING Distro
+ 進入 Ubuntu
+ 進入後安裝加載Ubuntu的vscode  docker

# 更新apt
apt update
apt upgrade

# 安裝 .net6
apt-get install -y dotnet6

