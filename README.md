# AutoBackup
利用python的apscheduler模块写的数据库定时自动备份脚本
备份是用mysqldump程序，此程序是mysql数据库自带的程序，所以请确保已经安装好mysql。

用法很简单 设置好配置文件 运行.py后缀的脚本即可。

配置详解：
[baseConfig]
dbusername=root       		//数据库用户名
dbpassword=××××××		//数据库对应用户名的密码
dbName=×××××			//数据库名字
resultFileLocation=/Users/stephen/Desktop/	//要存储的备份文件的路径
interval=1			//备份间隔，单位是分钟
