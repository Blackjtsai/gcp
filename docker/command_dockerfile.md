# 最底層的鏡像從docker那邊取
FROM python:3.7

# COPY . (.指當前所有的) the app code  到 docker 底層的 /app (沒有他會自建)
COPY . /app 

# 之後運型的指令都在這個路徑
WORKDIR /app


# install 依賴
RUN pip install -r requirement.txt 

# Expose server's port
EXPOSE 5000

# RUN the server
ENTRYPOINT [ "python3","pyramid.py" ]
CMD ["5"]