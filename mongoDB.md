# ubuntu环境下安装
# 启动
```
sudo mongod --dbpath /var/lib/mongodb/ --logpath /var/log/mongodb/mongo.log --logappend &
```
 


## 启动目录
```commandline
cd /user/bin/mongod
```
## docker  
环境基于python安装配置mongo数据库
dockerhub中 基于lyy00/mongo_env
## win10 mongo 服务器开启  
```
c:\Program Files\MongoDB\Server\5.0\bin\mongod -dbpath c:\data\db
```
# 如果不能启动
```commandline
mongod --repair
``` 
# 常用命令       
```commandline
sudo systemctl status mongodb 
sudo systemctl stop mongodb 
sudo systemctl start mongodb 
sudo systemctl restart mongodb
```
# 设置用户验证
[验证设置流程](https://www.cnblogs.com/swordfall/p/10841418.html)
# docker mongo挂载目录
```commandline
docker run --name some-mongo -v /my/own/datadir:/data/db -d mongo
```
```
use admin
db.createUser({user: "myUserAdmin", pwd: 105014, roles: [{ role: "userAdminAnyDatabase", db: "admin" },{ role: "readWriteAnyDatabase", db: "admin" }]}
use admin
db.auth("","")
db.createUser({})
```

```commandline
docker network create -d bridge mynetwork
docker network connect --alias mongoAuth mynetwork mongoAuth
docker network inspect mynet
docker network connect --alias test mynetwork test

```
[设置参考](https://www.cnblogs.com/sz-wenbin/p/11010403.html)