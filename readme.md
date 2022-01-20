1.已经添加进supervvisor  
2.修改后使用sudo supervisorctl restart  
3.配置文件放在/etc/supervisor/conf.d/test.conf  
4.构建命令 docker build -t test:v1 .  
5.运行命令docker run -d -p 5000:5000 --name test test:v1  
6.docker push 需要先对镜像进行标记  docker tag test:v1 lyy007/test:v1 docker push lyy007/test:v1

7.mongo 服务器开启  
c:\Program Files\MongoDB\Server\5.0\bin\mongod -dbpath c:\data\db

suprevisor 服务  
1.安装  
ubuntu安装：   
sudo apt-get install supervisor   
centos安装：   
yum install -y supervisor   
基于python库安装  
pip2 install supervisor  
easy_install supervisor  
2.配置文件  
路径 ：/etc/supervisor/conf.d/  
文件内容：  
[program:task]                                       #管理进程的命名  
command=python test.py  -c test.conf　　　　　　　　　　#执行的命令  
stderr_logfile=/var/log/supervisor/test.log　　　　　　#错误日志输出路径  
stdout_logfile=/var/log/supervisor/test.log　　　　　　#日志输出路径  
directory=/root/test　　　　　　　　　　　　　　　　　　　 #命令执行的工作空间  
autostart=true　　　　　　　　　　　　　　　　　　　　　　　#自动启动  
user=ubuntu(注意用户权限)　　　　　　　　　　　　　　　　　　　　　　　　　　#指定用户  
autorestart=true　　　　　　　　　　　　　　　　　　　　　　#自动重启</pre>  
配置好后：  
supervisorctl reload  
基本命令：  
supervisorctl status #查看supervisorctl状态  
supervisorctl start nginx #启动子进程nginx  
supervisorctl stop nginx  #关闭子进程nginx  
supervisorctl restart nginx #重启子进程nginx  
docker  
环境基于python安装配置mongo数据库
dockerhub中 基于lyy00/mongo_env