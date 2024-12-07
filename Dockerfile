# 使用之前构建的 python-node-base 镜像作为基础镜像
FROM python-node-base:3.9

# 设置工作目录
WORKDIR /

# 复制依赖文件
COPY ./requirements.txt /requirements.txt

# 修改 pip 源为清华源并安装依赖
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --no-cache-dir -r requirements.txt

# 设置时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 复制整个项目到容器
COPY . /

# 使用 Python 启动服务
CMD ["python", "app.py"]
