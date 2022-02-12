#安装
#构建
    docker build -t test:v1 .  
#运行
    docker run -d -p 5000:5000 --name test test:v1
#注意
docker push 需要先对镜像进行标记   
docker tag test:v1 lyy007/test:v1   
docker push lyy007/test:v1  
#常用命令地址
[菜鸟教程](https://www.runoob.com/docker/docker-container-usage.html)