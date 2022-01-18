1.已经添加进supervvisor  
2.修改后使用sudo supervisorctl restart  
3.配置文件放在/etc/supervisor/conf.d/test.conf  
4.构建命令 docker build -t test:v1 .  
5.运行命令docker run -d -p 5000:5000 --name test test:v1  
6.docker push 需要先对镜像进行标记  docker tag test:v1 lyy007/test:v1 docker push lyy007/test:v1