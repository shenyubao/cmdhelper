#CmdHelper
控制台管理工具

##功能说明
v0.1 - 记录,调用 开发者在控制台中的常用命令
v0.2 - 提供服务器存储功能.实现跨机器调用命令

##安装说明
    0.服务依赖: python2.7 easy_install
    1.获取发布包: wget https://raw.github.com/Shenyubao/cmdhelper/master/dist/cmdhelper-0.1.1-py2.7.egg
    2.安装:easy_install cmdhelper-0.1.1-py2.7.egg
  
##使用说明
###客户端配置
    ch set uid sample_id     (用户ID,必填)
    ch set host http://1.chsyb.sinaapp.com/chserver (存储服务URL,选填)
    ch set pwd 123456    (存储服务密码,选填)

###基础功能
####chset 
    chset key value  #设置Key-Value
    eg:
    chset db.dev mysql -h 127.0.0.1 -utest --port=3600 -ptest test
    chset db.test mysql -h 127.0.0.1 -utest --port=3600 -ptest test
    chset db.pro mysql -h 127.0.0.1 -utest --port=3600 -ptest test
    
####chlist 
    chlist   #查看Key-Value
    
    #Terminal 显示:
    [  1] db.dev      : mysql -h 127.0.0.1 -utest --port=3600 -ptest test
    [  2] db.test     : mysql -h 127.0.0.2 -utest --port=3600 -ptest test
    [  3] db.pro      : mysql -h 127.0.0.3 -utest --port=3600 -ptest test
    [  4] ssh.60      : yubao1@10.0.0.60
    
####chdel
    chdel [index|key]  #删除Key-Value
    chdel 1
    chdel db.dev

####chrun
    chrun [index|key]  #执行命令
    chrun 1
    chrun db.dev  
    
####chmark
    chmark key   # 收藏当前目录
    chmark ch
    @echo
    ....
    [  5] ch          : /Projects/python/cmdhelper
  
###同步功能
####chpush
    chpush   # 提交当前K-V至服务器
####chpull
    chpull   # 从服务器更新K-V
  
  
