#安装
```
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
#构建
```commandline
docker build -t test:v1 . 
```
     
#运行
```commandline
docker run -d -p 5000:5000 --name test test:v1
```    
#注意
docker push 需要先对镜像进行标记   
docker tag test:v1 lyy007/test:v1   
docker push lyy007/test:v1  
#常用命令地址
[菜鸟教程](https://www.runoob.com/docker/docker-container-usage.html)