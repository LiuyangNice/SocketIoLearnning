#安装
1.安装  
ubuntu安装：
```commandline
sudo apt-get install supervisor
```
centos安装：
```commandline
yum install -y supervisor 
```
      
基于python库安装  
 ```commandline
pip2 install supervisor  
easy_install supervisor  
```        

#配置文件  
路径 ：
    /etc/supervisor/conf.d/  
文件内容：
```
[program:task]                                       #管理进程的命名  
command=python test.py  -c test.conf　　　　　　　　　　#执行的命令  
stderr_logfile=/var/log/supervisor/test.log　　　　　　#错误日志输出路径  
stdout_logfile=/var/log/supervisor/test.log　　　　　　#日志输出路径  
directory=/root/test　　　　　　　　　　　　　　　　　　　 #命令执行的工作空间  
autostart=true　　　　　　　　　　　　　　　　　　　　　　　#自动启动  
user=ubuntu(注意用户权限)　　　　　　　　　　　　　　　　　　　　　　　　　　#指定用户  
autorestart=true　　　　　　　　　　　　　　　　　　　　　　#自动重启</pre> 
```
#常用命令
配置好后:
```commandline
supervisorctl reload
```
    
基本命令：  
```
supervisorctl status #查看supervisorctl状态  
supervisorctl start nginx #启动子进程nginx  
supervisorctl stop nginx  #关闭子进程nginx  
supervisorctl restart nginx #重启子进程nginx  
sudo supervisorctl update 更新
sudo supervisorctl reload 加载
```

