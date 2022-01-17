1.已经添加进supervvisor  
2.修改后使用sudo supervisorctl restart  
3.配置文件放在/etc/supervisor/conf.d/test.conf  
4.构建命令 docker build -t test:v1 .  
5.运行命令docker run -d -p 5000:5000 --name test test:v1

