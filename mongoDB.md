#ubuntu环境下安装
#启动
```sudo mongod --dbpath /var/lib/mongodb/ --logpath /var/log/mongodb/mongo.log --logappend &```
 


##启动目录
```
/user/bin/mongod
```
##docker  
环境基于python安装配置mongo数据库
dockerhub中 基于lyy00/mongo_env
##win10 mongo 服务器开启  
```
c:\Program Files\MongoDB\Server\5.0\bin\mongod -dbpath c:\data\db
```
#如果不能启动
```修复
mongod --repair
``` 
#常用命令       
```
sudo systemctl status mongodb 
sudo systemctl stop mongodb 
sudo systemctl start mongodb 
sudo systemctl restart mongodb
```
    